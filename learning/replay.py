"""
replay.py

Deterministic replay engine.
Replays logged episodes and verifies identical behavior.
"""

class ReplayDivergenceError(Exception):
    """Raised when replay produces different results than original run."""
    pass

class ReplayEngine:
    def __init__(self, environment, policy):
        self.environment = environment
        self.policy = policy

    def replay(self, replay_log: dict) -> None:
        self.environment.reset()

        for i, transition in enumerate(replay_log["episode_trace"]):
            expected_action = transition["action"]
            state = transition["state"]

            actual_action = self.policy.select_action(state)

            if actual_action != expected_action:
                error_msg = (
                    f"Replay divergence at step {i}: "
                    f"expected action '{expected_action}', "
                    f"got '{actual_action}' for state {state}"
                )
                raise ReplayDivergenceError(error_msg)

            self.environment.step(actual_action)
