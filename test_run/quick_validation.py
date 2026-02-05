#!/usr/bin/env python3
"""
Quick System Validation

Fast validation of core system components.
Run with: python test_run/quick_validation.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.state import validate_state
from core.contracts import STATE_FIELDS, ACTION_SET, REWARD_RANGE
from uncertainty.confidence import ConfidenceEngine
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from utils.logger import DeterministicLogger

def test_contracts():
    """Validate system contracts."""
    print("Testing system contracts...")
    
    # Check contracts are properly defined
    assert len(STATE_FIELDS) == 4, "STATE_FIELDS should have 4 fields"
    assert len(ACTION_SET) == 3, "ACTION_SET should have 3 actions"
    assert REWARD_RANGE == (-10.0, 10.0), "REWARD_RANGE should be (-10.0, 10.0)"
    
    print("✓ System contracts validated")

def test_state_validation():
    """Test state validation logic."""
    print("Testing state validation...")
    
    # Valid state
    valid_state = {
        "current_step": 1,
        "observed_signal": 2.5,
        "previous_action": "WAIT",
        "accumulated_reward": 1.5
    }
    validate_state(valid_state)  # Should not raise
    
    # Invalid state - missing field
    try:
        invalid_state = {"current_step": 1}
        validate_state(invalid_state)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected
    
    print("✓ State validation working correctly")

def test_confidence_engine():
    """Test confidence computation."""
    print("Testing confidence engine...")
    
    engine = ConfidenceEngine()
    
    # Test normal case
    confidence = engine.compute(5, 0.8)
    assert 0.0 <= confidence <= 1.0, "Confidence should be in [0,1]"
    
    # Test edge cases
    assert engine.compute(0, 0.5) == 0.0, "Zero visits should give zero confidence"
    
    # Test validation
    try:
        engine.compute(-1, 0.5)
        assert False, "Should reject negative visits"
    except ValueError:
        pass
    
    print("✓ Confidence engine working correctly")

def test_learning_components():
    """Test learning system components."""
    print("Testing learning components...")
    
    # Test learner
    learner = Learner()
    
    # Test exploration strategy
    exploration = ExplorationStrategy()
    test_state = {"current_step": 1, "observed_signal": 1.0, "previous_action": "WAIT", "accumulated_reward": 0.0}
    decision = exploration.decide(test_state, step=1)
    assert decision in ["EXPLORE", "EXPLOIT"], f"Invalid decision: {decision}"
    
    # Test logger
    logger = DeterministicLogger()
    logger.log({"test": "data"})
    logs = logger.export()
    assert len(logs) == 1, "Logger should have 1 record"
    assert logs[0]["test"] == "data", "Logger should preserve data"
    
    print("✓ Learning components working correctly")

def main():
    """Run quick validation."""
    print("DETERMINISTIC RL ENGINE - QUICK VALIDATION")
    print("=" * 50)
    
    tests = [
        ("System Contracts", test_contracts),
        ("State Validation", test_state_validation),
        ("Confidence Engine", test_confidence_engine),
        ("Learning Components", test_learning_components)
    ]
    
    passed = 0
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✓ {test_name}: PASSED")
            passed += 1
        except Exception as e:
            print(f"✗ {test_name}: FAILED - {e}")
    
    print("=" * 50)
    print(f"Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 QUICK VALIDATION SUCCESSFUL")
        return 0
    else:
        print("⚠️  VALIDATION FAILED")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)