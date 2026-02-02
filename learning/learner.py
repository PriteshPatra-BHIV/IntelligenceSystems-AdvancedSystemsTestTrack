"""
learner.py

Deterministic policy update logic.
This module:
- Takes a completed episode trace
- Updates the policy deterministically
- Contains NO environment interaction
"""

from typing import List, Dict, Any


class Learner:
    def update_policy(self, policy, episode_trace: List[Dict[str, Any]]) -> None:
        """
        policy: mutable policy object
        episode_trace: list of transitions from one episode
        """

        for transition in episode_trace:
            state = transition["state"]
            action = transition["action"]
            reward = transition["reward"]

            # Deterministic update rule:
            # Accumulate reward per (state, action) pair
            policy.update(state, action, reward)
