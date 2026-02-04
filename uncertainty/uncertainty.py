"""
uncertainty.py

Explicit uncertainty tracking.
Unknowns are recorded, not guessed.
"""

class UncertaintyModel:
    def __init__(self):
        self.unseen_states = set()
        self.partial_observations = 0

    def register_state(self, state):
        key = str(state)
        self.unseen_states.add(key)

    def mark_observed(self, state):
        key = str(state)
        if key in self.unseen_states:
            self.unseen_states.remove(key)

    def record_partial_observation(self):
        self.partial_observations += 1

    def snapshot(self) -> dict:
        return {
            "unseen_state_count": len(self.unseen_states),
            "partial_observation_count": self.partial_observations
        }
