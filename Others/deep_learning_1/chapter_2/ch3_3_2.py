#NAND, OR 게이트 구현하기
import numpy as np

def NAND(x1, x2):
    x=np.array([x1, x2])
    w=np.array([-0.5,-0.5]) #AND와는 가중치(w1, w2)와 편향(b)만 다르다.
    b=0.7

    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x=np.array([x1, x2])
    w=np.array([0.5,0.5])   #AND와는 가중치(w1, w2)와 편향(b)만 다르다.
    b=-0.2

    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
    