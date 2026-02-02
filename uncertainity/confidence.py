"""
confidence.py

Confidence scoring based on evidence, not probability.
Confidence reflects how well-supported a decision is,
not how correct it is.
"""

class ConfidenceEngine:
    def compute(self, state_visits: int, reward_consistency: float) -> float:
        """
        state_visits: how many times this state-action was seen
        reward_consistency: 0.0–1.0 (how stable rewards were)

        Returns confidence score in range [0.0, 1.0]
        """

        if state_visits == 0:
            return 0.0

        visit_factor = min(state_visits / 10.0, 1.0)
        confidence = visit_factor * reward_consistency

        return round(confidence, 3)
