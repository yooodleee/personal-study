#신경망에서의 기울기
'''
기울기는 가중치 매개변수에 대한 손실 함수의 기울기이다.

가중치가 W, 손실 함수가 L인 신경망이 있다고 하자.
이 경우 경사는 dL/dW로 나타낼 수 있다.

dL/dW의 각 원소는 각각의 원소에 관한 편미분이다.
dL/dW_11은 W_11을 조금 변경했을 떄 손실 함수 L이 얼마나 변화하느냐를 나타낸다.
dL/dW의 형상이 W와 같다.
'''
import sys, os
sys.path.append(os.pardir)
import numpy as np

def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def cross_entropy_error(y, t):
    delta=1e-7
    return -np.sum(t*np.log)

def numerical_gradient(f,x):    
    h=1e-4
    grad=np.zeros_like(x)  

    for idx in range(x.size):
        tmp_val=x[idx]

        #f(x+h) 계산  
        x[idx]=tmp_val+h
        fxh1=f(x)

        #f(x-h) 계산
        x[idx]=tmp_val-h
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val  #값 복원
    
    return grad

from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:    #클래스 형상이 2x3인 가중치 매개변수 하나를 인스턴스 변수로 갖는다.
    def __init__(self):
        self.W=np.random.randn(2,3)
    
    def predict(self, x):   #예측을 수행하는 메서드
        return np.dot(x, self.W)
    
    def loss(self, x, t):   #손실 함수의 값을 구하는 메서드, x:입력 데이터, t:정답 레이블
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        return loss

net=simpleNet()
print(net.W)    #가중치 매개변수

x=np.array([0.6, 0.9])
p=net.predict(x)
print(p)

z=np.argmax(p)  #최댓값의 인덱스
print(z)

t=np.array([0, 0, 1])   #정답 레이블
z2=net.loss(x, t)
print(z2)

#기울기
def f(W):   #f(W) 함수의 인수 W는 더미dummy로 만든 것이다.
    return net.loss(x,t)

dW=numerical_gradient(f, net.W) 
#numerical_gradient 내부에서 f(x)를 실행하는데, 일관성을 위해 f(w)를 정의함
print(dW)

'''
numerical_gradient(f,x)의 인수 f는 함수, x는 함수 f의 인수이다.
-> net.W를 인수로 받아 손실 함수를 계산하는 새로운 함수 f를 정의했다.
-> 이 새로 정의한 함수를 numerical_gradient(f,x)에 넘긴다.

dW는 numerical_gradient(f,net.W)의 결과로, 그 형상은 2x3의 2차원 배열이다.
dW의 내용을 보면, 예를 들어 dL/dW의 dL/dW_11은 대략 0.2이다.
이는 W_11을 h만큼 늘리면 손실 함수의 값은 0.2h만큼 증가한다는 의미이다.

-> 손실 함수를 줄인다는 관점에서는 dL/dW_23의 양의 방향으로 갱신하고\
W11은 음의 방향으로 갱신해야 함을 알 수 있다.
-> 한 번에 갱신되는 양에는 dL/dW_23이 W_11보다 크게 기여한다는 사실도 알 수 있다.
'''
#lambda를 쓰면 간단한 함수를 정의하는 데 더 편리하다.

f=lambda W:net.loss(x,t)
dW=numerical_gradient(f, net.W)