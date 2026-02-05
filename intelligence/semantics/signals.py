# intelligence/semantics/signals.py
from enum import Enum
from dataclasses import dataclass
from typing import Literal


class SignalType(Enum):
    OBSERVATION = "observation"
    ASSERTION = "assertion"
    CONTRADICTION = "contradiction"


class Provenance(Enum):
    SENSOR = "sensor"
    HUMAN = "human"
    SYSTEM = "system"


@dataclass(frozen=True)
class Signal:
    signal_type: SignalType
    provenance: Provenance
    severity: int          # impact magnitude (0–10)
    confidence: float      # source confidence (0.0–1.0)
    uncertainty: float     # epistemic uncertainty (0.0–1.0)
