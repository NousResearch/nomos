from fastmcp import FastMCP
from solve_agent import SolveAgent, ProblemState
import toml
import uuid
import asyncio
import time


with open("config.toml", "r") as f:
    config = toml.load(f)

mcp = FastMCP("Nomos1 Solver")

@mcp.tool
async def solve(problem: str) -> str:
    """Solve a complex mathematical or logical problem using Nomos1 Solver."""
    agent = SolveAgent(
        problems_dir=None,
        base_url=config["models"]["base_url"],
        model=config["models"]["solve_model"],
        judge_model=config["models"]["judge_model"],
        target_perfect_scores=config["agent"]["target_perfect_score"],
        max_concurrent=int(config["agent"]["max_concurrent"]),
        time_limit_hours=float(config["agent"]["time_limit_hours"])
    )

    suid = str(uuid.uuid4())

    problem = ProblemState(
        problem_id=suid,
        problem_text=problem
    )

    problems = {
        suid: problem
    }

    agent.problems = problems
    agent.start_time = time.time()  # Initialize start_time before solving

    # Start watchdog in background (safe mode = doesn't kill process)
    watchdog = asyncio.create_task(agent._deadline_watchdog(safe=True))

    try:
        await agent.run_solving_phase()
        await agent.run_finalization_phase()
    finally:
        watchdog.cancel()

    solution = agent.get_problem_solution(suid)

    return solution if solution else "No solution generated"



if __name__ == "__main__":
    print("MCP Server sould be ran using :")
    print("fastmcp run ./mcp.py --transport http --port 9000")
    print("Then connect to it using any MCP client (tested on Insomnia).")