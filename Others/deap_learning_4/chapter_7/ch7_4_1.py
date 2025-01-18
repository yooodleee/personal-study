#3x4 그리드 월드를 전처리(원-핫 벡터)
import numpy as np

def one_hot(state):
    #(1) 벡터 준비
    HEIGHT, WIDTH=3, 4
    vec=np.zeros(HEIGHT*WIDTH, dtype=np.float32)

    #(2) state에 해당하는 원소만 1.0으로 설정
    y, x=state
    idx=WIDTH*y+x
    vec[idx]=1.0

    #(3) 배치 처리를 위해 새로운 축 추가
    return vec[np.newaxis, :]

state=(2, 0)
x=one_hot(state)

print(x.shape)
#(1, 12)
print(x)
#[[0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]


#Q 함수(테이블(defaultdict)) 구현
from collections import defaultdict

Q=defaultdict(lambda: 0)
state=(2, 0)
action=0

print(Q[state, action])
#0.0


#2계층의 완전 연결 형태로 구성된 신경망 구현
from dezero import Model
import dezero.functions as F
import dezero.layers as L

class QNet(Model):
    def __init__(self):
        super().__init__()
        self.l1=L.Linear(100) #중간층의 크기
        self.l2=L.Linear(4) #행동의 크기(가능한 행동의 개수)
    
    def forward(self, x):
        x=F.relu(self.l1(x))
        x=self.l2(x)
        return x

qnet=QNet()

state=(2, 0)
state=one_hot(state) #원-핫 벡터로 변환

qs=qnet(state)
print(qs.shape)
#(1, 4)

from dezero import optimizers

class QLeaningAgent:
    def __init__(self):
        self.gamma=0.9
        self.lr=0.01
        self.epsilon=0.1
        self.action_size=4

        self.qnet=QNet() #신경망 초기화
        self.optimizer=optimizers.SGD(self.lr) #옵티마이저 생성
        self.optimizer.setup(self.qnet) #옵티마이저에 신경망 등록

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.action_size)
        else:
            qs=self.qnet(state)
            return qs.data.argamx()
    
    def update(self, state, action, reward, next_state, done):
        #(1)다음 상태에서 최대가 되는 Q 함수의 값(next_q) 계산
        if done: #(2) 목표 상태에 도달
            next_q=np.zeros(1) 
            #(3) [0.](목표 상태에서의 Q 함수는 항상 0)
        else:
            next_qs=self.qnet(next_state)
            next_q=next_qs.max(axis=1)
            next_q.unchain() #(4)next_q를 역전파 대상에서 제외
        
        #(5) 목표
        target=self.gamma*next_q+reward
        #(6) 현재 상태에서의 Q 함수 값(q) 계산
        qs=self.qnet(state)
        q=qs[:,action]
        #(7) 목표(target)와 q의 오차 계산
        loss=F.mean_squared_error(target, q)

        #(8) 역전파-> 매개변수 갱신
        self.qnet.cleargrads()
        loss.backward()
        self.optimizer.update()

        return loss.data
    
    # def update(self, state, action, reward, next_state, done):
    #     done=int(done) #(1) 0 or 1
    #     next_qs=self.qnet(next_state)
    #     next_q=next_qs.max(axis=1)
    #     next_q.unchain()
    #     #기존 코드: target=self.gamma*next_q+reward
    #     target=reward(1-done)*self.gamma*next_q #(2)

from gridworld import GridWorld

env=GridWorld()
agent=QLeaningAgent()

episodes=1000 #에피소드 수
loss_history=[]

for episode in range(episodes):
    state=env.reset()
    state=one_hot(state)
    total_loss, cnt=0, 0
    done=False

    while not done:
        action=agent.get_action(state)
        next_state, reward, done=env.step(action)
        next_state=one_hot(next_state)

        loss=agent.update(state, action, reward, next_state, done)
        total_loss+=loss
        cnt+=1
        state=next_state
    
    average_loss=total_loss/cnt
    loss_history.append(average_loss)