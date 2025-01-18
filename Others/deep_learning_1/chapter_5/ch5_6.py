#Affine/Softmax 계층 구현하기
import numpy as np

x=np.random.rand(2) #x,yw,b-> 형상이 각각 (2,), (2,3), (3,)인 다차원 배열
w=np.random.rand(2,3)
b=np.random.rand(3)

z1=x.shape
print(z1)
#(2,)

z2=w.shape
print(z2)
#(2,3)

z3=b.shape
print(z3)
#(3,)

y=np.dot(x,w)+b
print(y)
#[0.79155135 1.34649834 0.78371039]

'''
*어파인 변환affine transformation
-> 신경망의 순전파 때 수행하는 행렬의 곱은 기하학에서는 어파인 변환이라고 한다.
어파인 변환을 수행하는 처리를 'Affine 게층'이라고 구현한다.
'''