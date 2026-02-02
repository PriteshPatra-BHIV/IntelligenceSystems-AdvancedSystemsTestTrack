# Handover Document

## Purpose
This repository contains a deterministic reinforcement learning system
with explicit uncertainty modeling and quantum-inspired decision limits.

## How to Run Learning
- Use run_learning.py
- Episodes and steps are fixed
- Replay logs are generated automatically

## How to Replay
- Load replay logs from replay_logs/
- Use replay engine to verify identical behavior

## What to Trust
- Deterministic behavior
- Replay fidelity
- Explicit uncertainty reporting

## What NOT to Trust
- Claims of optimality
- High confidence under limited data

## Known Limitations
- Partial observability restricts learning
- Adversarial rewards reduce confidence
- System prioritizes transparency over performance
