# Handover Document

This system is designed to be used and maintained without its original author.

## How to Run

1. Clone the repository
2. Ensure Python 3.11+ is installed
3. From the project root, run:
   pytest

All tests must pass before usage.

## System Expectations

- Inputs must be explicit Signal objects
- Outputs must be consumed as structured intelligence
- Uncertainty must be respected by downstream systems

## Safe Extension Rules

- Add new SignalTypes explicitly
- Update fusion rules only with invariant tests
- Uncertainty must never be reduced without evidence

## What Not to Do

- Do not add machine learning
- Do not infer missing data
- Do not collapse ambiguity
- Do not treat outputs as decisions
