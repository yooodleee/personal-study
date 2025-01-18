import numpy as np

x=np.array([[51,55],[14,19],[0,4]])
x=x.flatten()   #x를 1차원 배열로 변환(평탄화)
print(x)    #[51 55 14 19 0 4]

x[np.array([0,2,4])]    #인덱스가 0,2,4인 원소 얻기
#array([51, 14, 0])

x>15    #x에서 15이상인 값(bool형)
# array([True, True, False, True, False, False], dtype=bool)

x[x>15] #x에서 15이상인 값
# array([51, 55, 19])