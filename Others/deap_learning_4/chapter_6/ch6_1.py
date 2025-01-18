#TD법 구현(TdAgent 클래스)
from collections import defaultdict
from gridworld import GridWorld
from td_eval import TdAgent
import numpy as np

class Agent:
    def __init__(self):
        self.gamma=0.9
        self.alpha=0.01
        self.action_size=4

        random_actions={0:0.25, 1:0.25, 2:0.25, 3:0.25}
        self.pi=defaultdict(lambda: random_actions)
        self.V=defaultdict(lambda: 0)
    
    def get_action(self, state):
        action_probs=self.pi[state]
        actions=list(action_probs.keys())
        probs=list(action_probs.values())
        return np.random.choice(actions, p=probs)
    
    def eval(self, state, reward, next_state, done):
        next_V=0 if done else self.V[next_state] #목표 지점의 가치 함수는 0
        target=reward+self.gamma*next_V

        self.V[state]+=(target-self.V[state])*self.alpha


#에이전트를 실제로 행동하도록 시켜 정책을 평가(총 1000번의 에피소드를 실행)
env=GridWorld()
agent=TdAgent()

episodes=1000
for episode in range(episodes):
    state=env.reset()

    while True:
        action=agent.get_action(state)
        next_state, reward, done=env.step(action)

        agent.eval(state, reward, next_state, done) #매번 호출
        if done:
            break
        state=next_state

env.render_v(agent.V)