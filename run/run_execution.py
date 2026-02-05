"""
run_execution.py

Runs policy execution without learning.
"""

from execution.decision import DecisionEngine
from execution.executor import Executor


def run(environment, policy, max_steps: int = 1000):
    """Run execution with step limit to prevent infinite loops."""
    decision_engine = DecisionEngine()
    executor = Executor(environment, decision_engine, policy)

    state = environment.reset()
    step_count = 0

    while step_count < max_steps:
        result = executor.run_step(state)
        state = result["next_state"]
        step_count += 1

        if result["done"]:
            break
    
    if step_count >= max_steps:
        print(f"Warning: Execution stopped after {max_steps} steps to prevent infinite loop")
