#!/usr/bin/env python3
"""
Full Project Test Runner

Executes all components of the Deterministic RL Engine:
1. Core validation
2. Learning phase
3. Execution phase
4. Replay verification
5. Explainability demo
6. Uncertainty tracking
7. Stress testing

Run with: python test_run/run_full_project.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from learning.learning_loop import LearningLoop
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from learning.replay import ReplayEngine
from execution.executor import Executor
from execution.decision import DecisionEngine
from explainability.explain import Explainer
from uncertainty.confidence import ConfidenceEngine
from uncertainty.uncertainty import UncertaintyModel
from utils.logger import DeterministicLogger
from core.state import validate_state
from collections import namedtuple
import json

# Environment step result
StepResult = namedtuple('StepResult', ['next_state', 'reward', 'done', 'info'])

class ComprehensiveEnvironment:
    """Enhanced environment for full system testing."""
    
    def __init__(self):
        self.step_count = 0
        self.total_reward = 0.0
        self.episode_count = 0
        
    def reset(self):
        self.step_count = 0
        self.total_reward = 0.0
        self.episode_count += 1
        
        initial_state = {
            "current_step": 0,
            "observed_signal": 1.0 + (self.episode_count * 0.1),  # Slight variation per episode
            "previous_action": "WAIT",
            "accumulated_reward": 0.0
        }
        
        # Validate state using core validation
        validate_state(initial_state)
        return initial_state
    
    def step(self, action):
        self.step_count += 1
        
        # Reward logic based on action
        if action == "WAIT":
            reward = 1.0
        elif action == "EXPLORE":
            reward = 0.5
        elif action == "COMMIT":
            reward = 2.0 if self.step_count > 2 else -1.0
        else:
            reward = -5.0  # Invalid action penalty
            
        self.total_reward += reward
        done = self.step_count >= 5
        
        next_state = {
            "current_step": self.step_count,
            "observed_signal": 1.0 + (self.step_count * 0.2),
            "previous_action": action,
            "accumulated_reward": self.total_reward
        }
        
        # Validate state
        validate_state(next_state)
        return StepResult(next_state, reward, done, {"step_info": f"Step {self.step_count}"})

class IntelligentPolicy:
    """Policy that demonstrates learning and decision making."""
    
    def __init__(self):
        self.action_values = {"WAIT": 0.0, "EXPLORE": 0.0, "COMMIT": 0.0}
        self.state_action_counts = {}
        
    def select_action(self, state):
        # Simple policy: choose action with highest value
        best_action = max(self.action_values, key=self.action_values.get)
        return best_action
    
    def update(self, state, action, reward):
        # Update action values based on reward
        learning_rate = 0.1
        self.action_values[action] += learning_rate * reward
        
        # Track state-action counts for confidence
        key = f"{state['current_step']}_{action}"
        self.state_action_counts[key] = self.state_action_counts.get(key, 0) + 1
    
    def snapshot(self):
        return {
            "action_values": self.action_values.copy(),
            "state_action_counts": self.state_action_counts.copy()
        }
    
    def get_confidence(self, state):
        # Confidence based on experience
        total_experience = sum(self.state_action_counts.values())
        return min(total_experience / 10.0, 1.0)

def run_core_validation():
    """Test core system components."""
    print("=" * 50)
    print("1. CORE VALIDATION")
    print("=" * 50)
    
    # Test state validation
    try:
        valid_state = {
            "current_step": 1,
            "observed_signal": 2.5,
            "previous_action": "WAIT",
            "accumulated_reward": 1.5
        }
        validate_state(valid_state)
        print("✓ State validation: PASSED")
    except Exception as e:
        print(f"✗ State validation: FAILED - {e}")
        return False
    
    # Test confidence engine
    try:
        confidence_engine = ConfidenceEngine()
        confidence = confidence_engine.compute(state_visits=5, reward_consistency=0.8)
        print(f"✓ Confidence computation: PASSED (confidence={confidence})")
    except Exception as e:
        print(f"✗ Confidence computation: FAILED - {e}")
        return False
    
    # Test uncertainty model
    try:
        uncertainty_model = UncertaintyModel()
        uncertainty_model.register_state(valid_state)
        snapshot = uncertainty_model.snapshot()
        print(f"✓ Uncertainty tracking: PASSED (unseen_states={snapshot['unseen_state_count']})")
    except Exception as e:
        print(f"✗ Uncertainty tracking: FAILED - {e}")
        return False
    
    print("Core validation: ALL TESTS PASSED\n")
    return True

def run_learning_phase():
    """Execute learning phase with full logging."""
    print("=" * 50)
    print("2. LEARNING PHASE")
    print("=" * 50)
    
    try:
        env = ComprehensiveEnvironment()
        policy = IntelligentPolicy()
        learner = Learner()
        exploration = ExplorationStrategy(min_visits_required=2)
        logger = DeterministicLogger()
        
        loop = LearningLoop(env, policy, learner, exploration, logger)
        
        print("Starting learning...")
        loop.train(episodes=3, max_steps_per_episode=5)
        
        logs = logger.export()
        print(f"✓ Learning completed: {len(logs)} episodes logged")
        print(f"✓ Policy learned values: {policy.action_values}")
        
        return logs, env, policy
        
    except Exception as e:
        print(f"✗ Learning phase: FAILED - {e}")
        return None, None, None

def run_execution_phase(env, policy):
    """Execute trained policy."""
    print("=" * 50)
    print("3. EXECUTION PHASE")
    print("=" * 50)
    
    try:
        decision_engine = DecisionEngine()
        executor = Executor(env, decision_engine, policy)
        
        state = env.reset()
        total_reward = 0
        steps = 0
        
        print("Executing trained policy...")
        while steps < 5:
            result = executor.run_step(state)
            state = result["next_state"]
            total_reward += result["reward"]
            steps += 1
            
            print(f"  Step {steps}: Action={result['decision']['action']}, Reward={result['reward']}")
            
            if result["done"]:
                break
        
        print(f"✓ Execution completed: {steps} steps, total reward={total_reward}")
        return True
        
    except Exception as e:
        print(f"✗ Execution phase: FAILED - {e}")
        return False

def run_replay_verification(logs, env, policy):
    """Verify deterministic replay."""
    print("=" * 50)
    print("4. REPLAY VERIFICATION")
    print("=" * 50)
    
    try:
        replay_engine = ReplayEngine(env, policy)
        
        for i, log in enumerate(logs):
            print(f"Replaying episode {i+1}...")
            replay_engine.replay(log)
        
        print("✓ Replay verification: ALL EPISODES REPLAYED SUCCESSFULLY")
        return True
        
    except Exception as e:
        print(f"✗ Replay verification: FAILED - {e}")
        return False

def run_explainability_demo():
    """Demonstrate explainability features."""
    print("=" * 50)
    print("5. EXPLAINABILITY DEMO")
    print("=" * 50)
    
    try:
        explainer = Explainer()
        uncertainty_model = UncertaintyModel()
        
        sample_state = {
            "current_step": 3,
            "observed_signal": 1.5,
            "previous_action": "EXPLORE",
            "accumulated_reward": 2.5
        }
        
        uncertainty_model.register_state(sample_state)
        uncertainty_snapshot = uncertainty_model.snapshot()
        
        explanation = explainer.explain_decision(
            state=sample_state,
            action="COMMIT",
            confidence=0.75,
            uncertainty_snapshot=uncertainty_snapshot
        )
        
        print("✓ Decision explanation generated:")
        print(f"  Action: {explanation['chosen_action']}")
        print(f"  Confidence: {explanation['confidence']}")
        print(f"  Claim: {explanation['claim']}")
        print(f"  Disclaimer: {explanation['disclaimer']}")
        
        return True
        
    except Exception as e:
        print(f"✗ Explainability demo: FAILED - {e}")
        return False

def run_uncertainty_tracking():
    """Demonstrate uncertainty propagation."""
    print("=" * 50)
    print("6. UNCERTAINTY TRACKING")
    print("=" * 50)
    
    try:
        uncertainty_model = UncertaintyModel()
        confidence_engine = ConfidenceEngine()
        
        # Simulate uncertainty evolution
        states = [
            {"current_step": i, "observed_signal": i*0.5, "previous_action": "WAIT", "accumulated_reward": i}
            for i in range(5)
        ]
        
        print("Tracking uncertainty across states...")
        for i, state in enumerate(states):
            uncertainty_model.register_state(state)
            
            # Simulate varying confidence based on experience
            visits = i + 1
            consistency = max(0.5, 1.0 - i*0.1)  # Decreasing consistency
            confidence = confidence_engine.compute(visits, consistency)
            
            snapshot = uncertainty_model.snapshot()
            print(f"  State {i}: Confidence={confidence:.3f}, Unseen={snapshot['unseen_state_count']}")
        
        print("✓ Uncertainty tracking: COMPLETED")
        return True
        
    except Exception as e:
        print(f"✗ Uncertainty tracking: FAILED - {e}")
        return False

def run_stress_tests():
    """Run basic stress tests."""
    print("=" * 50)
    print("7. STRESS TESTING")
    print("=" * 50)
    
    try:
        # Test with invalid inputs
        confidence_engine = ConfidenceEngine()
        
        # Test negative visits
        try:
            confidence_engine.compute(-1, 0.5)
            print("✗ Negative visits test: FAILED (should have raised error)")
            return False
        except ValueError:
            print("✓ Negative visits test: PASSED")
        
        # Test invalid consistency
        try:
            confidence_engine.compute(5, 1.5)
            print("✗ Invalid consistency test: FAILED (should have raised error)")
            return False
        except ValueError:
            print("✓ Invalid consistency test: PASSED")
        
        # Test state validation with missing fields
        try:
            validate_state({"current_step": 1})  # Missing required fields
            print("✗ Missing fields test: FAILED (should have raised error)")
            return False
        except ValueError:
            print("✓ Missing fields test: PASSED")
        
        print("✓ Stress testing: ALL TESTS PASSED")
        return True
        
    except Exception as e:
        print(f"✗ Stress testing: FAILED - {e}")
        return False

def main():
    """Run complete project test suite."""
    print("DETERMINISTIC RL ENGINE - FULL PROJECT TEST")
    print("=" * 60)
    
    results = []
    
    # Run all test phases
    results.append(("Core Validation", run_core_validation()))
    
    logs, env, policy = run_learning_phase()
    results.append(("Learning Phase", logs is not None))
    
    if env and policy:
        results.append(("Execution Phase", run_execution_phase(env, policy)))
        results.append(("Replay Verification", run_replay_verification(logs, env, policy)))
    else:
        results.append(("Execution Phase", False))
        results.append(("Replay Verification", False))
    
    results.append(("Explainability Demo", run_explainability_demo()))
    results.append(("Uncertainty Tracking", run_uncertainty_tracking()))
    results.append(("Stress Testing", run_stress_tests()))
    
    # Summary
    print("=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "PASSED" if success else "FAILED"
        symbol = "✓" if success else "✗"
        print(f"{symbol} {test_name}: {status}")
        if success:
            passed += 1
    
    print("=" * 60)
    print(f"OVERALL: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL SYSTEMS OPERATIONAL - PROJECT READY FOR DEPLOYMENT")
        return 0
    else:
        print("⚠️  SOME TESTS FAILED - REVIEW REQUIRED")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)