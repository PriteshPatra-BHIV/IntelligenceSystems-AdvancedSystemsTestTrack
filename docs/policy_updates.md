# Policy Update Logic

## Overview
The policy update mechanism is deterministic and transparent.
It updates action preferences based solely on observed rewards.

## What Changes
- Reward totals associated with (state, action) pairs
- Action preference ordering within known states

## What Never Changes
- State representation
- Action definitions
- Update rule structure

## Why This Is Deterministic
- No randomness is used
- Same episode trace produces the same policy update
- Updates depend only on recorded transitions

## Design Rationale
The policy improves by accumulating evidence, not by guessing.
Learning is incremental, replayable, and auditable.
