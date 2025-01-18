#배치용 Affine 계층
import numpy as np

class sigmoid:
    def __init__(self):
        self.out=None
    
    def forward(self, x):
        out=1/(1+np.exp(-x))
        self.out=out

        return out
    
    def backward(self, dout):
        dx=dout*(1.0-self.out)*self.out

        return dx

x_dot_W=np.array([[0,0,0],[10,10,10]])
B=np.array([1,2,3])

print(x_dot_W+B)
# [[ 1  2  3]
#  [11 12 13]]

print(x_dot_W)
# [[ 1  2  3]
#  [11 12 13]]

dy=np.array([[1,2,3],[4,5,6]])
print(dy)
# [[1 2 3]
#  [4 5 6]]

dB=np.sum(dy, axis=0)
print(dB)
#[5 7 9]

'''
데이터가 2개(N=2)라고 가정한다.
편향의 역전파는 그 두 데이터에 대한 미분을 데이터마다 더해서 구한다.
-> np.sum()에서 0번째 축(데이터를 단위로 한 축)에 대해서 (axis=0)의 총합을 구한다.
'''
class Affine:
    def __init__(self, W, b):
        self.W=W
        self.b=b
        self.x=None
        self.dW=None
        self.db=None
    
    def forward(self, x):
        self.x=x
        out=np.dot(x, self.W)+self.b

        return out
    
    def backward(self, dout):
        dx=np.dot(dout, self.W.T)
        self.dW=np.dot(self.x.T, dout)
        self.db=np.sum(dout, axis=0)

        return dx