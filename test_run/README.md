# Test Run Scripts

This folder contains comprehensive test scripts to validate and demonstrate the entire Deterministic RL Engine project.

## Scripts Overview

### 1. `run_full_project.py` - Complete System Test
**Purpose**: Comprehensive testing of all system components
**Usage**: `python test_run/run_full_project.py`

**Test Coverage**:
- ✅ Core validation (state, confidence, uncertainty)
- ✅ Learning phase (3 episodes with intelligent policy)
- ✅ Execution phase (trained policy execution)
- ✅ Replay verification (deterministic behavior)
- ✅ Explainability demo (decision explanations)
- ✅ Uncertainty tracking (evidence-based confidence)
- ✅ Stress testing (error handling validation)

**Expected Output**: 7/7 tests passed with detailed progress logs

### 2. `quick_validation.py` - Fast System Check
**Purpose**: Quick validation of core components
**Usage**: `python test_run/quick_validation.py`

**Test Coverage**:
- ✅ System contracts validation
- ✅ State validation logic
- ✅ Confidence engine functionality
- ✅ Learning components integration

**Expected Output**: 4/4 tests passed in under 5 seconds

### 3. `demo_system.py` - Interactive Demonstration
**Purpose**: Showcase system capabilities with detailed output
**Usage**: `python test_run/demo_system.py`

**Demonstrations**:
- 🎯 Learning process with adaptive policy
- 🚀 Policy execution with phase transitions
- 📊 Decision explanations with confidence scores
- 📈 Uncertainty evolution across scenarios
- 🔄 Deterministic replay verification

**Expected Output**: Interactive demonstration with formatted tables and progress indicators

## Quick Start

### Run Everything (Recommended)
```bash
# Full system validation
python test_run/run_full_project.py

# If all tests pass, run demonstration
python test_run/demo_system.py
```

### Quick Check Only
```bash
# Fast validation (< 5 seconds)
python test_run/quick_validation.py
```

## Expected Results

### Success Indicators
- ✅ All validation tests pass
- ✅ Learning converges to optimal policy
- ✅ Replay produces identical results
- ✅ Confidence scores reflect evidence quality
- ✅ Uncertainty tracking works correctly
- ✅ Error handling prevents invalid inputs

### What Each Script Validates

#### Core System Integrity
- State validation with proper error handling
- Confidence computation with input validation
- Uncertainty tracking with robust state identification
- Learning components with type safety

#### Learning System
- Policy updates are deterministic
- Exploration strategy tracks state visits correctly
- Episode logging captures complete traces
- Reward accumulation works properly

#### Execution System
- Trained policies execute correctly
- Decision engine integrates properly
- Step limits prevent infinite loops
- Results are properly structured

#### Explainability
- Decision explanations are generated
- Confidence reflects evidence quality
- Uncertainty information is preserved
- Claims and disclaimers are appropriate

#### Determinism
- Same inputs produce same outputs
- Replay matches original execution exactly
- No hidden randomness or timestamps
- Complete state capture for auditability

## Troubleshooting

### If Tests Fail

1. **Import Errors**: Ensure you're running from project root
2. **Validation Errors**: Check that fixes were applied correctly
3. **Logic Errors**: Verify exploration strategy and reward accumulation
4. **Type Errors**: Confirm type hints and validation are in place

### Common Issues

- **Path Problems**: Scripts automatically add parent directory to Python path
- **Missing Dependencies**: Only standard library is required
- **Permission Issues**: Ensure write access for log generation

## Integration with Main Project

These scripts complement the existing entry points:
- `quick_run.py` - Basic learning demonstration
- `demo_run.py` - Simple system demo
- `quick_replay.py` - Replay validation

The test_run scripts provide comprehensive validation that the main entry points work correctly and the system meets all design requirements.

## Success Criteria

The project is ready for production when:
- ✅ `run_full_project.py` shows 7/7 tests passed
- ✅ `demo_system.py` completes without errors
- ✅ All confidence scores are evidence-based
- ✅ All uncertainty is explicitly tracked
- ✅ All decisions are explainable
- ✅ All behavior is deterministic

Run these scripts after any code changes to ensure system integrity is maintained.