# Confidence–Uncertainty Formal Constraints

This document defines strict, system-wide constraints
that govern the relationship between confidence and uncertainty.

These constraints are mandatory and non-negotiable.

---

## 1. Definitions

### Confidence
Confidence represents the degree of support
for a decision based on observed evidence.

Confidence is experience-based, not correctness-based.

### Uncertainty
Uncertainty represents the degree of incomplete,
missing, or insufficient information.

Uncertainty reflects knowledge limits, not error.

---

## 2. Core Constraint

### Rule CU-1: Upper Bound Constraint
Confidence MUST satisfy the following condition:

Confidence ≤ (1 − Uncertainty)

This constraint applies globally and at all times.

---

## 3. Propagation Rules

### Rule CU-2: Uncertainty Dominance
If uncertainty increases, confidence MUST NOT increase.

### Rule CU-3: Evidence-Gated Growth
Confidence MAY increase only if:
- Uncertainty is decreasing, and
- Observations are consistent over time

### Rule CU-4: Confidence Decay
If uncertainty remains non-zero,
confidence growth MUST asymptotically slow.

---

## 4. Failure Prevention

### Rule CU-5: No Confidence Inflation
The system MUST NOT increase confidence
through repeated exposure to identical outcomes
when uncertainty remains unchanged.

---

## 5. Design Principle

Confidence is a derivative of knowledge.
Uncertainty is a boundary on knowledge.

The system prioritizes correctness of limits
over magnitude of confidence.
