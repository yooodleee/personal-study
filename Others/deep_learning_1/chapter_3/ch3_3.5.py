#신경망에서의 행렬 곱(편향과 활성화 함수를 생략하고 가중치만 갖는다.)
import numpy as np

x=np.array([1,2])
x.shape
#(2,)

w=np.array([[1,3,5],[2,4,6]])
print(w)
w.shape
# [[1 3 5]
#  [2 4 6]]

y=np.dot(x,w)
print(y)
#[ 5 11 17]