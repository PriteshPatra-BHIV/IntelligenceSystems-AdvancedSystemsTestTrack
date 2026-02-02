"""
contracts.py

Frozen system invariants.
Changing these breaks compatibility.
"""

STATE_FIELDS = [
    "current_step",
    "observed_signal",
    "previous_action",
    "accumulated_reward"
]

ACTION_SET = ["WAIT", "EXPLORE", "COMMIT"]

REWARD_RANGE = (-10.0, 10.0)
