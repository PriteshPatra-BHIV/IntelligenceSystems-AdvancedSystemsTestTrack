"""
replay.py

Deterministic replay engine.
Replays logged episodes and verifies identical behavior.
"""

class ReplayEngine:
    def __init__(self, environment, policy):
        self.environment = environment
        self.policy = policy

    def replay(self, replay_log: dict) -> None:
        self.environment.reset()

        for transition in replay_log["episode_trace"]:
            expected_action = transition["action"]
            state = transition["state"]

            actual_action = self.policy.select_action(state)

            assert actual_action == expected_action, (
                "Replay divergence detected"
            )

            self.environment.step(actual_action)
