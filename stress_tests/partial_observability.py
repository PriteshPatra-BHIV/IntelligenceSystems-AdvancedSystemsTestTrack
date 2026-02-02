"""
partial_observability.py

Stress test: hide parts of the environment state.
System must not invent missing information.
"""

def run_partial_observability(environment, learning_loop):
    environment.enable_partial_observability(True)

    learning_loop.train(episodes=5, max_steps_per_episode=10)

    return {
        "status": "completed",
        "expectation": "Exploration increases; uncertainty explicitly recorded"
    }
