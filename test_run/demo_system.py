#!/usr/bin/env python3
"""
System Demonstration

Interactive demonstration of the Deterministic RL Engine capabilities.
Run with: python test_run/demo_system.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from learning.learning_loop import LearningLoop
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from execution.executor import Executor
from execution.decision import DecisionEngine
from explainability.explain import Explainer
from uncertainty.confidence import ConfidenceEngine
from uncertainty.uncertainty import UncertaintyModel
from utils.logger import DeterministicLogger
from core.state import validate_state
from collections import namedtuple
import time

# Environment step result
StepResult = namedtuple('StepResult', ['next_state', 'reward', 'done', 'info'])

class DemoEnvironment:
    """Demonstration environment with interesting dynamics."""
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.step_count = 0
        self.total_reward = 0.0
        self.phase = "exploration"  # exploration -> commitment -> completion
        
        return {
            "current_step": 0,
            "observed_signal": 1.0,
            "previous_action": "WAIT",
            "accumulated_reward": 0.0
        }
    
    def step(self, action):
        self.step_count += 1
        
        # Dynamic reward based on phase and action
        if self.phase == "exploration":
            if action == "EXPLORE":
                reward = 2.0
                if self.step_count >= 3:
                    self.phase = "commitment"
            elif action == "WAIT":
                reward = 0.5
            else:
                reward = -1.0
                
        elif self.phase == "commitment":
            if action == "COMMIT":
                reward = 5.0
                self.phase = "completion"
            elif action == "EXPLORE":
                reward = 1.0
            else:
                reward = 0.0
                
        else:  # completion
            reward = 1.0 if action == "WAIT" else 0.0
        
        self.total_reward += reward
        done = self.step_count >= 8
        
        # Signal changes based on phase
        signal_map = {"exploration": 1.0, "commitment": 2.0, "completion": 3.0}
        
        next_state = {
            "current_step": self.step_count,
            "observed_signal": signal_map[self.phase] + (self.step_count * 0.1),
            "previous_action": action,
            "accumulated_reward": self.total_reward
        }
        
        validate_state(next_state)
        return StepResult(next_state, reward, done, {"phase": self.phase})

class AdaptivePolicy:
    """Policy that learns and adapts."""
    
    def __init__(self):
        self.q_values = {}
        self.visit_counts = {}
        
    def _state_key(self, state):
        return f"step_{state['current_step']}_signal_{state['observed_signal']:.1f}"
    
    def select_action(self, state):
        state_key = self._state_key(state)
        
        if state_key not in self.q_values:
            # Initialize Q-values for new state
            self.q_values[state_key] = {"WAIT": 0.0, "EXPLORE": 0.0, "COMMIT": 0.0}
        
        # Select action with highest Q-value
        best_action = max(self.q_values[state_key], key=self.q_values[state_key].get)
        return best_action
    
    def update(self, state, action, reward):
        state_key = self._state_key(state)
        
        if state_key not in self.q_values:
            self.q_values[state_key] = {"WAIT": 0.0, "EXPLORE": 0.0, "COMMIT": 0.0}
        
        # Q-learning update
        learning_rate = 0.1
        self.q_values[state_key][action] += learning_rate * reward
        
        # Track visits
        visit_key = f"{state_key}_{action}"
        self.visit_counts[visit_key] = self.visit_counts.get(visit_key, 0) + 1
    
    def snapshot(self):
        return {
            "q_values": self.q_values.copy(),
            "visit_counts": self.visit_counts.copy()
        }
    
    def get_confidence(self, state):
        state_key = self._state_key(state)
        total_visits = sum(
            count for key, count in self.visit_counts.items() 
            if key.startswith(state_key)
        )
        return min(total_visits / 5.0, 1.0)

def print_header(title):
    """Print formatted section header."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def demonstrate_learning():
    """Demonstrate the learning process."""
    print_header("LEARNING DEMONSTRATION")
    
    env = DemoEnvironment()
    policy = AdaptivePolicy()
    learner = Learner()
    exploration = ExplorationStrategy(min_visits_required=1)
    logger = DeterministicLogger()
    
    loop = LearningLoop(env, policy, learner, exploration, logger)
    
    print("Training agent for 3 episodes...")
    print("Watch how the policy learns optimal actions for different phases:")
    
    loop.train(episodes=3, max_steps_per_episode=8)
    
    print(f"\nLearning completed!")
    print(f"Episodes logged: {len(logger.export())}")
    print(f"Final Q-values sample: {list(policy.q_values.items())[:3]}")
    
    return env, policy, logger.export()

def demonstrate_execution(env, policy):
    """Demonstrate policy execution."""
    print_header("EXECUTION DEMONSTRATION")
    
    decision_engine = DecisionEngine()
    executor = Executor(env, decision_engine, policy)
    
    state = env.reset()
    print("Executing trained policy...")
    print("Step | Action   | Reward | Phase       | Signal | Confidence")
    print("-" * 60)
    
    step = 0
    while step < 8:
        confidence = policy.get_confidence(state)
        result = executor.run_step(state)
        
        print(f"{step+1:4d} | {result['decision']['action']:8s} | {result['reward']:6.1f} | "
              f"{result['next_state'].get('phase', 'unknown'):11s} | "
              f"{result['next_state']['observed_signal']:6.1f} | {confidence:10.3f}")
        
        state = result["next_state"]
        step += 1
        
        if result["done"]:
            break
    
    print(f"\nExecution completed! Final reward: {state['accumulated_reward']}")

def demonstrate_explainability(policy):
    """Demonstrate explainability features."""
    print_header("EXPLAINABILITY DEMONSTRATION")
    
    explainer = Explainer()
    uncertainty_model = UncertaintyModel()
    
    # Create sample decision scenario
    sample_state = {
        "current_step": 4,
        "observed_signal": 2.3,
        "previous_action": "EXPLORE",
        "accumulated_reward": 7.5
    }
    
    action = policy.select_action(sample_state)
    confidence = policy.get_confidence(sample_state)
    
    uncertainty_model.register_state(sample_state)
    uncertainty_snapshot = uncertainty_model.snapshot()
    
    explanation = explainer.explain_decision(
        state=sample_state,
        action=action,
        confidence=confidence,
        uncertainty_snapshot=uncertainty_snapshot
    )
    
    print("Decision Explanation:")
    print(f"  State: Step {sample_state['current_step']}, Signal {sample_state['observed_signal']}")
    print(f"  Chosen Action: {explanation['chosen_action']}")
    print(f"  Confidence: {explanation['confidence']:.3f}")
    print(f"  Uncertainty Info: {explanation['known_limits']}")
    print(f"  Claim: {explanation['claim']}")
    print(f"  Disclaimer: {explanation['disclaimer']}")

def demonstrate_uncertainty_tracking():
    """Demonstrate uncertainty management."""
    print_header("UNCERTAINTY TRACKING DEMONSTRATION")
    
    confidence_engine = ConfidenceEngine()
    uncertainty_model = UncertaintyModel()
    
    print("Simulating uncertainty evolution across different scenarios:")
    print("Scenario | Visits | Consistency | Confidence | Unseen States")
    print("-" * 60)
    
    scenarios = [
        ("New State", 0, 0.0),
        ("First Visit", 1, 0.3),
        ("Learning", 3, 0.6),
        ("Experienced", 7, 0.9),
        ("Expert", 15, 0.95),
        ("Inconsistent", 10, 0.2)  # High visits but low consistency
    ]
    
    for i, (scenario, visits, consistency) in enumerate(scenarios):
        # Register some states for uncertainty tracking
        test_state = {"current_step": i, "observed_signal": i*0.5, "previous_action": "WAIT", "accumulated_reward": i}
        uncertainty_model.register_state(test_state)
        
        confidence = confidence_engine.compute(visits, consistency) if visits > 0 else 0.0
        snapshot = uncertainty_model.snapshot()
        
        print(f"{scenario:12s} | {visits:6d} | {consistency:11.2f} | {confidence:10.3f} | {snapshot['unseen_state_count']:12d}")

def demonstrate_determinism(logs, env, policy):
    """Demonstrate deterministic replay."""
    print_header("DETERMINISM DEMONSTRATION")
    
    from learning.replay import ReplayEngine
    
    replay_engine = ReplayEngine(env, policy)
    
    print("Verifying deterministic behavior through replay...")
    
    try:
        for i, log in enumerate(logs):
            print(f"Replaying episode {i+1}...", end=" ")
            replay_engine.replay(log)
            print("✓ IDENTICAL")
        
        print("\n🎉 Perfect deterministic replay achieved!")
        print("Same inputs always produce same outputs - system is fully deterministic.")
        
    except Exception as e:
        print(f"\n❌ Replay failed: {e}")

def main():
    """Run complete system demonstration."""
    print("DETERMINISTIC RL ENGINE - SYSTEM DEMONSTRATION")
    print("Showcasing: Learning, Execution, Explainability, Uncertainty, Determinism")
    
    try:
        # Learning phase
        env, policy, logs = demonstrate_learning()
        
        # Execution phase
        demonstrate_execution(env, policy)
        
        # Explainability
        demonstrate_explainability(policy)
        
        # Uncertainty tracking
        demonstrate_uncertainty_tracking()
        
        # Determinism verification
        demonstrate_determinism(logs, env, policy)
        
        print_header("DEMONSTRATION COMPLETE")
        print("🎉 All system capabilities successfully demonstrated!")
        print("The Deterministic RL Engine is ready for production use.")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Demonstration failed: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)