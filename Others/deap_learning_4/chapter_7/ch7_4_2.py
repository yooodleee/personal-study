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
#