#가중치와 편향 구현하기(AND 게이트)
'''
편향(b=-theta)은 가중치 w1, w2와 기능이 다르다.
w1, w2는 각 입력 신호가 결과에 주는 영향력(중요도)를 조절하는 매개변수고,\
편향은 얼마나 쉽게 활성화(결과를 1로 출력)하느냐를 조정하는 매개변수이다.
'''
import numpy as np

def AND(x1, x2):
    x=np.array([x1, x2])
    w=np.array([0.5,0.5])
    b=-0.7

    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
