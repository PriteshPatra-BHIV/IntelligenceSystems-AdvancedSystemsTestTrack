"""
explain.py

Produces a human-readable explanation
for why a particular action was selected.
"""

from typing import Dict, Any

class Explainer:
    def explain_decision(
        self,
        state: Dict[str, Any],
        action: str,
        confidence: float,
        uncertainty_snapshot: Dict[str, Any]
    ) -> Dict[str, Any]:

        return {
            "state": state,
            "chosen_action": action,
            "confidence": confidence,
            "known_limits": uncertainty_snapshot,
            "claim": "Action selected based on available evidence only",
            "disclaimer": "Decision does not imply certainty or optimality"
        }
