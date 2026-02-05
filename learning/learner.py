"""
learner.py

Deterministic policy update logic.
This module:
- Takes a completed episode trace
- Updates the policy deterministically
- Contains NO environment interaction
"""

from typing import List, Dict, Any, Protocol


class Policy(Protocol):
    def update(self, state: Dict[str, Any], action: str, reward: float) -> None:
        ...


class Learner:
    def update_policy(self, policy: Policy, episode_trace: List[Dict[str, Any]]) -> None:
        """
        policy: mutable policy object
        episode_trace: list of transitions from one episode
        """
        if not episode_trace:
            return

        for transition in episode_trace:
            # Validate transition structure
            required_keys = ["state", "action", "reward"]
            for key in required_keys:
                if key not in transition:
                    raise ValueError(f"Missing required key '{key}' in transition")
            
            state = transition["state"]
            action = transition["action"]
            reward = transition["reward"]

            # Deterministic update rule:
            # Accumulate reward per (state, action) pair
            policy.update(state, action, reward)
