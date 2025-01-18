#오차역전파법을 적용한 신경망 구현하기
import sys, os
sys.path.append(os.pardir)
import numpy as np
from collections import OrderedDict
from mnist import load_mnist
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
 

def softmax(x):
    exp_a=np.exp(x)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def cross_entropy_error(y, t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        
        self.x = None
        self.original_x_shape = None
        # 가중치와 편향 매개변수의 미분
        self.dW = None
        self.db = None

    def forward(self, x):
        # 텐서 대응
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        
        dx = dx.reshape(*self.original_x_shape)  # 입력 데이터 모양 변경(텐서 대응)
        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # 손실함수
        self.y = None    # softmax의 출력
        self.t = None    # 정답 레이블(원-핫 인코딩 형태)
        
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size: # 정답 레이블이 원-핫 인코딩 형태일 때
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        
        return dx

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

class TwoLayerNet:  #입력층(뉴런 수), 은닉층, 출력층, 가중치 초기화시 정규분포 스케일
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params={}  #신경망의 매개변수를 보관
        self.params['W1']=weight_init_std*np.random.randn(input_size, hidden_size)
        #1번째 층의 가중치(self.params['W1'])
        self.params['b1']=weight_init_std*np.random.randn(hidden_size)
        #1번째 층의 편향(self.params['b1'])
        self.params['W2']=weight_init_std*np.random.randn(hidden_size, output_size)
        #2번째 층의 가중치(self.params['W2'])
        self.params['b2']=np.zeros(output_size)
        #2번째 층의 편향(self.params['b2'])

        #계층 생성
        self.layers=OrderedDict()   #순서가 있는 딕셔너리-> 순전파 때 순서대로 호출함.
        self.layers['Affine1']=Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1']=Relu()
        self.layers['Affine2']=Affine(self.params['W2'], self.params['b2'])
        self.lastLayer=SoftmaxWithLoss()
    
    def predict(self, x):   #예측(추론)을 수행함, 인수 x는 이미지 데이터
        for layer in self.layers.values():
            x=layer.forward(x)
        return x
    
    def loss(self, x, t):   #손실 함수의 값을 구한다, 인수 x는 이미지 데이터, t는 정답 레이블
        y=self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):   #정확도를 구한다.
        y=self.predict(x)
        y=np.argmax(y, axis=1)
        if t.ndim!=1:t=np.argmax(t, axis=1) #argmax-> 가장 높은 요소의 인덱스

        accuracy=np.sum(y==t)/float(x.shape[0])
        return accuracy
    
    def numerical_gradient(self, x, t): #가중치 매개변수의 기울기를 수치 미분 방식으로 구한다.
        loss_W=lambda W:self.loss(x, t)

        grads={}
        grads['W1']=numerical_gradient(loss_W, self.params['W1'])
        grads['b1']=numerical_gradient(loss_W, self.params['b1'])
        grads['W2']=numerical_gradient(loss_W, self.params['W2'])
        grads['b2']=numerical_gradient(loss_W, self.params['b2'])
        return grads
    
    def gradient(self, x, t):   #가중치 매개변수의 기울기를 오차역전파법으로 구한다.
        #순전파
        self.loss(x,t)

        #역전파
        dout=1
        dout=self.lastLayer.backward(dout)

        layers=list(self.layers.values())
        layers.reverse()    #순전파에서 OrderedDict로 리스트에 담았으므로
        for layer in layers:    #역전파에서는 그 리스트를 reverse()한다.
            dout=layer.backward(dout)
        
        #결과 저장
        grads={}
        grads['W1']=self.layers['Affine1'].dW
        grads['b1']=self.layers['Affine1'].db
        grads['W2']=self.layers['Affine2'].dW
        grads['b2']=self.layers['Affine2'].db
        return grads

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 기울기 계산
    #grad = network.numerical_gradient(x_batch, t_batch) # 수치 미분 방식
    grad = network.gradient(x_batch, t_batch) # 오차역전파법 방식(훨씬 빠르다)
    
    # 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)
