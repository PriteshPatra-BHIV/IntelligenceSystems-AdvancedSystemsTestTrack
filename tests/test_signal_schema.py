import sys
from pathlib import Path

# Add project root (multiSignalSovereign) to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from intelligence.semantics.signals import Signal, SignalType, Provenance


def test_signal_creation():
    signal = Signal(
        signal_type=SignalType.OBSERVATION,
        provenance=Provenance.SENSOR,
        severity=5,
        confidence=0.8,
        uncertainty=0.2,
    )

    assert signal.signal_type == SignalType.OBSERVATION
    assert signal.provenance == Provenance.SENSOR
    assert 0 <= signal.severity <= 10
    assert 0.0 <= signal.confidence <= 1.0
    assert 0.0 <= signal.uncertainty <= 1.0
