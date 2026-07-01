"""Tests for the consolidation input cap in solve_agent._finalize_problem.

When a problem has enough perfect submissions to take the "perfect" branch in
`_finalize_problem`, the number of submissions handed to `consolidate()` (and
therefore embedded in the consolidation prompt) must be capped at 8. Otherwise
an overshoot of perfect submissions blows past the guard and forces the
TokenLimitError random-drop fallback the cap exists to avoid.
"""

import asyncio

import solve_agent
from solve_agent import ProblemState, Submission, SolveAgent

CONSOLIDATION_CAP = 8


def _make_agent(target_perfect_scores: int = 4):
    """Build a SolveAgent without running the network/prompt-file heavy __init__."""
    agent = SolveAgent.__new__(SolveAgent)
    agent.judge_model = "test-model"
    agent.target_perfect_scores = target_perfect_scores
    # Minimal templates containing the placeholders consolidate() fills in.
    agent.consolidation_prompt_template = "PROBLEM:\n{problem}\nSUBMISSIONS:\n{submissions}"
    agent.pairwise_prompt_template = "{problem}\n{submission1}\n{submission2}"
    return agent


def _make_problem(num_perfect: int) -> ProblemState:
    problem = ProblemState(problem_id="P1", problem_text="prove something")
    for i in range(num_perfect):
        sub = Submission(
            problem_id="P1",
            content=f"solution body {i}",
            score=7,
            judge_feedback="looks perfect",
            attempt_num=i,
        )
        problem.submissions.append(sub)
        problem.perfect_submissions.append(sub)
    return problem


def _run_finalize_and_capture(num_perfect: int, target_perfect_scores: int = 4) -> int:
    """Run _finalize_problem and return the max number of '### Submission' blocks
    that appeared in any consolidation prompt sent to the LLM."""
    agent = _make_agent(target_perfect_scores=target_perfect_scores)
    problem = _make_problem(num_perfect)

    max_blocks = {"n": 0}

    async def fake_call_llm(messages, model=None, **kwargs):
        content = messages[-1]["content"]
        # Only consolidation prompts carry the "### Submission" blocks.
        if "### Submission" in content:
            blocks = content.count("### Submission ")
            max_blocks["n"] = max(max_blocks["n"], blocks)
            # Keep a single submission so consolidation terminates immediately
            # and no pairwise tournament runs.
            return "analysis...\n<keep>[1]</keep>"
        # Any other (e.g. pairwise) call: return a harmless response.
        return "<answer>1</answer>"

    agent._call_llm = fake_call_llm
    asyncio.run(agent._finalize_problem(problem))
    return max_blocks["n"]


def test_perfect_branch_caps_consolidation_input_at_8():
    # 12 perfect submissions, target of 4 -> takes the "perfect" branch.
    blocks = _run_finalize_and_capture(num_perfect=12, target_perfect_scores=4)
    assert blocks > 0, "consolidation prompt was never built"
    assert blocks <= CONSOLIDATION_CAP, (
        f"consolidation prompt contained {blocks} submissions, "
        f"expected at most {CONSOLIDATION_CAP}"
    )


def test_perfect_branch_high_target_still_caps():
    # Higher --target_perfect_scores than the cap must still be capped at 8.
    blocks = _run_finalize_and_capture(num_perfect=12, target_perfect_scores=12)
    assert blocks <= CONSOLIDATION_CAP, (
        f"consolidation prompt contained {blocks} submissions, "
        f"expected at most {CONSOLIDATION_CAP}"
    )


def test_fewer_than_cap_passes_all_through():
    # Sanity: with <= 8 perfect submissions all of them are consolidated.
    blocks = _run_finalize_and_capture(num_perfect=5, target_perfect_scores=4)
    assert blocks == 5


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"PASS {name}")
