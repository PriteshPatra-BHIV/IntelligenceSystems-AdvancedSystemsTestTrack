# Deterministic Reinforcement Learning Engine
## With Quantum Decision Foundations

This project implements a system-grade deterministic
reinforcement learning engine designed for auditability,
replayability, and explicit uncertainty handling.

## Key Characteristics
- No black-box ML
- No stochastic opacity
- Explicit learning vs execution separation
- Quantum-inspired information limits

## Structure
- core/          → definitions and contracts
- learning/      → deterministic learning logic
- execution/     → read-only policy execution
- uncertainty/   → confidence and uncertainty modeling
- explainability/→ decision explanations
- quantum/       → study notes and mappings
- stress_tests/  → adversarial validation

## Entry Points
- See HANDOVER.md for full usage instructions

## Design Philosophy
The system favors honesty over performance
and determinism over speculation.
