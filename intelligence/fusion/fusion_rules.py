from intelligence.semantics.signals import Signal, SignalType


class FusionError(Exception):
    """Raised when signals cannot be fused safely."""
    pass


def fuse(a: Signal, b: Signal) -> Signal:
    """
    Deterministic fusion of two signals.

    Rules:
    - Only signals of the same type may fuse
    - Severity takes the maximum
    - Confidence never increases (min)
    - Uncertainty never decreases (max)
    """

    if a.signal_type != b.signal_type:
        raise FusionError("Signal types cannot be fused")

    # Combine provenance information to maintain traceability
    combined_provenance = f"{a.provenance}+{b.provenance}"

    if a.signal_type == SignalType.CONTRADICTION:
        # Contradictions amplify uncertainty
        return Signal(
            signal_type=SignalType.CONTRADICTION,
            provenance=combined_provenance,
            severity=max(a.severity, b.severity),
            confidence=min(a.confidence, b.confidence),
            uncertainty=min(1.0, max(a.uncertainty, b.uncertainty) + 0.2),
        )

    return Signal(
        signal_type=a.signal_type,
        provenance=combined_provenance,
        severity=max(a.severity, b.severity),
        confidence=min(a.confidence, b.confidence),
        uncertainty=max(a.uncertainty, b.uncertainty),
    )
