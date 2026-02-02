"""
action.py

Defines the finite action space.
Actions are explicit and enumerable.
"""

ACTIONS = {
    "WAIT",
    "EXPLORE",
    "COMMIT"
}


def validate_action(action: str) -> None:
    if action not in ACTIONS:
        raise ValueError(f"Invalid action: {action}")
