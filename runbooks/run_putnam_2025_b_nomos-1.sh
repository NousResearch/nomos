#!/bin/bash
# Run solve agent on Putnam 2025 B problems
# 6 problems, 3 hour time limit

cd "$(dirname "$0")/.."

python3 solve_agent.py \
    problems/putnam-2025/b \
    --submissions_dir=submissions/nomos-1/putnam_2025/b \
    --time_limit_hours=3.0 \
    --model=nomos-1 \
    --judge_model=nomos-1 \
    --max_concurrent=128 \
    --target_perfect_scores=4
