#소프트맥스 함수 구현 시 주의점
'''
소프트맥스는 컴퓨터로 계산할 떄 결함(오버플로우)이 있다.
소프트맥스 함수는 지수 함수를 사용하는데, 지수 함수는 계산의 괒ㅇ에서 아주 큰 값을 출력한다.
큰 값끼리 나눗셈을 하면 결과 수치가 '불안정'하다.

*오버플로우overflow
-> 컴퓨터 수를 4바이트나 8바이트와 같이 크기가 유한한 데이터를 다루는 것이 아니라\
표현할 수 있는 수의 범위를 넘어설 때 발생하는 문제점.

문제 해결을 위한 소프트맥스 함수 구현을 개선한다.

y_k=C*exp(a_k)/C*sigma exp(a_i)

    ={exp(a_k)+logC}/{sigma exp(a_i)+logC}

    =exp(a_k+C')/sigma exp(a_i+C')


C는 오버플로우를 막을 목적으로 입력 신호 중 최댓값을 이용하는 것이 일반적이다.
'''
import numpy as np

a=np.array([1010, 1000, 990])   
np.exp(a)/np.sum(np.sum(a)) #softmax-> 제대로 계산되지 않음
#array([nan,    nan,    nan])   not a number

c=np.max(a)   #c=1010(최댓값)   -> c를 빼주면 올바르게 계산할 수 있다.
print(a-c)
#array([    0,  -10,    -20])

z=np.exp(a-c)/np.sum(np.exp(a-c))
print(z)
#[9.99954600e-01 4.53978686e-05 2.06106005e-09]

def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y