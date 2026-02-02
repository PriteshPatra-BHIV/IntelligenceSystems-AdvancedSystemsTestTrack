"""
state.py

Defines the agent-observable state.
State represents knowledge, not reality.
"""

from typing import Dict, Any


def validate_state(state: Dict[str, Any]) -> None:
    required_keys = [
        "current_step",
        "observed_signal",
        "previous_action",
        "accumulated_reward"
    ]

    for key in required_keys:
        if key not in state:
            raise ValueError(f"Missing state field: {key}")
