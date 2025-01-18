#신경망 학습
import numpy as np
from dezero import Variable
import dezero.functions as F

#데이터셋
np.random.seed(0)
x=np.random.rand(100, 1)
y=np.sin(2*np.pi*x)+np.random.rand(100, 1)

#(1) 매개변수 초기화
I, H, O=1, 10, 1 #I=입력층 차원 수, H=은닉층 차원 수, O=출력층 차원 수
w1=Variable(0.01*np.random.rand(I, H)) #첫 번째 층의 가중치
b1=Variable(np.zeros(H)) #첫 번째 층의 편향
w2=Variable(0.01*np.random.randn(H, O)) #두 번째 층의 가중치
b2=Variable(np.zeros(O)) #두 번째 층의 편향

#(2) 신경망 추론
def predict(x):
    y=F.linear(x, w1, b1)
    y=F.sigmoid(y)
    y=F.linear(y, w2, b2)
    return y

lr=0.2
iters=10000

#(3) 신경망 학습(매개변수 갱신)
for i in range(iters):
    y_pred=predict(x)
    loss=F.mean_squared_error(y, y_pred)

    w1.cleargrad()
    b1.cleargrad()
    w2.cleargrad()
    w2.cleargrad()

    loss.backward()

    w1.data-=lr*w1.grad.data
    b1.data-=lr*b1.grad.data
    w2.data-=lr*w2.grad.data
    b2.data-=lr*b2.grad.data

    if i %1000==0: #1000회마다 출력
        print(loss.data)

#0.07703265167191234
