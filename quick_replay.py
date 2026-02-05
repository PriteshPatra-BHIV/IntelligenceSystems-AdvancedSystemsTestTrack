from learning.replay import ReplayEngine
from learning.learning_loop import LearningLoop
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from utils.logger import DeterministicLogger
from collections import namedtuple

# Environment step result for better type safety
StepResult = namedtuple('StepResult', ['next_state', 'reward', 'done', 'info'])

# -------------------------------
# Minimal deterministic environment
# -------------------------------
class SimpleEnv:
    def __init__(self):
        self.step_count = 0
        self.total_reward = 0.0

    def reset(self):
        self.step_count = 0
        self.total_reward = 0.0
        return {
            "current_step": 0,
            "observed_signal": 1.0,
            "previous_action": "WAIT",
            "accumulated_reward": 0.0
        }

    def step(self, action):
        self.step_count += 1
        reward = 1.0 if action == "WAIT" else 0.0
        self.total_reward += reward  # Properly accumulate rewards
        done = self.step_count >= 3

        next_state = {
            "current_step": self.step_count,
            "observed_signal": 1.0,
            "previous_action": action,
            "accumulated_reward": self.total_reward  # Use accumulated total
        }

        return StepResult(next_state, reward, done, {})

# -------------------------------
# Minimal deterministic policy
# -------------------------------
class SimplePolicy:
    def __init__(self):
        pass  # Remove unused memory attribute

    def select_action(self, state):
        return "WAIT"

    def update(self, state, action, reward):
        pass

    def snapshot(self):
        return {}  # Return empty dict directly

    def get_confidence(self, state):
        return 0.5

# -------------------------------
# Step 1: Run learning to generate logs
# -------------------------------
env = SimpleEnv()
policy = SimplePolicy()
learner = Learner()
exploration = ExplorationStrategy()
logger = DeterministicLogger()

loop = LearningLoop(env, policy, learner, exploration, logger)
loop.train(episodes=1, max_steps_per_episode=3)

print("Learning completed. Replay log generated.")

# -------------------------------
# Step 2: Replay learning deterministically
# -------------------------------
replay_engine = ReplayEngine(env, policy)

replay_engine.replay({
    "episode_trace": logger.export()[0]["episode_trace"]
})

print("Replay executed without divergence. Determinism verified.")