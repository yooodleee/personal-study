#행렬의 곱(2x2)
import numpy as np

A=np.array([[1,2],[3,4]])
A.shape
#(2,2)

B=np.array([[5,6],[7,8]])
B.shape
#(2,2)

np.dot(A, B)    #두 행렬의 곱은 넘파이 함수 np.dot(), np.dot(A,b)와 np.dot(B,A)는 다를 수 있다.
# array([[19,22],
#        [43,50]])