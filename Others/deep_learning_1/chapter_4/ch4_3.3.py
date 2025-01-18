#편미분(f(x_0, f_1)=(x_0)**2+(x_1)**2)
def function_2(x):
    return x[0]**2+x[1]**2
    #return np.sum(x**2)

'''
x는 넘파이 배열이라고 가정한다.
넘파이 배열의 각 원소를 제곱하고 그 합을 구할 뿐인 간단한 구현이다.
'''
#문제1:x_0=3, x_1=4일때, x_0에 대한 편미분 df/dx_0를 구하시오.
def numerical_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)

def function_tmp1(x0):
    return x0*x0+4.0**2.0

z1=numerical_diff(function_tmp1, 3.0)
print(z1)
#6.00000000000378


#문제2: x_0=3, x_1=4일때, x_1에 대한 편미분 df/dx_1를 구하시오.
def function_tmp2(x1):
    return 3.0**2.0+x1*x1

z2=numerical_diff(function_tmp2, 4.0)
print(z2)
#7.999999999999119

'''
편미분은 변수가 하나인 미분과 마찬가지로 특정 장소의 기울기를 구한다.
단, 여러 변수 중 목표 변수 하나에 초점을 맞추고 다른 변수는 고정한다.
-> 목표 변수를 제외한 나머지를 특정 값에 고정하기 위해 새로운 함수를 정의한다.
-> 새로 정의한 함수에 대해 수치 미분 함수를 적용해 편미분을 구한 것이다.
'''