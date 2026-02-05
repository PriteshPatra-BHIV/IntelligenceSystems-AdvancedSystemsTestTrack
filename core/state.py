"""
state.py

Defines the agent-observable state.
State represents knowledge, not reality.
"""

from typing import Dict, Any
from core.contracts import ACTION_SET, REWARD_RANGE


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
    
    # Validate field types and values
    current_step = state["current_step"]
    if not isinstance(current_step, int) or current_step < 0:
        raise ValueError(f"current_step must be non-negative integer, got {current_step}")
    
    observed_signal = state["observed_signal"]
    if not isinstance(observed_signal, (int, float)):
        raise ValueError(f"observed_signal must be numeric, got {type(observed_signal)}")
    
    previous_action = state["previous_action"]
    if previous_action not in ACTION_SET:
        raise ValueError(f"previous_action must be one of {ACTION_SET}, got {previous_action}")
    
    accumulated_reward = state["accumulated_reward"]
    if not isinstance(accumulated_reward, (int, float)):
        raise ValueError(f"accumulated_reward must be numeric, got {type(accumulated_reward)}")
    
    min_reward, max_reward = REWARD_RANGE
    if not (min_reward <= accumulated_reward <= max_reward):
        raise ValueError(f"accumulated_reward must be in range {REWARD_RANGE}, got {accumulated_reward}")
