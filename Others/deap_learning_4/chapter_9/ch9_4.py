#행위자-비평자 구현
import numpy as np
import gym
from dezero import Model
from dezero import optimizers
import dezero.functions as F
import dezero.layers as L

class PolicyNet(Model): #정책 신경망
    def __init__(self, action_size=2):
        super().__init__()
        self.l1=L.Linear(128)
        self.l2=L.Linear(action_size)
    
    def forward(self, x):
        x=F.relu(self.l1(x))
        x=self.l2(x)
        x=F.softmax(x) #확률 출력
        return x

class ValueNet(Model): #가치 함수 신경망
    def __init__(self):
        super().__init__()
        self.l1=L.Linear(128)
        self.l2=L.Linear(1)
    
    def forward(self, x):
        x=F.relu(self.l1(x))
        x=self.l2(x)
        return x

class Agent:
    def __init__(self):
        self.gamma=0.98
        self.lr_pi=0.0002
        self.lr_v=0.0005
        self.action_size=2

        self.pi=PolicyNet()
        self.v=ValueNet()
        self.optimizer_pi=optimizers.Adam(self.lr_pi).setup(self.pi)
        self.optimizer_v=optimizers.Adam(self.lr_v).setup(self.v)
    
    def get_action(self, state):
        state=state[np.newaxis, :] #(1) 배치 처리용 축 추가
        probs=self.pi(state)
        probs=probs[0]
        action=np.random.choice(len(probs), p=probs.data)
        return action, probs[action] #선택된 행동과 행동의 확률 반환
    
    def update(self, state, action_prob, reward, next_state, done):
        #배치 처리용 축 추가
        state=state[np.newaxis, :]
        next_state=next_state[np.newaxis, :]

        #(2) 가치 함수(self.v)의 손실 계산
        target=reward+self.gamma*self.v(next_state)*(1-done) #TD 목표
        target.unchain()
        v=self.v(state) #현재 상태의 가치 함수
        loss_v=F.mean_squared_error(v, target) #두 값의 평균 제곱 오차

        #(3) 정책(self.pi)의 손실 계산
        delta=target-v
        delta.unchain()
        loss_pi=-F.log(action_prob)*delta

        #신경망 학습
        self.v.cleargrads()
        self.pi.cleargrads()
        loss_v.backward()
        loss_pi.backward()
        self.optimizer_v.update()
        self.optimizer_pi.update()