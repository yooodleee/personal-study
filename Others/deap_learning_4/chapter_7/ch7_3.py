#비선형 데이터셋
import numpy as np

np.random.seed(0)
x=np.random.rand(100, 1)
y=np.sin(2*np.pi*x)+np.random.rand(100, 1)


#신경망 구현
from dezero import Variable
import dezero.functions as F

w1, b1=Variable(...), Variable(...)
w2, b2=Variable(...), Variable(...)

def predict(x):
    y=F.linear(x, w1, b1) #선형 변횐
    y=F.sigmoid(y) #활성화 함수(시그모이드 함수)
    y=F.linear(y, w2, b2) #선형 변환
    return y