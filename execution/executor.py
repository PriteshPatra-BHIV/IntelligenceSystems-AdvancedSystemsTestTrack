"""
executor.py

Executes decisions using a fixed policy.
"""

class Executor:
    def __init__(self, environment, decision_engine, policy):
        self.environment = environment
        self.decision_engine = decision_engine
        self.policy = policy

    def run_step(self, state):
        decision = self.decision_engine.decide(self.policy, state)
        next_state, reward, done, _ = self.environment.step(
            decision["action"]
        )

        return {
            "decision": decision,
            "next_state": next_state,
            "reward": reward,
            "done": done
        }
