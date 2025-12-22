# Nomos
<p align="center">
  <a href="https://x.com/NousResearch"><img src="https://img.shields.io/badge/X-NousResearch-000000?logo=x&logoColor=white" alt="X (formerly Twitter)"></a>&nbsp;<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow?logoColor=white" alt="MIT License"></a>&nbsp;<a href="https://huggingface.co/NousResearch/nomos-1"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-FFD21E" alt="Hugging Face"></a>
</p>
<p align="center">
  <img height="400" alt="image" src="https://github.com/user-attachments/assets/3f665bb9-f45b-4653-b6e9-a670b1f4c705" />
</p>

A reasoning harness for mathematical problem-solving and proof-writing in natural language.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python solve_agent.py <problems_dir> [options]
```

### Required Argumentsmassiveaxe

- `problems_dir`: Directory containing `.md` problem files

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--submissions_dir` | `submissions/{problems_dir}-{timestamp}` | Output directory for final submissions |
| `--judge_prompt` | `prompts/score.md` | Judge prompt file |
| `--solve_prompt` | `None` | Solver system prompt |
| `--consolidation_prompt` | `prompts/consolidation.md` | Consolidation prompt |
| `--pairwise_prompt` | `prompts/pairwise.md` | Pairwise comparison prompt |
| `--time_limit_hours` | `3.0` | Total time limit |
| `--max_concurrent` | `32` | Max parallel API requests |
| `--target_perfect_scores` | `4` | Number of 7/7 scores needed per problem |
| `--model` | `nomos-1` | Model for solving |
| `--judge_model` | `nomos-1` | Model for judging |
| `--base_url` | `http://localhost:30000/v1` | OpenAI-compatible API endpoint |

## Workflow

Nomos keeps working on the problems you give it until its time limit runs out or it reaches a target number of self-critiqued perfect scores on every problem. Once either termination condition is reached Nomos enters a finalization phase where it first discards a number of submissions and the remainder are judged pairwise tournament-style to select a final submission.

### Solving Phase

In the solving phase we launch `max_concurrent` parallel workers where each worker

1. Picks a problem based on priority + round-robin:
   - Priority: problems with fewest perfect scores
   - Round-robin among problems tied at the minimum
2. Generates submission.
3. Scores submission out of a maximum of 7 points.

Nomos keeps spawning workers until all problems have `target_perfect_scores` or time runs out.

### Finalization Phase

Starts 15 minutes before time limit (or at 50% of time limit for short runs). Consists of two subphases:

1. **Consolidation**: Groups submissions by conclusion, keeps what it thinks is the correct group (not necessarily the majority group).
2. **Pairwise Tournament**: Single elimination bracket among consolidated submissions, with ties resolved randomly.

### Output Format

Each final submission is written to its own markdown file in the following format:

```markdown
# problem_id

## Problem

[original problem text]

## Submission

[selected solution]
```

## Runbooks

```bash
./runbooks/run_putnam_2025_a_nomos-1.sh   # Putnam 2025 A problems
./runbooks/run_putnam_2025_b_nomos-1.sh   # Putnam 2025 B problems
```

## Results
When run on the Putnam 2025 with the [NousResearch/Nomos-1](https://huggingface.co/NousResearch/nomos-1) model, this reasoning harness achieves a score of **87/120** as graded by a human expert. Below we show a problem-wise comparison with [Qwen3/Qwen](Qwen/Qwen3-30B-A3B-Thinking-2507), which scores 24/120 under the same conditions.
<p align="center">
  <img height="400" alt="image" src="https://github.com/user-attachments/assets/46d91fb1-609b-4cae-9919-9ef27087d6f6" />
</p>

## Citation
If you would like to cite our work, please use this for now
```
@misc{nomos2025,
  title        = {Nomos},
  author       = {Jin, Roger and Quesnelle, Jeffrey and Mahan, Dakota and Guang, Chen and Teknium, Ryan and Park, Jun and Ustelbay, Ibrakhim and Kim, Samuel and Yurkevich, Miron and Zauytkhan, Adilet and Amankos, Rinat and Andreyev, Alex and Nurlanov, Damir and Abuov, Abuzer and massiveaxe, Askar},
  year         = {2025},
  howpublished = {\url{https://github.com/NousResearch/nomos}},
  note         = {GitHub repository},
}
```
