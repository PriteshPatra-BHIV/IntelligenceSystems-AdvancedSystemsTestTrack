"""
validators.py

Schema and contract validation helpers.
"""

from core.state import validate_state
from core.action import validate_action
from core.reward import validate_reward


def validate_transition(state, action, reward) -> None:
    validate_state(state)
    validate_action(action)
    validate_reward(reward)
