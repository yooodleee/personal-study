import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[3,0],[0,6]])

A+B
# array([[4,2],
#        [3,10]])
A*B
# array([[3,0],
#        0,24])
A*10
# array([[10,20],
#        [30,40]])

'''
넘파이 배열(np.array)은 N차원 배열을 작성할 수 있다.
1차원 배열-> 벡터 vector
2차원 배열-> 행렬 matrix
행렬과 벡터를 일반화한 텐서tensor
'''