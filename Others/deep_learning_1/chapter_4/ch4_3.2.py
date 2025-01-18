#수치 미분의 예(y=0.01*x^2+0.1*x)
def numerical_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)

def function_1(x):
    return 0.01*x**2+0.1*x

import numpy as np
import matplotlib.pylab as plt

x=np.arange(0.0, 20.0, 0.1) #0.0~20.0까지 0.1의 간격으로 배열 x를 만든다.
y=function_1(x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x,y)
plt.show()

z1=numerical_diff(function_1, 5)    #x=5일 때의 함수의 미분
print(z1)
#0.1999999999990898

z2=numerical_diff(function_1, 10)   #x=10일 때의 함수의 미분
print(z2)
#0.2999999999986347