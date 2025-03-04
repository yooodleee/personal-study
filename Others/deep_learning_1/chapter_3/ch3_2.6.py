#비선형 함수
'''
계단 함수-> 계단처럼 구부러진 직선 함수
시그모이드 함수-> 곡선 함수
동시에 비선형 함수.

*선형 함수-> 출력이 입력의 상수배만큼 변하는 함수-. 곧은 직선 하나
*비선형 함수-> 직선 1개로는 그릴 수 없음

신경망에선 비선형 함수를 사용한다.
선형 함수를 사용하면 층을 아무리 깊게 해도 '은닉층'이 없는 네트워크로도 똑같은 기능을 할 수 있다.

선형 함수 h(x)=cx를 활성화 함수로 사용한 3층 네트워크는\
y(x)=h(h(h(x)))=c*c*c*x=c^3*.
-> 은닉층이 없는 네트워크로 표현할 수 있다.
'''