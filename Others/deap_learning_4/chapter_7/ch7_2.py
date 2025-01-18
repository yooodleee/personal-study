#선형 회귀(토이 데이터셋)
import numpy as np

np.random.seed(0) #시드 고정
x=np.random.rand(100, 1)
y=5+2*x+np.random.rand(100, 1)


#선형 회귀 구현(경사 하강법을 이용한 손실 함수(평균 제곱 오차) 구현)
import numpy as np
from dezero import Variable
import dezero.functions as F

#토이 데이터셋
np.random.seed(0)
x=np.random.rand(100, 1)
y=5+2*x+np.random.rand(100, 1)
x, y=Variable(x), Variable(y) #생략 가능

#매개변수 정의
W=Variable(np.zeros((1, 1)))
b=Variable(np.zeros(1))

#예측 함수
def predict(x):
    y=F.matmul(x, W)+b #행렬 곱으로 여러 데이터 일괄 계산
    return y


#평균 제곱 오차(식 7.2) 계산 함수
def mean_squared_error(x0, x1):
    diff=x0-x1
    return F.sum(diff**2)/len(diff)

#경사 하강법으로 매개변수 갱신
lr=0.1
iters=100

for i in range(iters):
    y_pred=predict(x)
    loss=mean_squared_error(y, y_pred)
    #또는 loss=F.mean_squared_error(y, y_pred)
    W.cleargrad()
    b.cleargrad()
    loss.backward()

    W.data-=lr*W.grad.data
    b.data-=lr*b.grad.data

    if i % 10==0: #10회 반복마다 출력
        print(loss.data)

print('===')
print('W= ', W.data)
#W=  [[2.11807369]]
print('b= ', b.data)
#b=  [5.46608905]