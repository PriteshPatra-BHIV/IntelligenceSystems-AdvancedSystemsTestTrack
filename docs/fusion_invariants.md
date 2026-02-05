# Fusion Invariants

The fusion engine enforces the following invariants:

- Fusion is deterministic for identical inputs
- Confidence never increases during fusion
- Uncertainty never decreases during fusion
- Incompatible signals cannot be fused
- Contradictions increase uncertainty explicitly

All invariants are enforced via tests.
