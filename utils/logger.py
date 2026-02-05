"""
logger.py

Deterministic logger.
No timestamps. No randomness.
"""

from typing import List, Dict, Any

class DeterministicLogger:
    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def log(self, record: Dict[str, Any]) -> None:
        self.records.append(record)

    def export(self) -> List[Dict[str, Any]]:
        # Return copy to prevent external modification
        return self.records.copy()
