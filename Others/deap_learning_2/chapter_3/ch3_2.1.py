#CBOW 모델의 추론 처리(MatMul 계층)
import sys
sys.path.append('..')
import numpy as np
from layers import MatMul

#샘플 맥락 데이터
c0=np.array([[1,0,0,0,0,0,0]])
c1=np.array([[0,0,1,0,0,0,0]])

#가중치 초기화
W_in=np.random.randn(7,3)
W_out=np.random.randn(3,7)

#계층 생성
in_layer0=MatMul(W_in)
in_layer1=MatMul(W_in)
out_layer=MatMul(W_out)

#순전파
h0=in_layer0.forward(c0)
h1=in_layer1.forward(c1)
h=0.5*(h0+h1)
s=out_layer.forward(h)

print(s)
#[[-0.87055385  0.66627221 -1.84465604 -1.55320244 -1.19941132 -0.78945104
#   1.13609201]]