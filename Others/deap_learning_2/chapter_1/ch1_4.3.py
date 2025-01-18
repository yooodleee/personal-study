#학습용 코드
'''
학습 데이터를 읽어 들여 신경망(모델)과 옵티마이저(최적화기)를 생성한다.
학습의 4단계의 절차를 수행한다.
'''
import sys
sys.path.append('..')
import matplotlib.pyplot as plt
import numpy as np

#하이퍼 파라미터 설정
max_epoch=300
batch_size=30
hidden_size=10
learning_rate=1.0

def load_data(seed=1984):
    np.random.seed(seed)
    N = 100  # 클래스당 샘플 수
    DIM = 2  # 데어터 요소 수
    CLS_NUM = 3  # 클래스 수

    x = np.zeros((N*CLS_NUM, DIM))
    t = np.zeros((N*CLS_NUM, CLS_NUM), dtype=np.int)

    for j in range(CLS_NUM):
        for i in range(N): # N*j, N*(j+1)):
            rate = i / N
            radius = 1.0*rate
            theta = j*4.0 + 4.0*rate + np.random.randn()*0.2

            ix = N*j + i
            x[ix] = np.array([radius*np.sin(theta),
                              radius*np.cos(theta)]).flatten()
            t[ix, j] = 1

    return x, t

def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def cross_entropy_error(y, t):
    if y.ndim == 1: #y(입력 데이터)가 1차원일 때
        t = t.reshape(1, t.size)    #t(정답 테이블)을 reshpae
        y = y.reshape(1, y.size)    #y(입력 데이터)를 reshape
        
    # 정답 데이터가 원핫 벡터일 경우 정답 레이블 인덱스로 변환
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]

    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

class Sigmoid:
    def __init__(self):
        self.params, self.grads=[], []
        self.out=None
    
    def forward(self, x):
        out=1/(1+np.exp(-x))
        self.out=out
        return out
    
    def backward(self, dout):
        dx=dout*(1.0-self.out)*self.out
        return dx

class Affine:
    def __init__(self, W, b):
        self.params=[W, b]
        self.grads=[np.zeros_like(W), np.zeros_like(b)]
        self.x=None
    
    def forward(self, x):
        W, b=self.params
        out=np.matmul(W, b) #가중치와 편향에 대해 행렬의 곱 계산
        self.x=x
        return out
    
    def backward(self, dout):
        W, b=self.params
        dx=np.matmul(dout, W.T) #dx인 경우에는 dout*W의 전치행렬
        dW=np.matmul(self.x.T, dout)    #dW인 경우에는 dout*x의 전치행렬
        db=np.sum(dout, axis=0)

        self.grads[0][...]=dW   #깊은 복사(...)
        self.grads[1][...]=db   #깊은 복사(...)
        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.y = None  # softmax의 출력
        self.t = None  # 정답 레이블

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x) 

        # 정답 레이블이 원핫 벡터일 경우 정답의 인덱스로 변환
        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, self.t)
        return loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]

        dx = self.y.copy()
        dx[np.arange(batch_size), self.t] -= 1
        dx *= dout
        dx = dx / batch_size

        return dx

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size):
        #입력층 뉴런수, 은닉층 뉴런수, 출력층 뉴런수
        I,H,O=input_size, hidden_size, output_size

        W1=0.01*np.random.randn(I, H)   #가중치를 작은 무작위 값으로 초기화-> 학습이 잘 진행될 수 있음
        b1=np.zeros(H)  #편향을 영벡터zero vector로 초기화한다.
        W2=0.01*np.random.randn(H, O)
        b2=np.zeros(O)

        self.layers=[
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]
        self.loss_layer=SoftmaxWithLoss()   #소프트맥스와 손실함수

        self.params, self.grads=[], []  #이 모델에서 사용하는 매개변수들과 기울기들을 각각 하나로 모은다.
        for layer in self.layers:
            self.params+=layer.params
            self.grads+=layer.grads
    
    def predict(self, x):
        for layer in self.layers:
            x=layer.forward(x)  #params가 layer에 들어있음(기울기와 매개변수들을 사용한다)
        return x
    
    def forward(self, x, t):
        score=self.predict(x)   #입력 데이터들에 대해 순전파를 진행한다-> 점수score
        loss=self.loss_layer.forward(score, t)
        return loss #손실 함수도 측정한다.
    
    def backward(self, dout=1):
        dout=self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout=layer.backward(dout)   #layer를 reversed
        
        return dout

class SGD:
    '''
    확률적 경사하강법(Stochastic Gradient Descent)
    '''
    def __init__(self, lr=0.01):
        self.lr = lr
        
    def update(self, params, grads):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]
#데이터 읽기, 모델(신경망)과 옵티마이저(최적화기)
x, t=load_data()
model=TwoLayerNet(input_size=2, hidden_size=hidden_size, output_size=3)
optimizer=SGD(lr=learning_rate)

#학습에 사용하는 변수
data_size=len(x)
max_iters=data_size//batch_size
total_loss=0
loss_count=0
loss_list=[]

for epoch in range(max_epoch):
    #데이터 뒤섞기
    idx=np.random.permutation(data_size)
    x=x[idx]
    t=t[idx]

    for iters in range(max_iters):
        batch_x=x[iters*batch_size:(iters+1)*batch_size]
        batch_t=t[iters*batch_size:(iters+1)*batch_size]

        #기울기를 구해 매개변수 갱신
        loss=model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)

        total_loss+=loss
        loss_count+=1

        #정기적을 학습 경과 출력
        if (iters+1)%10==0:
            avg_loss=total_loss/loss_count
            print('| 에폭%d | 반복 %d / %d | 손실 %.2f' %(epoch+1, iter+1, max_iters+1, avg_loss))
            loss_list.append(avg_loss)
            total_loss, loss_count=0, 0

import numpy as np

a=np.random.permutation(10)
print(a)
