#행렬의 곱(2x3, 3x2)
import numpy as np

A=np.array([[1,2,3],[4,5,6]])   #행렬의 형상(shape)
A.shape
#(2,3)

B=np.array([[1,2],[3,4],[5,6]])
B.shape
#(3,2)

np.dot(A,B)     #A의 원소 수(열 수)=B의 차원의 수(행 수), 대응하는 차원의 원소 수를 일치시켜라
# array([[22,28],
#        [49,64]])