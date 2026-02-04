# Explicit Non-Knowledge Handling Rules

This document defines mandatory constraints that govern system behavior
when information is incomplete, uncertain, or missing.

These rules are enforced conceptually at the system level and are not optional.

---

## 1. Definition of Non-Knowledge

Non-knowledge exists when any of the following are true:
- The current state has not been observed previously
- The environment is partially observable
- Reward signals are conflicting or unstable
- Uncertainty exceeds defined thresholds

Non-knowledge is treated as a first-class system condition.

---

## 2. Action Constraints Under Non-Knowledge

### Rule NK-1: Commit Restriction
If system uncertainty exceeds a defined threshold,
the system MUST NOT select the COMMIT action.

### Rule NK-2: Forced Caution
If unseen states are present,
the system MUST prefer WAIT or EXPLORE actions.

### Rule NK-3: No Forced Action
The system MUST NOT be forced to act decisively
when available information is insufficient.

---

## 3. Confidence Constraints

### Rule NK-4: Confidence Upper Bound
System confidence MUST NOT exceed (1 − uncertainty).

### Rule NK-5: Evidence Requirement
Confidence MUST increase only through repeated,
consistent observations.

Confidence MUST decrease when uncertainty increases.

---

## 4. Knowledge Growth Limits

### Rule NK-6: No Assumed Knowledge
The system MUST NOT infer hidden environment state.

### Rule NK-7: Bounded Learning
Learning reduces uncertainty but MUST NOT eliminate it entirely.

---

## 5. Design Principle

The system is designed to behave conservatively under uncertainty.
Correctness is secondary to honesty and auditability.

The system prefers inaction over unjustified confidence.
