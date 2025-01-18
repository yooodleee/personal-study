#학습 알고리즘 구현하기
'''
1) 전제
    신경망에 적응 가능한 가중치와 편향이 있고, 이 가중치와 편향을 훈련 데이터에\
    적응하도록 조정하는 과정을 '학습'이라고 한다.
2) 미니배치
    훈련 데이터 중 일부를 무작위로 가져온다.
    이렇게 선별한 데이터를 미니 배치라고 하며, 그 미니배치의 손실 함수 값을 줄이는 것이 목표이다.
3) 기울기 산출
    미니배치의 손실 함수 값을 줄이기 위해 각 가중치 매개변수의 기울기를 구한다.
    기울기는 손실 함수의 값을 가장 작게 하는 방향을 제시한다.
4) 매개변수 갱신
    가중치 매개변수를 기울기 방향으로 아주 조금 갱신한다.
5) 반복
    2~4를 반복한다.

경사 하강법으로 매개변수를 갱신하는 방법이며, 이때 데이터를 미니배치로 무작위로\
선정하기 때문에 '확률적 경사 하강법stochastic gradient descenden, SGD라고 부른다.
확률적으로 무작위로 골라낸 데이터에 대해 수행하는 경사 하강법이라는 의미이다.
대부분의 딥러닝 프레임워크는 SGD로 구현하고 있다.
'''
#2층 신경망 클래스 구현하기
import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import *
from common.gradient import numeriacal_gradient

def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def sigmoid(x):
    return 1/(1+np.exp(-x))

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

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params={}
        self.params['W1']=weight_init_std*np.random.randn(input_size, hidden_size)
        self.params['b1']=np.zeros_like(hidden_size)
        self.params['W2']=weight_init_std*np.random.randn(hidden_size, output_size)
        self.params['b2']=np.zeros_like(output_size)
    
    def predict(self,x):
        W1,W2=self.params['W1'],self.params['W2']
        b1,b2=self.params['b1'],self.params['b2']

        a1=np.dot(x,W1)+b1
        z1=sigmoid(a1)
        a2=np.dot(z1, W2)+b2
        y=softmax(a2)

        return y
    
    #x:입력 데이터, t:정답 레이블
    def loss(self,x,t):
        y=self.predict(x)
        return cross_entropy_error(y,t)
    
    def accuracy(self,x,t):
        y=self.predict(x)
        y=np.argmax(y,axis=1)
        t=np.argmax(t,axis=1)

        accuracy=np.sum(y==t)/float(x.shape[0])
        return accuracy
    
    def numerical_gradient(self,x,t):
        loss_W=lambda W:self.loss(x,t)

        grads={}
        grads['W1']=numerical_gradient(loss_W, self.params['W1'])
        grads['b1']=numerical_gradient(loss_W, self.params['b1'])
        grads['W2']=numerical_gradient(loss_W, self.params['W2'])
        grads['b2']=numerical_gradient(loss_W, self.params['b2'])

        return grads

#예측 처리(순방향 처리) 실행
net=TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
x=np.random.randn(100,784)  #더미 입력 데이터(100장 분량)
y=net.predict(x)
t=np.random.randn(100,10)   #더미 정답 레이블(100장 분량)

grads=net.numerical_gradient(x,t)   #기울기 계산

net.params['W1'].shape  #(784, 10)
net.params['b1'].shape  #(100,)
net.params['W2'].shape  #(100,10)
net.params['b2'].shape  #(10,)


'''
*변수

1) params-> 신경망의 매개변수를 보관하는 딕셔너리 변수(인스턴스 변수)
            params['W1']:1번째 층의 가중치, params['b1']:1번째 층의 편향
            신경망에 필요한 매개변수가 모두 저장됨
            저장된 가중치 매개변수가 예측 처리(순방향 처리)에서 사용된다.

2) grads-> 기울기를 보관하는 딕셔너리 변수(numerical_gradient) 메서드의 변환 값
            grads['W1']:1번째 층의 가중치의 기울기, grads['b1']:1번째 층의 편향의 기울기
'''
'''
*메서드

1) __init__(self, input_size, hidden_size, output_size)
-> 초기화를 수행하고 인수는 순서대로 입력층의 뉴런수, 은닉층의 뉴런수, 출력층의 뉴런수

2) predict(self, x)-> 예측(추론)을 수행함, 인수 x는 이미지 데이터

3) loss(self, x, t)-> 손실 함수의 값을 구한다, 인수 x는 이미지 데이터, t는 정답 레이블

4) accuaracy(self, x, t)-> 정확도를 구한다.

5) numarical_gradient(self, x, t)-> 가중치 매개변수의 기울기를 구한다.

6) gradient(self, x, t)-> 가중치 매개변수의 기울기를 구한다.오차역전파법을 이용하여 기울기를 효율적으로 계산.
'''