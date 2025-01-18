#계단 함수 구현하기
import numpy as np

def step_function(x):
    if x>0:
        return 1
    else:
        return 0
    
def step_function_2(x):
    y=x>0
    return y.astype(np.int) #계단 함수는 0이나 1의 'int형'을 출력

x=np.array([-1.0, 1.0, 2.0])
print(x)