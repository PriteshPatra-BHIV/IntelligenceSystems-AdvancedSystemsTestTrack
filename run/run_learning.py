"""
run_learning.py

Starts deterministic training.
"""

from learning.learning_loop import LearningLoop


def run(environment, policy, learner, exploration, replay_logger):
    loop = LearningLoop(
        environment=environment,
        policy=policy,
        learner=learner,
        exploration_strategy=exploration,
        replay_logger=replay_logger
    )

    loop.train(episodes=5, max_steps_per_episode=10)
