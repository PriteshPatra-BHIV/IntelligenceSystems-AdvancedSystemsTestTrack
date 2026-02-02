"""
contradictory_feedback.py

Stress test: identical states produce conflicting rewards.
System must acknowledge uncertainty instead of overfitting.
"""

def run_contradictory_feedback(environment, learning_loop):
    environment.set_reward_mode("contradictory")

    learning_loop.train(episodes=5, max_steps_per_episode=8)

    return {
        "status": "completed",
        "expectation": "Uncertainty increases; confidence remains bounded"
    }
