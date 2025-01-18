#슬롯머신 구현
import numpy as np

class Bandit:
    def __init__(self, arms=10): 
        self.rates=np.random.rand(arms) #한번 설정하면 변하지 않음
    
    def play(self, arm):
        rate=self.rates[arm]
        if rate > np.random.rand():
            return 1
        else:
            return 0

# bandit=Bandit()

# for i in range(3):
#     print(bandit.play(0))
#1
#0
#0

#에이전트 구현
# bandit=Bandit()
# Qs=np.zeros(10) #각 슬롯머신의 가치 추정치
# ns=np.zeros(10) #각 슬롯머신의 플레이 횟수

# for n in range(10):
#     action=np.random.randint(0, 10) #무작위 행동(임의의 슬롯머신 선택)
#     reward=bandit.play(action)

#     ns[action]+=1 #action번째 슬롯머신을 플레이한 횟수 증가
#     Qs[action]+=(reward-Qs[action])/ns[action]
#     print(Qs)

# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 1. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 1. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 1. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 1. 0. 0. 0. 0. 0.]
# [0. 0. 0. 1. 1. 0. 0. 0. 0. 1.]
# [0. 0. 1. 1. 1. 0. 0. 0. 0. 1.]
# [0.  0.5 1.  1.  1.  0.  0.  0.  0.  1. ]
# [0.  0.5 1.  1.  1.  0.  0.  0.  0.  1. ]

class Agent:
    def __init__(self, epsilon, action_size=10):
        self.epsilon=epsilon    #무작위로 행동할 확률(탐색 확률)
        self.Qs=np.zeros(action_size)
        self.ns=np.zeros(action_size)
    
    def update(self, action, reward):   #슬롯머신의 가치 추정
        self.ns[action]+=1
        self.Qs[action]+=(reward-self.Qs[action])/self.ns[action]
    
    def get_action(self):   #행동 선택(ε-탐욕 정책)
        if np.random.rand()<self.epsilon:
            return np.random.randint(0, len(self.Qs))   #무작위 행동 선택
        return np.argmax(self.Qs)   #탐욕 행동 선택

import matplotlib.pyplot as plt

steps=1000
epsilon=0.1

bandit=Bandit()
agent=Agent(epsilon)
total_reward=0
total_rewards=[]    #보상 합
rates=[]    #승률

for step in range(steps):
    action=agent.get_action() #(1) 행동 선택
    reward=bandit.play(action) #(2) 실제로 플레이하고 보상을 받음
    agent.update(action, reward) #(3) 행동과 보상을 통해 학습
    total_reward+=reward

    total_rewards.append(total_reward) #현재까지의 보상 합 저장
    rates.append(total_reward/(step+1)) #현재까지의 승률 저장

print(total_reward)

#그래프 그리기:단계별 보상 총합(그림1-12)
plt.ylabel('Total reward')
plt.xlabel('Steps')
plt.plot(total_rewards)
plt.show()

#그래프 그리기:단계별 승률(그림1-13)
plt.ylabel('Rates')
plt.xlabel('Steps')
plt.plot(rates)
plt.show()

#슬롯머신 1000번 플레이-> 총 200번 반복하여 평균 산출
runs=200
steps=1000
epsilon=0.1
all_rates=np.zeros((runs, steps))

for run in range(runs):
    bandit=Bandit()
    agent=Agent(epsilon)
    total_reward=0
    rates=[]

    for step in range(steps):
        action=agent.get_action()
        reward=bandit.play(action)
        agent.update(action, reward)
        total_reward+=reward
        rates.append(total_reward/(step+1))
    
    all_rates[run]=rates

avg_rates=np.average(all_rates, axis=0)

plt.ylabel('Rates')
plt.xlabel('Steps')
plt.plot(avg_rates)
plt.show()


#비정상 문제-> self.rates가 플레이할 때마다 달라지는 경우
class NonStatBandit:
    def __init__(self, arms=10):
        self.arms=arms
        self.rates=np.random.rand(arms)
    
    def play(self, arm):
        rate=self.rates[arm]
        self.rates+=0.1*np.random.rand(arm) #노이즈 추가
        if rate > np.random.rand():
            return 1
        else:
            return 0

#비정상 문제 풀기
class AlphaAgent:
    def __init__(self, epsilon, alpha, actions=10):
        self.epsilon=epsilon
        self.Qs=np.zeros(actions)
        self.alpha=alpha #고정값 a
    
    def update(self, reward):
        #a로 갱신
        self.Qs[action]+=(reward-self.Qs[action])*self.alpha
    
    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))
        return np.argmax(self.Qs)

