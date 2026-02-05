# System Handover Document

This document provides complete instructions for using, maintaining, and extending the Deterministic Reinforcement Learning Engine without requiring the original author.

## Prerequisites

### System Requirements
- Python 3.11 or higher
- No external ML libraries (intentional design choice)
- Standard library dependencies only

### Installation
1. Clone the repository
2. Verify Python version: `python --version`
3. Navigate to project root
4. Run validation: `pytest tests/`

**All tests must pass before system usage.**

## Quick Validation

### Immediate Test
```bash
python quick_run.py
```
Expected output: "Learning run completed deterministically"

### Demo Run
```bash
python demo_run.py
```
Expected output: Deterministic episode completion messages

### Full Test Suite
```bash
pytest tests/ -v
```
All tests must pass. Any failures indicate system integrity issues.

## Core Usage Patterns

### 1. Learning Phase

```python
from learning.learning_loop import LearningLoop
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from utils.logger import DeterministicLogger

# Initialize components
env = YourEnvironment()  # Must implement reset() and step()
policy = YourPolicy()    # Must implement select_action(), update(), snapshot()
learner = Learner()
exploration = ExplorationStrategy()
logger = DeterministicLogger()

# Run learning
loop = LearningLoop(env, policy, learner, exploration, logger)
loop.train(episodes=100, max_steps_per_episode=50)

# Access replay logs
replay_data = logger.export()
```

### 2. Execution Phase

```python
from execution.executor import Executor
from execution.decision import DecisionEngine

# Load trained policy
executor = Executor(env, DecisionEngine(), trained_policy)

# Execute single step
state = env.reset()
result = executor.run_step(state)
# result contains: decision, next_state, reward, done
```

### 3. Explanation Generation

```python
from explainability.explain import Explainer
from uncertainty.confidence import ConfidenceEngine

explainer = Explainer()
confidence_engine = ConfidenceEngine()

# Generate explanation
confidence = confidence_engine.compute(state_visits=5, reward_consistency=0.8)
explanation = explainer.explain_decision(state, action, confidence, uncertainty_data)
```

## System Contracts

### Environment Interface
Your environment must implement:
```python
class YourEnvironment:
    def reset(self) -> dict:
        # Return state dict with required fields
        return {
            "current_step": 0,
            "observed_signal": float,
            "previous_action": "WAIT",
            "accumulated_reward": 0.0
        }
    
    def step(self, action: str) -> tuple:
        # Return (next_state, reward, done, info)
        pass
```

### Policy Interface
Your policy must implement:
```python
class YourPolicy:
    def select_action(self, state: dict) -> str:
        # Return one of: "WAIT", "EXPLORE", "COMMIT"
        pass
    
    def update(self, state: dict, action: str, reward: float) -> None:
        # Deterministic update only
        pass
    
    def snapshot(self) -> dict:
        # Return complete policy state for replay
        pass
    
    def get_confidence(self, state: dict) -> float:
        # Return confidence in [0.0, 1.0]
        pass
```

### State Schema (Mandatory)
All states must contain exactly these fields:
- `current_step`: integer (episode step counter)
- `observed_signal`: number (observation value)
- `previous_action`: string (one of ACTION_SET)
- `accumulated_reward`: number (cumulative reward)

### Action Schema (Fixed)
Actions are limited to: `["WAIT", "EXPLORE", "COMMIT"]`
**Do not modify ACTION_SET in core/contracts.py**

### Reward Schema (Bounded)
Rewards must be in range `[-10.0, 10.0]`
**Do not modify REWARD_RANGE in core/contracts.py**

## Safe Extension Guidelines

### Adding New Components

#### 1. New Signal Types
```python
# In intelligence/semantics/signals.py
class NewSignalType:
    def __init__(self, data, provenance):
        self.data = data
        self.provenance = provenance
        self.uncertainty = self._compute_uncertainty()
```

#### 2. New Fusion Rules
```python
# In intelligence/fusion/fusion_rules.py
def new_fusion_rule(signals):
    # Must include uncertainty propagation
    # Must be deterministic
    # Must include invariant tests
    pass
```

#### 3. New Exploration Strategies
```python
# In learning/exploration.py
class NewExplorationStrategy:
    def should_explore(self, state, policy_confidence):
        # Must be deterministic
        # Must respect uncertainty bounds
        pass
```

### Mandatory Testing for Extensions

When adding new components:

1. **Determinism Test**: Same inputs must produce same outputs
```python
def test_determinism():
    result1 = your_component.process(input_data)
    result2 = your_component.process(input_data)
    assert result1 == result2
```

2. **Uncertainty Preservation**: Uncertainty must never decrease without evidence
```python
def test_uncertainty_preservation():
    initial_uncertainty = component.get_uncertainty()
    component.process_without_new_evidence()
    final_uncertainty = component.get_uncertainty()
    assert final_uncertainty >= initial_uncertainty
```

3. **Replay Compatibility**: All operations must be replayable
```python
def test_replay_compatibility():
    logger = DeterministicLogger()
    # Run operation with logging
    # Replay from logs
    # Assert identical results
```

## Stress Testing

### Required Validation Scenarios

Before deployment, run all stress tests:

```bash
python stress_tests/adversarial_rewards.py
python stress_tests/contradictory_feedback.py
python stress_tests/partial_observability.py
```

### Custom Stress Tests

Add new stress tests for your domain:
```python
def stress_test_your_scenario():
    # Create adversarial conditions
    # Run system
    # Verify deterministic behavior
    # Verify uncertainty handling
    pass
```

## Debugging and Troubleshooting

### Common Issues

#### 1. Non-Deterministic Behavior
**Symptoms**: Different outputs for same inputs
**Causes**: 
- Random number generation
- Timestamp usage
- Unordered data structures

**Solution**: Remove all sources of randomness

#### 2. Confidence Inflation
**Symptoms**: Confidence increases without new evidence
**Causes**: 
- Incorrect uncertainty propagation
- Missing evidence tracking

**Solution**: Audit confidence computation logic

#### 3. Replay Failures
**Symptoms**: Replay produces different results
**Causes**:
- Incomplete state logging
- External dependencies
- Non-deterministic operations

**Solution**: Ensure complete state capture

### Diagnostic Tools

#### 1. Determinism Checker
```python
from utils.validators import validate_determinism
validate_determinism(your_component, test_inputs)
```

#### 2. Uncertainty Auditor
```python
from intelligence.uncertainty.propagation import audit_uncertainty_flow
audit_uncertainty_flow(your_pipeline)
```

#### 3. Replay Validator
```python
from learning.replay import validate_replay
validate_replay(original_logs, replay_results)
```

## System Boundaries and Limitations

### What the System Does
- Provides structured intelligence about state-action relationships
- Maintains explicit uncertainty tracking
- Enables complete auditability and replay
- Offers evidence-based confidence scoring

### What the System Does NOT Do
- Make decisions (provides intelligence only)
- Predict future outcomes
- Resolve ambiguous situations
- Optimize for performance over correctness
- Use machine learning or neural networks

### Critical Constraints

#### 1. Never Reduce Uncertainty Without Evidence
```python
# WRONG
def bad_fusion(uncertain_signals):
    return average(signals)  # Reduces uncertainty artificially

# CORRECT
def good_fusion(uncertain_signals):
    result = combine(signals)
    result.uncertainty = propagate_uncertainty(signals)
    return result
```

#### 2. Never Hide System State
```python
# WRONG
class BadPolicy:
    def __init__(self):
        self._hidden_state = {}  # Not accessible

# CORRECT
class GoodPolicy:
    def snapshot(self):
        return complete_state_dict  # Everything accessible
```

#### 3. Never Assume Missing Information
```python
# WRONG
def bad_handler(partial_state):
    if 'missing_field' not in partial_state:
        partial_state['missing_field'] = default_value  # Assumption

# CORRECT
def good_handler(partial_state):
    if 'missing_field' not in partial_state:
        raise MissingInformationError("Cannot proceed without field")
```

## Maintenance Schedule

### Daily (If In Production)
- Monitor replay log integrity
- Verify deterministic behavior on sample runs

### Weekly
- Run full test suite: `pytest tests/`
- Execute all stress tests
- Review uncertainty propagation logs

### Monthly
- Audit confidence score distributions
- Review system boundary violations
- Update documentation for any extensions

### Before Any Changes
1. Run complete test suite
2. Document expected behavior changes
3. Add tests for new functionality
4. Verify backward compatibility
5. Update this handover document

## Emergency Procedures

### System Producing Non-Deterministic Results
1. Stop all operations immediately
2. Run diagnostic: `python utils/determinism_check.py`
3. Identify source of randomness
4. Revert to last known good state
5. Fix issue with proper testing

### Confidence Scores Appear Inflated
1. Audit confidence computation: `python utils/confidence_audit.py`
2. Check uncertainty propagation chain
3. Verify evidence tracking
4. Recalibrate if necessary

### Replay Failures
1. Compare original and replay logs
2. Identify state differences
3. Check for external dependencies
4. Ensure complete state capture

## Contact and Escalation

This system is designed to be maintainable without the original author. However, if critical issues arise:

1. Consult the comprehensive documentation in `docs/`
2. Review quantum theoretical foundations in `quantum-notes/`
3. Examine similar issues in `stress_tests/`
4. Check system guarantees in `intelligence/guarantees/`

## Success Criteria

The system is working correctly when:
- All tests pass consistently
- Replay produces identical results
- Uncertainty never decreases without evidence
- Confidence reflects evidence quality
- All decisions are explainable
- No hidden state exists

**Remember**: This system prioritizes correctness and transparency over performance. Never compromise these principles for speed or convenience.