"""
logger.py

Deterministic logger.
No timestamps. No randomness.
"""

class DeterministicLogger:
    def __init__(self):
        self.records = []

    def log(self, record: dict) -> None:
        self.records.append(record)

    def export(self) -> list:
        return self.records
