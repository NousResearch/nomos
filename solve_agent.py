#!/usr/bin/env python3
"""
Async agent for solving olympiad problems with judging, consolidation, and pairwise tournament.

Usage:
    python solve_agent.py --problems_dir=problems/ --judge_prompt=prompts/score.md --submissions_dir=submissions/
"""

import asyncio
from datetime import datetime
import os
import random
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import fire
import httpx
from openai import AsyncOpenAI
from tenacity import (
    retry,
    stop_after_delay,
    wait_exponential,
    retry_if_exception,
)


class TokenLimitError(Exception):
    """Raised when request exceeds token limit."""
    pass


class IncompleteResponseError(Exception):
    """Raised when response has non-standard stop reason."""
    pass


def _is_token_limit_error(error: BaseException) -> bool:
    """Check if error is a token/context limit error."""
    error_str = str(error).lower()
    token_error_patterns = [
        "context_length_exceeded",
        "context length",
        "maximum context",
        "token limit",
        "too many tokens",
        "max_tokens",
        "reduce the length",
        "input is too long",
    ]
    return any(pattern in error_str for pattern in token_error_patterns)


def _should_retry(error: BaseException) -> bool:
    """Determine if we should retry this error."""
    # Don't retry token limit errors
    if isinstance(error, TokenLimitError):
        return False
    if isinstance(error, IncompleteResponseError):
        return False
    if _is_token_limit_error(error):
        return False
    return True


# Valid finish reasons that indicate a complete response
VALID_FINISH_REASONS = {"stop", "end_turn", "end", "eos"}

# Safe print and rich traceback setup
def setup_rich():
    """Setup rich traceback if available."""
    try:
        from rich.traceback import install
        install(show_locals=True, suppress=[asyncio])
        return True
    except Exception:
        return False

RICH_AVAILABLE = setup_rich()

def safeprint(*args, **kwargs):
    """Print with rich if available, fallback to regular print."""
    try:
        if RICH_AVAILABLE:
            from rich import print as rprint
            rprint(*args, **kwargs)
        else:
            print(*args, **kwargs)
    except Exception:
        try:
            print(*args, **kwargs)
        except Exception:
            pass


@dataclass
class Submission:
    """A single submission for a problem."""
    problem_id: str
    content: str
    score: Optional[int] = None
    judge_feedback: Optional[str] = None
    attempt_num: int = 0


@dataclass
class ProblemState:
    """State tracking for a single problem."""
    problem_id: str
    problem_text: str
    submissions: list[Submission] = field(default_factory=list)
    perfect_submissions: list[Submission] = field(default_factory=list)
    consolidated_submissions: list[Submission] = field(default_factory=list)
    pairwise_winner: Optional[Submission] = None
    final_submission: Optional[Submission] = None
    consolidation_done: bool = False
    pairwise_done: bool = False
    attempt_count: int = 0


class SolveAgent:
    """Async agent for solving olympiad problems."""

    def __init__(
        self,
        problems_dir: str,
        judge_prompt: str = "prompts/score.md",
        submissions_dir: Optional[str] = None,
        solve_prompt: Optional[str] = None,
        consolidation_prompt: str = "prompts/consolidation.md",
        pairwise_prompt: str = "prompts/pairwise.md",
        time_limit_hours: float = 3.0,
        max_concurrent: int = 32,
        target_perfect_scores: int = 4,
        model: str = "nomos-1",
        judge_model: str = "nomos-1",
        base_url: str = "http://localhost:30000/v1",
    ):
        self.problems_dir = Path(problems_dir)
        if submissions_dir is None:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            submissions_dir = f"submissions/{self.problems_dir.name}-{timestamp}"
        self.submissions_dir = Path(submissions_dir)
        self.time_limit_seconds = time_limit_hours * 3600
        # Stop solving 15 min before end, but ensure at least 50% of time for solving
        self.early_stop_seconds = max(
            self.time_limit_seconds * 0.5,
            self.time_limit_seconds - (15 * 60)
        )
        self.max_concurrent = max_concurrent
        self.target_perfect_scores = target_perfect_scores
        self.model = model
        self.judge_model = judge_model

        # Load prompts (relative to script directory)
        base_dir = Path(__file__).parent
        self.judge_prompt_template = (base_dir / judge_prompt).read_text()
        self.solve_prompt = (base_dir / solve_prompt).read_text() if solve_prompt else None
        self.consolidation_prompt_template = (base_dir / consolidation_prompt).read_text()
        self.pairwise_prompt_template = (base_dir / pairwise_prompt).read_text()

        # State
        self.problems: dict[str, ProblemState] = {}
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.client = AsyncOpenAI(
            base_url=base_url,
            timeout=httpx.Timeout(99999, connect=60.0),
        )
        self.start_time: float = 0
        self.stopping = False
        self.finalization_started = False  # Prevents late submissions
        self.solve_tasks: set[asyncio.Task] = set()
        self.round_robin_index: int = 0
        self.round_robin_lock = asyncio.Lock()

    def _time_remaining(self) -> float:
        """Return seconds remaining before time limit."""
        return max(0, self.time_limit_seconds - (time.time() - self.start_time))

    def _should_stop_solving(self) -> bool:
        """Check if we should stop solving and start final processing."""
        return self.stopping or (time.time() - self.start_time) >= self.early_stop_seconds

    def _extract_answer(self, response: str) -> str:
        """Extract answer after last </think> tag."""
        # Find last </think> tag
        pattern = r'</think>\s*'
        matches = list(re.finditer(pattern, response, re.IGNORECASE))
        if matches:
            last_match = matches[-1]
            answer = response[last_match.end():].strip()
            return answer
        # No think tags, return as-is
        return response.strip()

    def _extract_score(self, judge_response: str) -> Optional[int]:
        """Extract score from judge response."""
        # Look for \boxed{N} pattern
        match = re.search(r'\\boxed\{(\d)\}', judge_response)
        if match:
            return int(match.group(1))
        return None

    def _extract_keep_list(self, consolidation_response: str) -> list[int]:
        """Extract keep list from consolidation response."""
        match = re.search(r'<keep>\s*\[([\d,\s]+)\]\s*</keep>', consolidation_response)
        if match:
            nums = match.group(1).split(',')
            return [int(n.strip()) for n in nums if n.strip().isdigit()]
        return []

    def _extract_verdict(self, pairwise_response: str) -> Optional[str]:
        """Extract verdict from pairwise response."""
        match = re.search(r'<verdict>\s*(1|2|tie)\s*</verdict>', pairwise_response, re.IGNORECASE)
        if match:
            return match.group(1).lower()
        return None

    @retry(
        stop=stop_after_delay(3 * 3600),  # 3 hour max retry time
        wait=wait_exponential(multiplier=2, min=4, max=300),
        retry=retry_if_exception(_should_retry),
        reraise=True,
    )
    async def _call_llm(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        check_finish_reason: bool = False,
    ) -> str:
        """Call LLM with retries and backoff."""
        try:
            async with self.semaphore:
                response = await self.client.chat.completions.create(
                    model=model or self.model,
                    messages=messages,
                    # presence_penalty=0.4,
                )
                choice = response.choices[0]
                finish_reason = choice.finish_reason

                # Check finish reason if requested
                if check_finish_reason and finish_reason not in VALID_FINISH_REASONS:
                    raise IncompleteResponseError(
                        f"Invalid finish_reason: {finish_reason}"
                    )

                return choice.message.content or ""
        except (TokenLimitError, IncompleteResponseError):
            raise
        except Exception as e:
            if _is_token_limit_error(e):
                raise TokenLimitError(str(e)) from e
            raise

    async def solve_problem(self, problem: ProblemState) -> Optional[Submission]:
        """Generate a solution for a problem."""
        if self._should_stop_solving():
            return None

        try:
            messages = []
            if self.solve_prompt:
                messages.append({"role": "system", "content": self.solve_prompt})
            messages.append({"role": "user", "content": problem.problem_text})
            response = await self._call_llm(messages, check_finish_reason=True)
            answer = self._extract_answer(response)

            problem.attempt_count += 1
            submission = Submission(
                problem_id=problem.problem_id,
                content=answer,
                attempt_num=problem.attempt_count,
            )
            return submission
        except IncompleteResponseError as e:
            problem.attempt_count += 1
            safeprint(f"[yellow]{problem.problem_id}[/yellow] attempt {problem.attempt_count}: incomplete response, skipping")
            return None
        except Exception as e:
            safeprint(f"[red]Error solving {problem.problem_id}: {e}[/red]")
            return None

    async def judge_submission(self, problem: ProblemState, submission: Submission) -> bool:
        """Judge a submission and update its score. Returns True if 7/7."""
        try:
            prompt = self.judge_prompt_template.replace("{problem}", problem.problem_text)
            prompt = prompt.replace("{answer}", submission.content)

            messages = [{"role": "user", "content": prompt}]
            response = await self._call_llm(messages, model=self.judge_model)

            # Don't log or update if finalization has started
            if self.finalization_started:
                return False

            submission.judge_feedback = response
            submission.score = self._extract_score(response)

            if submission.score is not None:
                safeprint(f"[cyan]{problem.problem_id}[/cyan] attempt {submission.attempt_num}: score {submission.score}/7")

            return submission.score == 7
        except TokenLimitError as e:
            safeprint(f"[yellow]{problem.problem_id}[/yellow] attempt {submission.attempt_num}: token limit exceeded, score 0")
            submission.score = 0
            return False
        except Exception as e:
            safeprint(f"[red]Error judging {problem.problem_id}: {e}[/red]")
            submission.score = 0
            return False

    async def consolidate(self, problem: ProblemState) -> list[Submission]:
        """Run consolidation on submissions to keep the best ones."""
        submissions = problem.perfect_submissions if problem.perfect_submissions else problem.submissions
        if len(submissions) <= 1:
            problem.consolidation_done = True
            problem.consolidated_submissions = submissions[:]
            return submissions

        # Work with a copy we can trim on token limit errors
        working_submissions = submissions[:]

        while len(working_submissions) > 1:
            try:
                # Format submissions for consolidation prompt
                submissions_text = ""
                for i, sub in enumerate(working_submissions, 1):
                    submissions_text += f"\n### Submission {i}\n\n{sub.content}\n"
                    if sub.judge_feedback:
                        submissions_text += f"\n**Judge Feedback:** {sub.judge_feedback}\n"

                prompt = self.consolidation_prompt_template.replace("{problem}", problem.problem_text)
                prompt = prompt.replace("{submissions}", submissions_text)

                messages = [{"role": "user", "content": prompt}]
                response = await self._call_llm(messages, model=self.judge_model)

                keep_indices = self._extract_keep_list(response)

                if keep_indices:
                    kept = [working_submissions[i-1] for i in keep_indices if 0 < i <= len(working_submissions)]
                    if kept:
                        problem.consolidated_submissions = kept
                        problem.consolidation_done = True
                        safeprint(f"[green]{problem.problem_id}[/green] consolidated: kept {len(kept)}/{len(submissions)}")
                        return kept

                # Fallback: keep all working submissions
                problem.consolidated_submissions = working_submissions[:]
                problem.consolidation_done = True
                return working_submissions

            except TokenLimitError:
                # Drop a random lowest-scoring submission and retry
                if len(working_submissions) <= 1:
                    break

                # Find minimum score
                min_score = min(s.score if s.score is not None else 0 for s in working_submissions)
                lowest_scored = [s for s in working_submissions if (s.score if s.score is not None else 0) == min_score]
                to_drop = random.choice(lowest_scored)
                working_submissions.remove(to_drop)
                safeprint(f"[yellow]{problem.problem_id}[/yellow] consolidation token limit, dropped submission {to_drop.attempt_num}, {len(working_submissions)} remaining")
                continue

            except Exception as e:
                safeprint(f"[red]Error consolidating {problem.problem_id}: {e}[/red]")
                problem.consolidated_submissions = working_submissions[:]
                problem.consolidation_done = True
                return working_submissions

        # Only one submission left after dropping
        problem.consolidated_submissions = working_submissions[:]
        problem.consolidation_done = True
        return working_submissions

    async def _pairwise_compare(self, problem: ProblemState, sub1: Submission, sub2: Submission) -> Submission:
        """Compare two submissions and return the winner."""
        prompt = self.pairwise_prompt_template.replace("{problem}", problem.problem_text)
        prompt = prompt.replace("{submission1}", sub1.content)
        prompt = prompt.replace("{submission2}", sub2.content)

        messages = [{"role": "user", "content": prompt}]
        response = await self._call_llm(messages, model=self.judge_model)

        verdict = self._extract_verdict(response)

        if verdict == "1":
            return sub1
        elif verdict == "2":
            return sub2
        else:  # tie or no answer
            return random.choice([sub1, sub2])

    async def pairwise_tournament(self, problem: ProblemState) -> Optional[Submission]:
        """Run pairwise tournament to find best submission."""
        submissions = problem.consolidated_submissions if problem.consolidated_submissions else problem.submissions

        if not submissions:
            return None
        if len(submissions) == 1:
            problem.pairwise_done = True
            problem.pairwise_winner = submissions[0]
            return submissions[0]

        try:
            # Single elimination tournament
            remaining = submissions[:]
            random.shuffle(remaining)  # Randomize bracket

            while len(remaining) > 1:
                # Build list of matches for this round
                matches = []
                byes = []
                for i in range(0, len(remaining), 2):
                    if i + 1 >= len(remaining):
                        byes.append(remaining[i])
                    else:
                        matches.append((remaining[i], remaining[i + 1]))

                # Run all matches in parallel
                if matches:
                    winners = await asyncio.gather(*[
                        self._pairwise_compare(problem, sub1, sub2)
                        for sub1, sub2 in matches
                    ])
                    remaining = list(winners) + byes
                else:
                    remaining = byes

            winner = remaining[0] if remaining else submissions[0]
            problem.pairwise_done = True
            problem.pairwise_winner = winner
            safeprint(f"[green]{problem.problem_id}[/green] pairwise winner: attempt {winner.attempt_num}")
            return winner

        except Exception as e:
            safeprint(f"[red]Error in pairwise for {problem.problem_id}: {e}[/red]")
            problem.pairwise_done = True
            problem.pairwise_winner = submissions[0]
            return submissions[0]

    def _get_best_submission(self, problem: ProblemState) -> Optional[Submission]:
        """Get the best submission using available data, guaranteed to return something if any submissions exist."""
        # Priority order:
        # 1. Pairwise winner
        if problem.pairwise_winner:
            return problem.pairwise_winner

        # 2. Pick from consolidated submissions
        if problem.consolidated_submissions:
            # Pick highest scored or first
            scored = [s for s in problem.consolidated_submissions if s.score is not None]
            if scored:
                return max(scored, key=lambda s: (s.score or 0))
            return problem.consolidated_submissions[0]

        # 3. Pick from perfect submissions
        if problem.perfect_submissions:
            return problem.perfect_submissions[0]

        # 4. Pick highest scored submission
        if problem.submissions:
            scored = [s for s in problem.submissions if s.score is not None]
            if scored:
                return max(scored, key=lambda s: (s.score or 0))
            return problem.submissions[0]

        return None

    async def solve_and_judge_one(self, problem: ProblemState) -> bool:
        """Solve and judge one attempt for a problem. Returns True if perfect."""
        if self._should_stop_solving():
            return False

        # Check if we have enough perfect scores
        if len(problem.perfect_submissions) >= self.target_perfect_scores:
            return False

        # Generate solution
        submission = await self.solve_problem(problem)
        if submission is None:
            return False

        # Don't add submissions after finalization has started
        if self.finalization_started:
            return False

        problem.submissions.append(submission)

        # Don't judge if finalization has started
        if self.finalization_started:
            return False

        # Judge it
        is_perfect = await self.judge_submission(problem, submission)

        # Final check - don't modify state if finalization started during judging
        if self.finalization_started:
            return False

        if is_perfect:
            problem.perfect_submissions.append(submission)
            if len(problem.perfect_submissions) >= self.target_perfect_scores:
                safeprint(f"[green]{problem.problem_id}[/green] has {len(problem.perfect_submissions)} perfect scores!")

        return is_perfect

    async def _get_next_problem(self) -> Optional[ProblemState]:
        """Get the next problem to work on - prioritize fewest perfects, round-robin among ties."""
        async with self.round_robin_lock:
            candidates = [
                p for p in self.problems.values()
                if len(p.perfect_submissions) < self.target_perfect_scores
            ]
            if not candidates:
                return None

            # Find minimum perfect score count
            min_perfects = min(len(p.perfect_submissions) for p in candidates)

            # Filter to only problems with the minimum
            priority_candidates = [
                p for p in candidates
                if len(p.perfect_submissions) == min_perfects
            ]

            # Sort by problem_id for stable round-robin order
            priority_candidates.sort(key=lambda p: p.problem_id)

            # Round-robin through priority candidates
            self.round_robin_index = self.round_robin_index % len(priority_candidates)
            selected = priority_candidates[self.round_robin_index]
            self.round_robin_index += 1

            return selected

    def _get_problem_priority(self, problem: ProblemState) -> tuple:
        """Get priority for a problem (lower = higher priority)."""
        perfect_count = len(problem.perfect_submissions)
        if perfect_count >= self.target_perfect_scores:
            return (1, 0)  # Low priority, already done
        return (0, -perfect_count)  # High priority, fewer perfects = higher priority

    async def run_solving_phase(self):
        """Run the main solving phase with prioritization and parallel requests."""
        safeprint(f"[bold blue]Starting solving phase with {self.max_concurrent} parallel workers...[/bold blue]")

        async def worker(worker_id: int):
            """Worker that continuously picks problems and solves them."""
            while not self._should_stop_solving():
                problem = await self._get_next_problem()
                if problem is None:
                    return
                await self.solve_and_judge_one(problem)
                await asyncio.sleep(0.01)

        # Launch max_concurrent workers
        tasks = []
        for i in range(self.max_concurrent):
            task = asyncio.create_task(worker(i))
            self.solve_tasks.add(task)
            tasks.append(task)

        # Wait for all tasks or timeout at early_stop
        try:
            timeout = self.early_stop_seconds - (time.time() - self.start_time)
            if timeout > 0:
                done, pending = await asyncio.wait(tasks, timeout=timeout)
                # Cancel pending tasks
                for task in pending:
                    task.cancel()
        except Exception as e:
            safeprint(f"[yellow]Solving phase interrupted: {e}[/yellow]")

        # Cancel any remaining solve tasks and move on immediately
        self.stopping = True
        for task in self.solve_tasks:
            if not task.done():
                task.cancel()

        safeprint("[cyan]Solving phase stopped, moving to finalization[/cyan]")

    async def _finalize_problem(self, problem: ProblemState) -> None:
        """Finalize a single problem (consolidation + pairwise)."""
        # Determine what to consolidate
        if len(problem.perfect_submissions) >= self.target_perfect_scores:
            to_consolidate = problem.perfect_submissions[:8]
        else:
            scored = sorted(problem.submissions, key=lambda s: (s.score or 0), reverse=True)
            to_consolidate = scored[:8]
            if to_consolidate:
                problem.perfect_submissions = to_consolidate

        if to_consolidate:
            await self.consolidate(problem)
            if len(problem.consolidated_submissions) > 1:
                await self.pairwise_tournament(problem)

        # Always ensure we have a final submission
        problem.final_submission = self._get_best_submission(problem)
        safeprint(f"[green]{problem.problem_id}[/green] finalized")

    async def run_finalization_phase(self):
        """Run consolidation and pairwise for all problems in parallel."""
        safeprint(f"[bold blue]Starting finalization phase...[/bold blue]")

        # Prevent any late submissions from modifying state
        self.finalization_started = True

        # Cancel any remaining solve tasks to free up GPUs (non-blocking)
        for task in self.solve_tasks:
            if not task.done():
                task.cancel()

        # Run all problem finalizations in parallel (watchdog handles deadline)
        tasks = [self._finalize_problem(problem) for problem in self.problems.values()]
        await asyncio.gather(*tasks, return_exceptions=True)

        # Ensure all problems have a final submission
        for problem in self.problems.values():
            if problem.final_submission is None:
                problem.final_submission = self._get_best_submission(problem)

    def write_submissions(self):
        """Write final submissions to disk."""
        self.submissions_dir.mkdir(parents=True, exist_ok=True)

        for problem in self.problems.values():
            # Ensure we have a submission
            final = problem.final_submission or self._get_best_submission(problem)

            if final is None:
                # Emergency fallback: create a placeholder
                safeprint(f"[red]WARNING: No submission for {problem.problem_id}, using problem text as placeholder[/red]")
                content = f"*Unable to generate solution within time limit.*\n\n{problem.problem_text}"
            else:
                content = final.content

            # Write to file
            filename = f"{problem.problem_id}.md"
            filepath = self.submissions_dir / filename

            output = f"# {problem.problem_id}\n\n"
            output += f"## Problem\n\n{problem.problem_text}\n\n"
            output += f"## Submission\n\n{content}\n"

            filepath.write_text(output, encoding="utf-8")
            safeprint(f"[green]Wrote {filepath}[/green]")

    async def _deadline_watchdog(self):
        """Background task that enforces hard deadline by killing the process."""
        # Trigger 1 min before deadline to allow time for writing submissions
        deadline = self.time_limit_seconds - 60
        while True:
            await asyncio.sleep(5)  # Check every 5 seconds
            elapsed = time.time() - self.start_time
            if elapsed >= deadline:
                safeprint(f"[red]WATCHDOG: Deadline approaching ({elapsed:.0f}s), force writing and exiting[/red]")
                self.finalization_started = True
                self.write_submissions()
                elapsed = time.time() - self.start_time
                safeprint(f"\n[bold green]Done in {elapsed/60:.1f} minutes[/bold green]")
                os._exit(0)

    async def run(self):
        """Main entry point."""
        self.start_time = time.time()

        # Start deadline watchdog
        watchdog = asyncio.create_task(self._deadline_watchdog())

        safeprint(f"[bold]Olympiad Solve Agent[/bold]")
        safeprint(f"Time limit: {self.time_limit_seconds/3600:.1f} hours")
        safeprint(f"Max concurrent requests: {self.max_concurrent}")
        safeprint(f"Target perfect scores: {self.target_perfect_scores}")
        safeprint("")

        # Load problems
        problem_files = sorted(self.problems_dir.glob("*.md"))
        if not problem_files:
            safeprint(f"[red]No .md files found in {self.problems_dir}[/red]")
            return

        for pf in problem_files:
            problem_id = pf.stem
            problem_text = pf.read_text().strip()
            self.problems[problem_id] = ProblemState(
                problem_id=problem_id,
                problem_text=problem_text,
            )

        safeprint(f"[cyan]Loaded {len(self.problems)} problems[/cyan]")

        try:
            # Solving phase
            await self.run_solving_phase()

            # Summary after solving
            safeprint("")
            safeprint("[bold]Solving phase complete. Summary:[/bold]")
            for pid, prob in sorted(self.problems.items()):
                perfect = len(prob.perfect_submissions)
                total = len(prob.submissions)
                safeprint(f"  {pid}: {perfect} perfect / {total} attempts")
            safeprint("")

            # Finalization phase (watchdog handles deadline)
            await self.run_finalization_phase()

        except Exception as e:
            safeprint(f"[red]Error during run: {e}[/red]")
            import traceback
            traceback.print_exc()
        finally:
            # Always write submissions, no matter what
            self.write_submissions()

            elapsed = time.time() - self.start_time
            safeprint(f"\n[bold green]Done in {elapsed/60:.1f} minutes[/bold green]")

            # Aggressively exit - don't wait for background tasks
            os._exit(0)


def main(
    problems_dir: str,
    judge_prompt: str = "prompts/score.md",
    submissions_dir: Optional[str] = None,
    solve_prompt: Optional[str] = None,
    consolidation_prompt: str = "prompts/consolidation.md",
    pairwise_prompt: str = "prompts/pairwise.md",
    time_limit_hours: float = 3.0,
    max_concurrent: int = 32,
    target_perfect_scores: int = 4,
    model: str = "nomos-1",
    judge_model: str = "nomos-1",
    base_url: str = "http://localhost:30000/v1",
):
    """
    Run the olympiad solve agent.

    Args:
        problems_dir: Directory containing .md problem files (required)
        judge_prompt: Path to judge prompt .md file
        submissions_dir: Directory to write final submissions
        solve_prompt: Path to solve system prompt
        consolidation_prompt: Path to consolidation prompt
        pairwise_prompt: Path to pairwise prompt
        time_limit_hours: Total time limit in hours (default: 3)
        max_concurrent: Max concurrent API requests (default: 32)
        target_perfect_scores: Number of 7/7 scores needed per problem (default: 4)
        model: Model to use for solving
        judge_model: Model to use for judging
        base_url: OpenAI-compatible API base URL
    """
    agent = SolveAgent(
        problems_dir=problems_dir,
        judge_prompt=judge_prompt,
        submissions_dir=submissions_dir,
        solve_prompt=solve_prompt,
        consolidation_prompt=consolidation_prompt,
        pairwise_prompt=pairwise_prompt,
        time_limit_hours=time_limit_hours,
        max_concurrent=max_concurrent,
        target_perfect_scores=target_perfect_scores,
        model=model,
        judge_model=judge_model,
        base_url=base_url,
    )
    asyncio.run(agent.run())


if __name__ == "__main__":
    fire.Fire(main)
