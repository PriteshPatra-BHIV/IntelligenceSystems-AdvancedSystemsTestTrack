# Fusion Rules and Explicit Assumptions

This document defines the assumptions used when fusing
state, reward, confidence, and uncertainty into decisions.

No assumption is implicit.

---

## 1. Fusion Definition

Fusion refers to the process by which the system combines:
- Observed state
- Action history
- Reward feedback
- Confidence estimates
- Uncertainty measures

to select an action.

---

## 2. Explicit Assumptions

### Assumption FA-1: Reward Stability
The system assumes reward signals are locally stable.

If violated:
- Confidence MUST decrease
- Uncertainty MUST increase

---

### Assumption FA-2: Observation Consistency
The system assumes observations are internally consistent.

If violated:
- Exploration MUST increase
- Commit actions MUST be restricted

---

### Assumption FA-3: Bounded Environment Change
The system assumes environment dynamics do not change abruptly.

If violated:
- Learning rate MUST slow
- Confidence growth MUST halt

---

### Assumption FA-4: Finite Action Effects
The system assumes actions have bounded and finite effects.

If violated:
- System MUST enter conservative mode (WAIT-dominant)

---

## 3. Assumption Violation Handling

Assumption violations are treated as first-class events.
They do not crash the system.

Instead, violations:
- Reduce confidence
- Increase uncertainty
- Restrict decisive actions

---

## 4. Design Principle

The system does not deny assumptions.
It exposes them and degrades safely when they fail.
