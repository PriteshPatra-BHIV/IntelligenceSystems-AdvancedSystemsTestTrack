"""
exploration.py

Explicit exploration vs exploitation logic.
No randomness.
All decisions are rule-based and explainable.
"""

class ExplorationStrategy:
    def __init__(self, min_visits_required: int = 2):
        self.state_visit_counter = {}
        self.min_visits_required = min_visits_required

    def decide(self, state, step: int) -> str:
        """
        Decide whether to explore or exploit.
        """
        key = self._state_key(state)
        visits = self.state_visit_counter.get(key, 0)

        if visits < self.min_visits_required:
            return "EXPLORE"
        return "EXPLOIT"

    def explore_action(self, state):
        """
        Deterministic exploration action.
        Always selects WAIT to gather more information.
        """
        return "WAIT"

    def register_state(self, state):
        key = self._state_key(state)
        self.state_visit_counter[key] = self.state_visit_counter.get(key, 0) + 1

    def _state_key(self, state):
        return str(state)
