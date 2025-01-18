#기울기
'''
x_0, x_1의 편미분을 동시에 계산하고 싶은 경우
x_0=3, x_1=4일 때, (x_0, x_1) 양쪽의 편미분을 묶어서 (df/dx_0, df/dx_1)\
-> 모든 변수의 편미분을 벡터로 정리한 것, 시울기gradient
'''
import numpy as np

def function_2(x):
    return x[0]**2+x[1]**2

def numerical_gradient(f,x):    #동작 방식은 변수가 하나일 때의 수치 미분과 거의 동일
    #함수의 인수인 f는 함수, x는 넘파이 배열이므로 x의 각 원소에 대해 수치 미분을 구한다.
    h=1e-4
    grad=np.zeros_like(x)   #x와 형상이 같은 배열 형성, 그 원소가 모두 0인 배열

    for idx in range(x.size):
        tmp_val=x[idx]

        #f(x+h) 계산  
        x[idx]=tmp_val+h
        fxh1=f(x)

        #f(x-h) 계산
        x[idx]=tmp_val-h
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val  #값 복원
    
    return grad

z1=numerical_gradient(function_2, np.array([3.0, 4.0]))
print(z1)
#[6. 8.]

z2=numerical_gradient(function_2, np.array([0.0, 2.0]))
print(z2)
#[0. 4.]

z3=numerical_gradient(function_2, np.array([3.0, 0.0]))
print(z3)
#[6. 0.]

'''
기울기의 의미-> 방향을 가진 벡터-> 함수의 '가장 낮은 최소값'
그 최소값에서 멀어질수록 벡터의 크기가 커진다.

기울기가 가리키는 쪽은 각 장소에서 함수의 출력 값을 가장 크게 줄이는 방향
'''