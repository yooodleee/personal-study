#오차역전파backpropagation

'''
신경망의 가중치 매개변수의 기울기(정확히는 가중치 매개변수에 대한 손실 함수의 기울기)는\
수치 미분을 사용해 구했다.
수치 미분은 단순하고 구현하기도 쉽지만 계산 시간이 오래 걸린다는 게 단점이다.
-> 가중치 매개변수의 기울기를 효율적으로 계산하는 '오차역전파'!

1) 기계학습을 다루는 대부분의 책에서는 수식을 중심으로 이야기를 전개한다.

2) 계산 그래프를 사용해서 '시각적'으로 이해하는 방법도 있다.
'''
#계산 그래프computational graph
'''
계산 과정을 그래프로 나타낸 것.
-> 복수의 노드node와 에자edge로 표현된다(노드 사이의 직선을 '에자'라고 한다.)

1) 계산 그래프를 구성한다.

2) 그래프에서 계산을 왼쪽에서 오른쪽으로 진행한다.

*계산을 왼쪽에서 오른쪽으로 진행하는 단계=> 순전파forward propagation
-> 계산 그래프의 출발점부터 종착점으로의 전파.
-> 오른쪽에서 왼쪽으로의 전파가 역전파backward propagation
'''
#국소적 계산
'''
계산 그래프는 '국소적 계산'을 전파함으로써 최종 결과를 얻을 수 있다.
전체에서 어떤 일이 벌어지든 상관없이 자신과 관계된 정보만으로 결과를 출력할 수 있음을 의미한다.
-> 계산 그래프는 국소적 계산에 집중한다.
'''
#왜 계산 그래프로 푸는가?
'''
전체가 아무리 복잡해도 각 노드에서는 단순한 계산에 집중하여 문제를 단순화할 수 있다.
계산 그래프는 중간 계산 결과를 모두 보관할 수 있다.
실제 계산 그래프를 사용하는 가장 큰 이유는 역전파를 통해 '미분'을 효율적으로 계산할 수 있다.
'''
#연쇄 법칙chain rule
'''
역전파는 '국소적인 미분'을 순방향과 달리 오른쪽-> 왼쪽 방향으로 전달한다.
또한, 국소적 미분을 전달하는 원리는 '연쇄 법칙'에 따른 것이다.

*합성 함수

z=t**2
t=x+y

dz/dx=dz/dt*dt/dx   ->   dz/dt=2t, dt=dx=1

dz/dx=dz/dt*dt/dx=2t*1=2(x+y)

'''