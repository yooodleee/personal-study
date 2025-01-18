#Variable 클래스
import numpy as np
from dezero import Variable #(1)dezero 모듈에서 Variable 임포트

x_np=np.array(5.0)
x=Variable(x_np) #(2) Variable인스턴스 생성

y=3*x**2 #(3) 넘파이 다차원 배열처럼 사용
print(y)
#variable(75.0)

#미분을 수행하는 backward() 메서드
y.backward()
print(x.grad)
#variable(30.0)


#벡터의 내적과 행렬 곱 계산
import numpy as np
from dezero import Variable
import dezero.functions as F #(1)

#벡터의 내적
a=np.array([1, 2, 3])
b=np.array([4, 5, 6])
a, b=Variable(a), Variable(b) #생략 가능
c=F.matmul(a, b) #(2)
print(c)

#행렬 곱
a=np.array([[1, 2], [3, 4]])
b=np.array([[5, 6], [7, 8]])
c=F.matmul(a, b) #(3)
print(c)

# variable(32)
# variable([[19 22]
#           [43 50]])


#로젠브록 함수의 미분
import numpy as np
from dezero import Variable

def rosenbrock(x0, x1):
    y=100*(x1-x0**2)**2+(x0-1)**2
    return y
x0=Variable(np.array(0.0))
x1=Variable(np.array(2.0))

y=rosenbrock(x0, x1)
y.backward()
print(x0.grad, x1.grad)
#variable(-2.0) variable(400.0)


#경사 하강법을 적용한 로젠브록 함수의 미분(최솟값 구하기)
x0=Variable(np.array(0.0))
x1=Variable(np.array(2.0))

Iters=10000 #반복 횟수
Lr=0.001 #학습률

for i in range(Iters): #갱신 반복
    print(x0, x1)
    y=rosenbrock(x0, x1)

    #이전 반복에서 더해진 미분 초기회
    x0.cleargrad()
    x1.cleargrad()

    #미분(역전파)
    y.backward()

    #변수 갱신
    x0.data-=Lr*x0.grad.data
    x1.data-=Lr*x1.grad.data

print(x0, x1)