#활성화 함수 계층 구현하기(ReLu 계층)
'''
y=x(x>0), 0(x<=0)

dy/dx=1(x>0), 0(x<=0)

순전파 떄의 입력인 x가 0보다 크면 역전파는 상류의 값을 그대로 하류로 흘린다.
반면, 순전파 때 x가 0 이하이면 역전파 때는 하류로 신호를 보내지 않는다(0을 보낸다).
'''
import numpy as np

class Relu:
    def __init__(self):
        self.mask=None  
    
    def forward(self, x):
        self.mask=(x<=0)
        out=x.copy()
        out[self.mask]=0
        return out
    
    def backward(self, dout):
        dout[self.mask]=0
        dx=dout
        return dx

x=np.array([[1.0, -0.5], [-2.0, 3.0]])
print(x)
# [[ 1.  -0.5]
#  [-2.   3. ]]

mask=(x<=0) #mask(인스턴스 변수)-> True, False로 구성된 넘파이 배열
print(mask)
# [[False  True]
#  [ True False]]
'''
순전파 때의 입력 값이 0 이하면 역전파 때의 값은 0이 되야한다.
-> 역전파 떄는 순전파 때 만들어둔 mask를 써서 mask의 원소가 True인 곳에는 상류에서 전파된\
dout을 0으로 생성한다.
'''