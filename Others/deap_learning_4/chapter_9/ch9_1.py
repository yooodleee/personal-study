#정책 경사법 구현
import numpy as np
import gym
from dezero import Model
from dezero import optimizers
import dezero.functions as F
import dezero.layers as L

class Policy(Model):
    def __init__(self, action_size):
        super().__init__()
        self.l1=L.Linear(128) #첫 번째 계층
        self.l2=L.Linear(action_size) #두 번째 계층

    def forward(self, x):
        x=F.relu(self.l1(x)) #첫 번째 계층에서는 ReLU 함수 사용
        x=F.softmax(self.l2(x)) #두 번째 계층에서는 소프트맥스 함수 사용
        return x

class Agent:
    def __init__(self):
        self.gamma=0.98
        self.lr=0.0002
        self.action_size=2

        self.memory=[]
        self.pi=Policy(self.action_size)
        self.optimizer=optimizers.Adam(self.lr)
        self.optimizer.setup(self.pi)

    def get_action(self, state):
        state=state[np.newaxis, :] #배치 처리용 축 추가
        probs=self.pi(state) #순전파 수행
        probs=probs[0]
        action=np.random.choice(len(probs), p=probs.data) #행동 선택
        return action, probs[action] #선택된 행동과 확률 반환
    
    def add(self, reward, prob):
        data=(reward, prob)
        self.memory.append(data)

    def update(self):
        self.pi.cleargrads()

        G, loss=0, 0
        for reward, prob in reversed(self.memory): #수익 G 계산
            G=reward+self.gamma*G
        # for reward, prob in self.memory: #손실 함수 계산(개선 전)
            loss+=-F.log(prob)*G
        
        loss.backward()
        self.optimizer.update()
        self.memory=[] #메모리 초기화

# env=gym.make('CartPole-v0', render_made='rgb_array')
# state=env.reset()
# agent=Agent()

# action, prob=agent.get_action(state)
# print('행동:', action)
# print('확률:', prob)

# G=100.0 #더미 가중치
# J=G*F.log(prob)
# prob('J:', J)

# #기울기 구하기
# J.backward()

episodes=3000
env=gym.make('CartPole-v0', render_made='rgb_array')
agent=Agent()
reward_history=[]

for episode in range(episodes):
    state=env.reset()[0]
    done=False
    total_reward=0

    while not done:
        action, prob=agent.get_action(state) #행동 선택
        #행동 수행
        #(1) 보상과 행동의 확률을 에이전트에 추가
        next_state, reward, terminated, truncated, info=env.step(action)
        done=terminated|truncated #상태 전이
        total_reward+=reward #보상 총합 계산

    agent.update() #(2) 정책 갱신
    reward_history.append(total_reward)
