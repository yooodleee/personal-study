#몬테카를로법 구현
from gridworld import GridWorld

env=GridWorld()
action=0
next_state, reward, done=env.step(action) #행동 수행

print('next_state: ', next_state)
#next_state:  (1, 0)
print('reward: ', reward)
#reward:  0
print('done: ', done)
#done:  False

env=GridWorld()
state=env.reset() #상태 초기화

from collections import defaultdict
import numpy as np

class RandomAgent:
    def __init__(self):
        self.gamma=0.9
        self.action_size=4

        random_actions={0:0.25, 1:0.25, 2:0.25, 3:0.25}
        self.pi=defaultdict(lambda:random_actions)
        self.V=defaultdict(lambda:0)
        self.cnts=defaultdict(lambda:0)
        self.memory=[]

    def get_action(self, state):
        action_probs=self.pi[state]
        actions=list(action_probs.keys())
        probs=list(action_probs.values())
        return np.random.choice(actions, p=probs)
    
    def add(self, state, action, reward):
        data=(state, action, reward)
        self.memory.append(data)
    
    def reset(self):
        self.memory.clear()
    
    def eval(self):
        G=0
        for data in reversed(self.memory):
            state, action, reward=data
            G=self.gamma*G+reward
            self.cnts[state]+=1
            self.V[state]+=(G-self.V[state])/self.cnts[state]

#몬테카를로법 실행
env=GridWorld()
agent=RandomAgent()

episodes=1000
for episode in range(episodes): #에피소드 1000번 수행
    state=env.reset()
    agent.reset()

    while True:
        action=agent.get_action(state) #행동 선택
        next_state, reward, done=env.step(action) #행동 수행

        agent.add(state, action, reward) #(상태, 행동, 보상) 저장
        if done: #목표 도달 시
            agent.eval() #몬테카를로법으로 가치 함수 갱신
            break #다음 에피소드 시작

        state=next_state

#모든 에피소드 종료

#가치 함수 시각화
env.render_v(agent.V)