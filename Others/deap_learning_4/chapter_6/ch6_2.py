#SARSA 구현
from collections import defaultdict, deque
from gridworld import GridWorld
import numpy as np
from utils import greedy_probs

class SarsaAgent:
    def __init__(self):
        self.gamma=0.9
        self.alpha=0.8
        self.epsilon=0.1
        self.action_size=4

        random_actions={0:0.25, 1:0.25, 3:0.25, 4:0.25}
        self.pi=defaultdict(lambda: random_actions)
        self.Q=defaultdict(lambda: 0)
        self.memory=deque(maxlen=2) #(1) deque 사용
    
    def get_action(self, state):
        actions_probs=self.pi[state] #(2) pi에서 선택
        actions=list(actions_probs.keys())
        probs=list(actions_probs.values())
        return np.random.choice(actions, p=probs)
    
    def reset(self):
        self.memory.clear()
    
    def update(self, state, action, reward, done):
        self.memory.append((state, action, reward, done))
        if len(self.memory) < 2:
            return 
        
        state, action, reward, done=self.memory[0]
        next_state, next_action, _, _=self.memory[1]
        #(3) 다음 Q 함수
        next_q=0 if done else self.Q[next_state, next_action]

        #(4) TD법으로 self.Q 갱신
        target=reward+self.gamma*next_q
        self.Q[state, action]+=(target-self.Q[state, action])*self.alpha

        #(5) 정책 개선
        self.pi[state]=greedy_probs(self.Q, state, self.epsilon)


#SarsaAgent 클래스 실행(3x4 그리드 월드 문제)
env=GridWorld()
agent=SarsaAgent()

episodes=10000
for episode in range(episodes):
    state=env.reset()
    agent.reset()

    while True:
        action=agent.get_action(state)
        next_state, reward, done=env.step(action)

        agent.update(state, action, reward, done) #(1) 매번 호출

        if done:
            #(2) 목표에 도달했을 때도 호출
            agent.update(next_state, None, None, None)
            break
        state=next_state

env.render_q(agent.Q) #Q 함수 시각화


#오프-정책 SARSA 구현
class SarsaOffPolicyAgent:
    def __init__(self):
        self.gamma=0.9
        self.alpha=9.8
        self.epsilon=0.1
        self.action_size=4

        random_actions={0:0.25, 1:0.25, 2:0.25, 3:0.25}
        self.pi=defaultdict(lambda: random_actions)
        self.b=defaultdict(lambda: random_actions)
        self.Q=defaultdict(lambda: 0)
        self.memory=deque(maxlen=2)

    def get_action(self, state):
        actions_probs=self.b[state]
        actions=list(actions_probs.keys())
        probs=list(actions_probs.values())
        return np.random.choice(actions, p=probs)
    
    def reset(self):
        self.memory.clear()
    
    def update(self, state, action, reward, done):
        self.memory.append(state, action, reward, done)
        if len(self.memory) < 2:
            return 
        
        state, action, reward, done=self.memory[0]
        next_state, next_action, _, _=self.memory[1]

        if done:
            next_q=0
            rho=1
        else:
            next_q=self.Q[next_state, next_action]
            #(2) 가중치 rho 계산
            rho=self.pi[next_state][next_action]/self.b[next_state][next_action]
        
        #(3) rho로 TD 목표 보정
        target=rho*(reward+self.gamma*next_q)
        self.Q[state, action]+=(target-self.Q[state, action])*self.alpha

        #(4) 각각의 정책 개선
        self.pi[state]=greedy_probs(self.Q, state, 0)
        self.b[state]=greedy_probs(self.Q, state, self.epsilon)
        