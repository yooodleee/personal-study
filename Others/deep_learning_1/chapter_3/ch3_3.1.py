#다차원 배열(1차원 배열-> 벡터vector)
import numpy as np

A=np.array([1,2,3])
np.ndim(A)  #배열의 차원 수
#[1 2 3 4]

A.shape #배열의 형상-> 인스턴스 변수 shape, 튜플(다차원 배열일 경우와 동일된 형태로 결과 반환)
#(4,)

A.shape[0]
#4

#다차원 배열(2차원 배열-> 행렬metrix)
B=np.array([[1,2],[3,4],[5,6]])
print(B)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
np.ndim(B)  #배열의 차수(2)
#2

B.shape #배열의 형상
#(3,2)