"""
confidence.py

Confidence scoring based on evidence, not probability.
Confidence reflects how well-supported a decision is,
not how correct it is.
"""

class ConfidenceEngine:
    MAX_VISITS_FOR_FULL_CONFIDENCE = 10.0
    
    def compute(self, state_visits: int, reward_consistency: float) -> float:
        """
        state_visits: how many times this state-action was seen
        reward_consistency: 0.0–1.0 (how stable rewards were)

        Returns confidence score in range [0.0, 1.0]
        """
        # Input validation
        if state_visits < 0:
            raise ValueError(f"state_visits must be non-negative, got {state_visits}")
        
        if not (0.0 <= reward_consistency <= 1.0):
            raise ValueError(f"reward_consistency must be in [0.0, 1.0], got {reward_consistency}")

        if state_visits == 0:
            return 0.0

        visit_factor = min(state_visits / self.MAX_VISITS_FOR_FULL_CONFIDENCE, 1.0)
        confidence = visit_factor * reward_consistency

        return round(confidence, 3)
