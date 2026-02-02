"""
traces.py

Decision trace builder.
Captures step-by-step reasoning for audit.
"""

class DecisionTrace:
    def __init__(self):
        self.trace = []

    def record(self, explanation: dict):
        self.trace.append(explanation)

    def export(self) -> list:
        return self.trace
