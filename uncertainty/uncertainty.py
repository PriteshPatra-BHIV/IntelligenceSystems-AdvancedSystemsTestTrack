"""
uncertainty.py

Explicit uncertainty tracking.
Unknowns are recorded, not guessed.
"""

import hashlib
from typing import Dict, Any

class UncertaintyModel:
    def __init__(self):
        self.unseen_states = set()
        self.partial_observations = 0

    def register_state(self, state: Dict[str, Any]):
        key = self._safe_state_key(state)
        self.unseen_states.add(key)

    def mark_observed(self, state: Dict[str, Any]):
        key = self._safe_state_key(state)
        if key in self.unseen_states:
            self.unseen_states.remove(key)

    def record_partial_observation(self):
        self.partial_observations += 1

    def snapshot(self) -> dict:
        return {
            "unseen_state_count": len(self.unseen_states),
            "partial_observation_count": self.partial_observations
        }
    
    def _safe_state_key(self, state: Dict[str, Any]) -> str:
        """Create a robust hash-based key for state identification."""
        # Sort keys for consistent hashing
        state_str = str(sorted(state.items()))
        return hashlib.md5(state_str.encode()).hexdigest()
