# Deterministic Reinforcement Learning Engine
## With Quantum Decision Foundations

This project implements a system-grade deterministic reinforcement learning engine designed for auditability, replayability, and explicit uncertainty handling.

## Key Characteristics
- No black-box ML
- No stochastic opacity
- Explicit learning vs execution separation
- Quantum-inspired information limits

## Architecture Overview

### Core Components (`core/`)
- **contracts.py**: Frozen system invariants and data contracts
- **state.py**: State representation with required fields
- **action.py**: Action definitions (WAIT, EXPLORE, COMMIT)
- **reward.py**: Reward handling within defined bounds (-10.0 to 10.0)

### Learning System (`learning/`)
- **learning_loop.py**: Top-level deterministic learning orchestrator
- **learner.py**: Deterministic policy update logic
- **episode_runner.py**: Episode execution with full traceability
- **exploration.py**: Controlled exploration strategies
- **replay.py**: Complete episode replay capabilities

### Execution System (`execution/`)
- **executor.py**: Read-only policy execution
- **decision.py**: Decision making with confidence tracking

### Uncertainty Management (`uncertainty/`)
- **confidence.py**: Evidence-based confidence scoring (not probability)
- **uncertainty.py**: Explicit uncertainty propagation

### Explainability (`explainability/`)
- **explain.py**: Human-readable decision explanations
- **traces.py**: Decision trace generation

### Intelligence Framework (`intelligence/`)
- **fusion/**: Signal fusion with deterministic rules
- **guarantees/**: System invariants and guarantees
- **semantics/**: Signal provenance and meaning
- **uncertainty/**: Uncertainty propagation logic

### Validation (`stress_tests/`)
- **adversarial_rewards.py**: Reward signal stress testing
- **contradictory_feedback.py**: Contradiction handling validation
- **partial_observability.py**: Incomplete information testing

## Quick Start

### Basic Learning Run
```bash
python quick_run.py
```

### Demo Run
```bash
python demo_run.py
```

### Full Test Suite
```bash
pytest tests/
```

## System Guarantees

1. **Deterministic Behavior**: Same inputs always produce same outputs
2. **Complete Auditability**: Every decision is traceable and explainable
3. **Uncertainty Honesty**: System never claims more confidence than evidence supports
4. **Replay Capability**: Any run can be perfectly reproduced
5. **No Hidden State**: All system state is explicit and inspectable

## Data Schema

States contain:
- `current_step`: Episode step counter
- `observed_signal`: Numerical observation
- `previous_action`: Last action taken
- `accumulated_reward`: Cumulative reward

Actions are limited to: `["WAIT", "EXPLORE", "COMMIT"]`

Rewards are bounded: `[-10.0, 10.0]`

## Design Philosophy

The system favors **honesty over performance** and **determinism over speculation**.

### Core Principles
- **No Black Boxes**: Every component is inspectable and explainable
- **Explicit Uncertainty**: Unknown information is never hidden or assumed
- **Separation of Concerns**: Learning and execution are strictly separated
- **Evidence-Based Confidence**: Confidence reflects evidence quality, not prediction accuracy
- **Quantum-Inspired Limits**: Information theoretical bounds are respected

## Usage Patterns

### Learning Phase
```python
from learning.learning_loop import LearningLoop
from learning.learner import Learner

# Setup components
loop = LearningLoop(env, policy, learner, exploration, logger)
loop.train(episodes=100, max_steps_per_episode=50)
```

### Execution Phase
```python
from execution.executor import Executor

executor = Executor(env, decision_engine, trained_policy)
result = executor.run_step(current_state)
```

### Explanation Generation
```python
from explainability.explain import Explainer

explainer = Explainer()
explanation = explainer.explain_decision(state, action, confidence, uncertainty)
```

## Quantum Connections

The system draws inspiration from quantum mechanics principles:
- **Measurement vs Observation**: Clear distinction between active and passive information gathering
- **Information Limits**: Fundamental bounds on knowable information
- **Uncertainty Principles**: Explicit handling of irreducible uncertainty
- **No Hidden Variables**: All system state is observable

See `quantum-notes/` for detailed theoretical foundations.

## Risk Management

### Identified Risks
- Low-quality input signals propagate uncertainty
- Persistent contradictions reduce usable confidence
- Downstream systems may misinterpret intelligence as decisions

### Mitigations
- Explicit uncertainty propagation prevents false certainty
- Deterministic fusion rules prevent hidden behavior
- Clear documentation defines system limitations

### Non-Goals
- Decision making (provides intelligence only)
- Prediction or forecasting
- Truth arbitration
- Performance optimization over correctness

## File Structure
```
core/          → System definitions and contracts
learning/      → Deterministic learning logic
execution/     → Read-only policy execution
uncertainty/   → Confidence and uncertainty modeling
explainability/→ Decision explanations and traces
intelligence/  → Signal fusion and semantic processing
quantum-notes/ → Theoretical foundations and mappings
stress_tests/  → Adversarial validation scenarios
docs/          → Detailed documentation
schema/        → Data format specifications
utils/         → Logging and validation utilities
run/           → Entry point scripts
tests/         → Comprehensive test suite
```

## Entry Points
- See [HANDOVER.md](HANDOVER.md) for complete usage instructions
- Run `python quick_run.py` for immediate demonstration
- Execute `pytest` for full validation

## Dependencies
- Python 3.11+
- No external ML libraries (by design)
- Standard library only for core functionality

## License
This project prioritizes transparency and auditability in reinforcement learning systems.