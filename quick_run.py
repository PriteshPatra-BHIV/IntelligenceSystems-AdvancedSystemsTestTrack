from learning.learning_loop import LearningLoop
from learning.learner import Learner
from learning.exploration import ExplorationStrategy
from utils.logger import DeterministicLogger

# ---- Minimal deterministic environment ----
class SimpleEnv:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return {
            "current_step": 0,
            "observed_signal": 1.0,
            "previous_action": "WAIT",
            "accumulated_reward": 0.0
        }

    def step(self, action):
        self.step_count += 1
        reward = 1.0 if action == "WAIT" else 0.0
        done = self.step_count >= 3

        next_state = {
            "current_step": self.step_count,
            "observed_signal": 1.0,
            "previous_action": action,
            "accumulated_reward": reward
        }

        return next_state, reward, done, {}

# ---- Minimal deterministic policy ----
class SimplePolicy:
    def __init__(self):
        self.memory = {}

    def select_action(self, state):
        return "WAIT"

    def update(self, state, action, reward):
        pass

    def snapshot(self):
        return dict(self.memory)

    def get_confidence(self, state):
        return 0.5

# ---- Run learning ----
env = SimpleEnv()
policy = SimplePolicy()
learner = Learner()
exploration = ExplorationStrategy()
logger = DeterministicLogger()

loop = LearningLoop(env, policy, learner, exploration, logger)
loop.train(episodes=2, max_steps_per_episode=3)

print("Learning run completed deterministically")
print("Replay logs:", logger.export())
