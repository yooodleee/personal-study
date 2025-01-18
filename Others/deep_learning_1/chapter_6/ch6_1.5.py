#AdaGrad
'''
학습률을 정하는 효과적 기술-> 확률적 감소learning rate decay
-> 학습을 진행하면서 학습률을 점차 줄이는 방법.
처음에는 크게 학습하다가 점점 작게 학습한다.

매개변수 '전체'의 학습률 값을 일괄적으로 낮춘다.-> AdaGrad
-> 각각의 매개변수에 맞춤형 값을 만들어준다.

개별 매개변수에 적응적으로adaptive 학습률을 조정하면서 학습을 진행한다.

h<-h+dL/dW (원소별 곱셈) dL/dW
W<-W- lr*[1/{(h)**1/2}]*dL/dW

W:갱신할 가중치 매개변수
dL/dW: W에 대한 손실 함수의 기울기
h: 기존 기울기라고 매개변수를 갱신할 때 1/{(h)**1/2}를 곱해 학습률을 조정한다.

매개변수의 원소 중에서 많이 움직인(크게 갱신된) 원소는 학습률이 낮아지는데,\
학습률 감소가 매개변수의 원소마다 다르게 적용됨을 의미한다.
'''

'''
Adagrad는 과거의 기울기를 제곱하여 계속 더해간다.
-> 학습을 진행할수록 갱신 강도가 약해진다.
-> 계속 학습하면 어느 순간 갱신량이 0이 되어 전혀 갱신되지 않게 된다.
-> RMSProp은 이를 개선한 방법이다.

먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영한다.
지수동평균Exponential Moving Average(XMA)라 하고, 과거 기울기의 반영 규모를 기하급수적으로 감소시킨다.
'''
import numpy as np

class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr=lr
        self.h=None
    
    def update(self, params, grads):
        if self.h is None:
            self.h={}
            for key, val in params.items():
                self.h[key]=np.zeros_like(val)
        
        for key in params.keys():   
            self.h[key]+=grads[key]*grads[key]  #h=기울기를 제곱하여 계속 더해준다.
            params[key]-=self.lr*grads[key]/(np.sqrt(self.h[key]+1e-7))
            #sqrt(self.h[key]+1e-7) -> 매개변수를 갱신할 때 1/(h)**1/2을 곱해 학습률을 조정한다.