#모멘텀momentum
'''
운동량을 뜻하는 단어
'''
import numpy as np

class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr=lr
        self.momentum=momentum
        self.v=None #v-> 물체의 속도
    
    def update(self, params, grads):
        if self.v is None:
            self.v={}   
            #update가 처음 호출될 때 매개변수와 같은 구조의 데이터를 딕셔너리 변수로 저장.
            for key, val in params.items():
                self.v[key]=np.zeros_like(val)  #속도(key)=val과 같은 

        for key in params.keys():
            self.v[key]=self.momentum*self.v[key]-self.lr*grads[key]    #모멘텀*속도(key)-학습률*기울기(key)
            params[key]+=self.v[key]
'''
보통 모멘텀의 갱신 경로는 공이 그릇 바닥을 구르듯 움직인다.
SGD와 비교하면 '지그재그 정도'가 덜 하다.
-> x축의 힘은 크지만 위아래로 번갈아 받아서 상충하여 y축의 방향의 속도는 안정적이지 않다.
-> 전체적으로 SGD보다 x축 방향으로 빠르게 다가가 지그재그 움직임이 줄어든다.
'''