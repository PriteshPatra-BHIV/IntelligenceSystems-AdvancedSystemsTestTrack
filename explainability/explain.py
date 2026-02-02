"""
explain.py

Produces a human-readable explanation
for why a particular action was selected.
"""

class Explainer:
    def explain_decision(
        self,
        state,
        action,
        confidence: float,
        uncertainty_snapshot: dict
    ) -> dict:

        return {
            "state": state,
            "chosen_action": action,
            "confidence": confidence,
            "known_limits": uncertainty_snapshot,
            "claim": "Action selected based on available evidence only",
            "disclaimer": "Decision does not imply certainty or optimality"
        }
