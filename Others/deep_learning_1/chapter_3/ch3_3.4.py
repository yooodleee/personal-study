#행렬의 곱
import numpy as np

A=np.array([[1,2],[3,4],[5,6]])
A.shape
#(3,2)

B=np.array([7,8])
B.shape
#(2,)

np.dot(A, B)
#array([23,53,83])