#매개변수 갱신
'''
*최적화
-> 신경망 학습의 목적은 손실 함수의 값을 낮추는 매개변수를 찾는 것이다.
매개변수의 최적값을 찾는 문제.

그러나, 매개변수 공간은 매우 넓고 복잡해서 최적의 솔루션을 찾기란 쉽지 않다.
수식을 풀어 순식간에 최적값을 구하는 방법은 없다.
게다가 심층 신경망에서는 매개변수의 수가 엄청나게 많아진다.

매개변수의 기울기를 구해, 기울어진 방향으로 매개변수 값을 갱신하는 일을 반복하여 최적 값에 다가간다.
-> 확률적 경사 하강법(SGD)
'''
#확률적 경사 하강법(SGD)
'''
W<-W-etha dL/dW

W:갱신할 가중치 매개변수
dL/dW:W에 대한 손실 함수의 기울기
etha: 학습률(0.1, 0.01... 미리 정해서 사용)
<-:우변의 값으로 좌변의 값을 갱신한다.

SGD는 기울어진 방향으로 일정 거리만 가겠다는 방법이다.
'''
import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def cross_entropy_error(y, t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 값 복원
        it.iternext()   
        
    return grad

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
    
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        
        return y
        
    # x : 입력 데이터, t : 정답 레이블
    def loss(self, x, t):
        y = self.predict(x)
        
        return cross_entropy_error(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x : 입력 데이터, t : 정답 레이블
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads
        
    def gradient(self, x, t):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        grads = {}
        
        batch_num = x.shape[0]
        
        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        
        # backward
        dy = (y - t) / batch_num
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)
        
        da1 = np.dot(dy, W2.T)
        dz1 = sigmoid_grad(a1) * da1
        grads['W1'] = np.dot(x.T, dz1)
        grads['b1'] = np.sum(dz1, axis=0)

        return grads

class SGD:
    def __init__(self, lr=0.01):    #lr:학습률
        self.lr=lr
    
    def update(self, params, grads):    #SGD 과정에서 반복해서 불림, params와 grads는 딕셔너리 변수
        for key in params.keys():
            params[key]-=self.lr*grads[key]

network=TwoLayerNet(...)
optimizer=SGD()

for i in range(10000):
    ...
    x_batch, t_batch=get_mini_batch(...)    #미니배치
    grads=network.gradient(x_batch, t_batch)
    params=network.params
    optimizer.update(params, grads)
    '''
    최적화를 담당하는 클래스를 분리해 구현하면 기능을 모듈화하기 좋다.
    '''

'''
*SGD의 단점

비등방성anisotropy 함수(방향에 따라 성질, 즉 여기서는 기울기가 달라지는 함수)에서는\
탐색 경로가 비효율적이다.
이럴 때는 SGD 같이 무작정 기울어진 방향으로 진행하는 단순한 방식보다 더 영리한 묘안이 간절해진다.
또한, SGD가 지그재그로 탐색하는 근본 원인은 기울어진 방향이 본래의 최솟값과 다른 방향을 가리켜서라는\
점도 생각해볼 필요가 있다.
'''