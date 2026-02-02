# Deterministic Reinforcement Learning Model

## A. Problem Statement
The system is a deterministic decision-making agent that selects actions
based on observed state information to maximize long-term reward.
The agent operates under partial observability and must make decisions
with bounded uncertainty.
The objective is not optimality under randomness, but reproducible,
explainable policy learning under explicit information limits.

---

## B. State Space

### Observable State
These are the variables available to the agent at decision time.
They are serializable and replayable.

Examples:
- current_step (int)
- observed_signal (float)
- previous_action (enum)
- accumulated_reward (float)

Observable state represents **agent knowledge**, not full reality.

### Hidden State
These variables exist in the environment but are not directly observable.

Examples:
- true_environment_condition
- delayed consequences
- external disturbances

Hidden state may influence rewards but is never directly accessed
by the agent.

---

## C. Action Space
The agent operates on a finite, discrete action set.

Allowed actions:
- WAIT        → do nothing, gather more information
- EXPLORE     → take action to reduce uncertainty
- COMMIT      → act decisively based on current policy

Each action is explicit and explainable.
No free-form or continuous actions are allowed.

---

## D. Reward Function
The reward is a deterministic numeric signal.

Properties:
- Range: -10.0 to +10.0
- Issued at end of each step
- Derived only from observable outcomes

Important:
Reward is not ground truth.
Reward is a feedback signal, not certainty or correctness.

---

## E. Policy Representation
The policy is represented as a deterministic mapping:

(state_features) → (action, confidence_score)

Policy characteristics:
- No randomness
- No neural networks
- Fully replayable
- Updateable only by the learning module

The policy does not know hidden state and never infers it directly.

---

## F. Separation of Environment State vs Agent Knowledge
The environment maintains a true internal state.
The agent maintains a belief state derived from observation.

Observation ≠ Reality  
Knowledge ≠ Truth  

This separation is intentional and fundamental to the system design.
