"""
run_execution.py

Runs policy execution without learning.
"""

from execution.decision import DecisionEngine
from execution.executor import Executor


def run(environment, policy):
    decision_engine = DecisionEngine()
    executor = Executor(environment, decision_engine, policy)

    state = environment.reset()

    while True:
        result = executor.run_step(state)
        state = result["next_state"]

        if result["done"]:
            break
