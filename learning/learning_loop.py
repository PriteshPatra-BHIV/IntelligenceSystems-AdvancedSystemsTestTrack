"""
learning_loop.py

Top-level deterministic learning orchestrator.
This module:
- Runs episodes
- Updates policy deterministically
- Logs everything needed for replay
"""

from typing import Dict, Any
from learning.episode_runner import EpisodeRunner


class LearningLoop:
    def __init__(self, environment, policy, learner, exploration_strategy, replay_logger):
        """
        environment: deterministic environment
        policy: policy object (mutable only by learner)
        learner: policy update logic
        exploration_strategy: exploration controller
        replay_logger: deterministic logger
        """
        self.environment = environment
        self.policy = policy
        self.learner = learner
        self.exploration = exploration_strategy
        self.replay_logger = replay_logger
        
        # Create episode runner once for efficiency
        self.episode_runner = EpisodeRunner(
            environment=self.environment,
            policy=self.policy,
            exploration_strategy=self.exploration
        )

    def train(self, episodes: int, max_steps_per_episode: int) -> None:
        for episode_id in range(episodes):
            episode_result = self.episode_runner.run_episode(max_steps_per_episode)

            # Deterministic policy update
            self.learner.update_policy(
                policy=self.policy,
                episode_trace=episode_result["trace"]
            )

            # Log everything needed for replay
            log_record: Dict[str, Any] = {
                "episode_id": episode_id,
                "policy_snapshot": self.policy.snapshot(),
                "episode_trace": episode_result["trace"]
            }

            self.replay_logger.log(log_record)
