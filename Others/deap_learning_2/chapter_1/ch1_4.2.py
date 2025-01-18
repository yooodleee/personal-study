#신경망 구현
'''
은닉층이 하나인 신경망을 구현한다.
'''
import sys
sys.path.append('..')
import numpy as np

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