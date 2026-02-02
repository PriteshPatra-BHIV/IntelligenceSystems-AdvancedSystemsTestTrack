"""
episode_runner.py

Runs a single deterministic episode.
This module:
- Uses the current policy
- Applies exploration rules
- Collects a full transition trace
- NEVER updates the policy
"""

from typing import Dict, List, Any


class EpisodeRunner:
    def __init__(self, environment, policy, exploration_strategy):
        """
        environment: object exposing reset() and step(action)
        policy: deterministic policy object
        exploration_strategy: explicit exploration controller
        """
        self.environment = environment
        self.policy = policy
        self.exploration = exploration_strategy

    def run_episode(self, max_steps: int) -> Dict[str, Any]:
        state = self.environment.reset()
        episode_trace: List[Dict[str, Any]] = []

        for step in range(max_steps):
            # Decide whether to explore or exploit (explicit rule)
            mode = self.exploration.decide(state, step)

            if mode == "EXPLORE":
                action = self.exploration.explore_action(state)
            else:
                action = self.policy.select_action(state)

            next_state, reward, done, info = self.environment.step(action)

            transition = {
                "step": step,
                "state": state,
                "action": action,
                "reward": reward,
                "next_state": next_state,
                "mode": mode
            }

            episode_trace.append(transition)

            state = next_state

            if done:
                break

        return {
            "episode_length": len(episode_trace),
            "trace": episode_trace
        }
