"""
decision.py

Final decision selection.
No learning. No exploration.
"""

class DecisionEngine:
    def decide(self, policy, state):
        action = policy.select_action(state)
        confidence = policy.get_confidence(state)

        return {
            "action": action,
            "confidence": confidence
        }
