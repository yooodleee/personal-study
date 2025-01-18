#Sofrmax-with-Loss 계층

'''
소프트맥스 함수는 입력 값을 정규화하여 출력한다.
-> 출력의 합이 1이 되도록 변형하여 출력함.

손실 함수인 교차 엔트로피 오차도 포함하여 'softmax-with-Loss 계층'이라는 이름으로 구현한다.
'''

'''
소프트맥스 함수는 'Softmax' 계층으로, 교차 엔트로피 오차는 'Cross Entropy Error' 계층으로
3클래스 분류를 가정하고 이전 계층에서 3개의 입력(점수)를 받는다.
Softmax 계층은 입력 (a1, a2, a3)를 정규화하여 (y1, y2, y3)를 출력한다.
Cross Entropy Error'계층은 Softmax의 출력 (a1, a2, a3)과 정답 레이블(t1, t2, t3)를 받고,\
이 데이터들로부터 손실 L을 출력한다.

Softmax 계층의 역전파는 (y1-t1, y2-t2, y3-t3)라는 '말끔한' 결과를 내놓고 있다.
(y1, y2, y3)는 Softmax의 출력이고, (t1, t2, t3)는 정답 레이블이므로\
(y1-t1, y2-t2, y3-t3)는 Softmax의 출력과 정답 레이블의 차분이다.
-> 이 차이인 오차가 앞 계층에 전해지는 것이다.

신경망 학습의 목적은 신경망의 출력(softmax의 출력)이 정답 레이블과 가까워지도록 가중치\
매개변수의 값을 조정하는 것이다.
그래서 신경망의 출력과 정답 레이블의 오차를 효율적으로 앞 계층에 전달해야 한다.
-> 신경망의 현재 출력과 정답 레이블의 오차를 있는 그대로 드러내는 것이다.
'''
import numpy as np

def softmax(x):
    exp_a=np.exp(x)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

def cross_entropy_error(y, t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))

class SoftmaxWithLoss:
    def __init__(self):
        self.loss=None
        self.y=None
        self.t=None
    
    def forward(self, x, t):
        self.t=t
        self.y=softmax(x)
        self.loss=cross_entropy_error(self.y, self.t)
        return self.loss
    
    def backward(self, dout=1): #전파하는 값을 배치의 수(batch_size)로 나눠 데이터 1개당 오차를 앞 계층으로 전파함에 주의한다.
        batch_size=self.t.shape[0]
        dx=(self.y-self.t)/batch_size
        return dx