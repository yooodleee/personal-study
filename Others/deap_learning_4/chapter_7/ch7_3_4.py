#계층과 모델
import numpy as np
import dezero.layers as L

linear=L.Linear(10) #출력 크기만 지정하여 Linear 계층 생성

batch_size, input_size=100, 5
x=np.random.randn(batch_size, input_size)
y=linear(x) #입력 데이터 x에 대해 선형 변환 수행

print('y shape:', y.shape)
print('params shape:', linear.W.shape, linear.b.shape)

for param in linear.params(): #매개변수들에 접근
    print(param.name, param.shape)

# y shape: (100, 10)
# params shape: (5, 10) (10,)
# W (5, 10)
# b (10,)


#신경망을 클래스 하나로 정의
from dezero import Model
import dezero.layers as L
import dezero.functions as F

class TwoLayerNet(Model):
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1=L.Linear(hidden_size)
        self.l2=L.Linear(out_size)

    def forward(self, x):
        y=F.relu(self.l1(x))
        y=self.l2(y)
        return y

model=TwoLayerNet(10, 1)

#모든 매개변수에 접근
for param in model.params():
    print(param)

#모든 매개변수의 기울기 초기화
model.cleargrads()

# variable(None)
# variable([0.])
# variable(None)
# variable([0. 0. 0. 0. 0. 0. 0. 0. 0. 0.])


#sin 함수의 비선형 데이터를 dezero.Model과 dezero.layers를 사용하여 학습
import numpy as np
from dezero import Model
import dezero.layers as L
import dezero.functions as F

#데이터셋 생성
np.random.seed(0)
x=np.random.rand(100, 1)
y=np.sin(2*np.pi*x)+np.random.rand(100, 1)

lr=0.2
iters=10000

class TwoLayerNet(Model): #2층 신경망
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1=L.Linear(hidden_size)
        self.l2=L.Linear(out_size)

    def forward(self, x):
        y=F.sigmoid(self.l1(x))
        y=self.l2(y)
        return y
    
model=TwoLayerNet(10, 1) #신경망 모델 생성

for i in range(iters):
    y_pred=model.forward(x) #또는 y_pred=model(x)
    loss=F.mean_squared_error(y, y_pred)

    model.cleargrads()
    loss.backward()

    for p in model.params():
        p.data-=lr*p.grad.data
    
    if i %1000==0:
        print(loss)

# variable(0.07618764131185572)

