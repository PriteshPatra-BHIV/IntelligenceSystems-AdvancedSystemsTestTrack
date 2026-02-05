import sys
from pathlib import Path

# Add project root (multiStageSoverign) to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from intelligence.semantics.signals import Signal, SignalType, Provenance
from intelligence.fusion.fusion_rules import fuse


def test_uncertainty_never_decreases():
    s1 = Signal(
        signal_type=SignalType.OBSERVATION,
        provenance=Provenance.SENSOR,
        severity=4,
        confidence=0.9,
        uncertainty=0.2,
    )
    s2 = Signal(
        signal_type=SignalType.OBSERVATION,
        provenance=Provenance.SENSOR,
        severity=6,
        confidence=0.8,
        uncertainty=0.5,
    )

    fused = fuse(s1, s2)

    assert fused.uncertainty >= max(s1.uncertainty, s2.uncertainty)


def test_confidence_never_increases():
    s1 = Signal(
        signal_type=SignalType.ASSERTION,
        provenance=Provenance.HUMAN,
        severity=3,
        confidence=0.7,
        uncertainty=0.3,
    )
    s2 = Signal(
        signal_type=SignalType.ASSERTION,
        provenance=Provenance.HUMAN,
        severity=5,
        confidence=0.6,
        uncertainty=0.4,
    )

    fused = fuse(s1, s2)

    assert fused.confidence <= min(s1.confidence, s2.confidence)
