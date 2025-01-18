#몬테카를로법으로 정책 제어 구현
from collections import defaultdict
from gridworld import GridWorld
import numpy as np

def greedy_probs(Q, state, epsilon=0, action_size=4):
    qs=[Q[state, action] for action in range(action_size)]
    max_action=np.argmax(qs)

    base_prob=epsilon/action_size
    action_probs={action:base_prob for action in range(action_size)}
    #이 시점에서 action_probs={0:ε/4, 1:ε/4, 2:ε/4, 3:ε/4}
    action_probs[max_action]+=(1-epsilon)
    return action_probs

class McAgent:
    def __init__(self):
        self.gamma=0.9
        self.epsilon=0.1 #(첫 번째 개선) ε-탐욕 정책의  ε
        self.alpha=0.1 #(두 번째 개선) Q 함수 갱신 시의 고정값 α
        self.action_size=4

        random_actions={0:0.25, 1:0.25, 3:0.25, 4:0.25}
        self.pi=defaultdict(lambda: random_actions) 
        self.Q=defaultdict(lambda:0)
        # self.cnts=defaultdict(lambda:0)
        self.memory=[]

    def get_action(self, state):
        actions_porbs=self.pi[state]
        actions=list(actions_porbs.keys())
        probs=list(actions_porbs.values())
        return np.random.choice(actions, p=probs)
    
    def add(self, state, action, reward):
        data=(state, action, reward)
        self.memory.append(data)
    
    def reset(self):
        self.memory.clear()

    def update(self):
        G=0
        for data in reversed(self.memory):
            state, action, reward=data
            G=self.gamma*G+reward
            key=(state, action)
            # self.cnts[key]+=1
            # self.Q[key]+=(G-self.Q[key])/self.cnts[key] 
            self.Q[key]+=(G-self.Q[key])*self.alpha #(1)
            self.pi[state]=greedy_probs(self.Q, state, self.epsilon) #(2)

            #state의 정책 탐욕화
            self.pi[state]=greedy_probs(self.Q, state)

env=GridWorld()
agent=McAgent()

episodes=10000
for episode in range(episodes):
    state=env.reset()
    agent.reset()

    while True:
        action=agent.get_action(state)
        next_state, reward, done=env.step(action)
        
        agent.add(state, action, reward)
        if done:
            agent.update()
            break

        state=next_state

env.render_q(agent.Q)