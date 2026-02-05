import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from intelligence.semantics.signals import Signal, SignalType, Provenance
from intelligence.fusion.fusion_rules import fuse


def test_contradiction_increases_uncertainty():
    s1 = Signal(SignalType.CONTRADICTION, Provenance.SYSTEM, 5, 0.6, 0.4)
    s2 = Signal(SignalType.CONTRADICTION, Provenance.SYSTEM, 5, 0.6, 0.4)

    fused = fuse(s1, s2)

    assert fused.uncertainty > 0.4
