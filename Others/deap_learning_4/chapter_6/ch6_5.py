#분포 모델 구현(무작위로 행동하는 에이전트)
from collections import defaultdict
from gridworld import GridWorld
from utils import greedy_probs
import numpy as np

class QLearningAgent:
    def __init__(self):
        self.gamma=0.9
        self.alpha=0.8
        self.epsilon=0.1
        self.action_size=4
        self.Q=defaultdict(lambda: 0)

    def get_action(self, state):
        if np.random.rand() < self.epsilon: #(1) epsilon의 확률로 무작위 행동
            return np.random.choice(self.action_size)
        else: #(2) (1-epsilon)의 확률로 탐욕 행동
            qs=[self.Q[state, a] for a in range(self.action_size)]
            return np.argmax(qs)
    
    def update(self, state, action, reward, next_state, done):
        if done:
            next_q_max=0
        else:
            next_qs=[self.Q[next_state, a] for a in range(self.action_size)]
            next_q_max=max(next_qs)
        
        target=reward+self.gamma*next_q_max
        self.Q[state, action]+=(target-self.Q[state, action])*self.alpha

        #pi는 탐욕화, b는 ε-탐욕화
        self.pi[state]=greedy_probs(self.Q, state, epsilon=0)
        self.b[state]=greedy_probs(self.Q, state, self.epsilon)