import copy
from collections import deque
import random
import numpy as np
from dezero import Model
from dezero import optimizers
import dezero.functions as F
import dezero.layers as L
import gym

class ReplayBuffer:
    def __init__(self, buffer_size, batch_size):
        self.buffer=deque(maxlen=buffer_size)
        self.batch_size=batch_size

    def add(self, state, action, reward, next_state, done):
        data=(state, action, reward, next_state, done)
        self.buffer.append(data)
    
    def __len__(self):
        return len(self.buffer)
    
    def get_batch(self):
        data=random.sample(self.buffer, self.batch_size)

        state=np.stack([x[0] for x in data])
        action=np.array([x[1] for x in data])
        reward=np.array([x[2] for x in data])
        next_state=np.stack([x[3] for x in data])
        done=np.array([x[4] for x in data]).astype(np.int32)
        return state, action, reward, next_state, done
    
class QNet(Model): #(1) 신경망 클래스
    def __init__(self, action_size):
        super().__init__()
        self.l1=L.Linear(128)
        self.l2=L.Linear(128)
        self.l3=L.Linear(action_size)
    
    def forward(self, x):
        x=F.relu(self.l1(x))
        x=F.relu(self.l2(x))
        x=self.l3(x)
        return x
    
class DQNAgent: #(2) 에이전트 클래스
    def __init__(self):
        self.gamma=0.98
        self.lr=0.0005
        self.epsilon=0.1
        self.buffer_size=1000 #경험 재생 버퍼 크기
        self.batch_size=32 #미니 배치 크기
        self.action_size=2

        self.replay_buffer=ReplayBuffer(self.buffer_size, self.batch_size)
        self.qnet=QNet(self.action_size) #(2) 원본 신경망
        self.qnet_target=QNet(self.action_size) #(2) 목표 신경망
        self.optimizer=optimizers.Adam(self.lr)
        self.optimizer.setup(self.qnet) #(3) 옵티마이저에 qnet 등록
    
    def sync_qnet(self): #(4) 두 신경망 동기화
        self.qnet_target=copy.deepcopy(self.qnet)

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.action_size)
        else:
            state=state[np.newaxis, :] #배치 처리용 차원 추가
            qs=self.qnet(state)
            return qs.data.argmax()
    
    def update(self, state, action, reward, next_state, done):
        #(1) 경험 재생 버퍼에 경험 데이터 추가
        self.replay_buffer.add(state, action, reward, next_state, done)
        if len(self.replay_buffer) < self.batch_size:
            return #데이터가 미니배치 크기만큼 쌓이지 않았으면 여기서 끝
        
        #(2) 미니배치 크기 이상이 쌓이면 미니배치 생성
        state, action, reward, next_state, done=self.replay_buffer.get_batch()

        qs=self.qnet(state) #(3)
        q=qs[np.arange(self.batch_size), action] #(4)

        next_qs=self.qnet_target(next_state) #(5)
        next_q=next_qs.max(axis=1)
        next_q.unchain()
        target=reward+(1-done)*self.gamma*next_q #(6)

        loss=F.mean_squared_error(q, target)

        self.qnet.cleargrads()
        loss.backward()
        self.optimizer.update()


#DQN 실행
epsiodes=300 #에피소드 수
sync_interval=20 #신경망 동기화 주기(20번째 에피소드마다 동기화)
env=gym.make('CartPole-v0', render_mode='rgb_array')
agent=DQNAgent()
reward_history=[] #에피소드별 보상 기록

for episode in range(epsiodes):
    state=env.reset()[0]
    done=False
    total_reward=0

    while not done:
        action=agent.get_action(state)
        next_state, reward, terminated, truncated, info=env.step(action)
        done=terminated|truncated

        agent.update(state, action, reward, next_state, done)
        state=next_state
        total_reward+=reward
    
    if episode % sync_interval==0:
        agent.sync_qnet()
    
    reward_history.append(total_reward)


#ε의 확률로 무작위 행동
agent.epsilon=0 #탐욕 정책(무작위로 행동할 확률 ε을 0으로 설정)
done=False
total_reward=0

while not done:
    action=agent.get_action(state)
    next_state, reward, terminated, truncated, info=env.step(action)
    done=terminated|truncated
    state=next_state
    total_reward+=reward
    env.render()
print('Total Reward:', total_reward)
#