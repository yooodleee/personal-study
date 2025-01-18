#항등 함수와 소프트맥스 함수 구현하기
'''
항등 함수identitiy function-> 입력을 그대로 출력한다.
입력과 출력이 항상 같다.
-> 출력층에서 항등 함수를 사용하면 입력 신호가 그대로 출력 신호가 된다.

분류에서 사용하는 소프트맥스 함수softmax function.
exp(x)는 e^x을 뜻하는 지수 함수exponential function이다.
n은 출력층의 뉴런 수, y^k는 그 중 k번째 출력임을 뜻함.
-> 분자는 입력 신호 a_k의 지수 함수, 분모는 모든 입력 신호의 지수 함수의 합으로 구성됨.

y_k=exp(a_k)/sigma exp(a_i)
'''
import numpy as np

a=np.array([0.3, 2.9, 4.0])

exp_a=np.exp(a) #지수함수(분자)
print(exp_a)
#[ 1.34985881 18.17414537 54.59815003]

sum_exp_a=np.sum(exp_a) #지수함수의 합(분모)
print(sum_exp_a)
#74.1221542101633

y=exp_a/sum_exp_a
print(y)
#[0.01821127 0.24519181 0.73659691]


#sofrmax 함수 구현
def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y