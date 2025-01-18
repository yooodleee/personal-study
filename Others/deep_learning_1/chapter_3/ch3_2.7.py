#ReLu 함수(Rectified Linear unit 렐루)
'''
입력이 0을 넘으면 입력을 드대로 출력
0이하이면 0을 출력

h(x)= x(x>0)
h(x)= 0(x<=0)
'''
import numpy as np

def relu(x):
    return np.maximum(0, x) #두 입력 중 큰 값을 선택해 반환(maximum)