#미분

# def numerical_diff(f,x):  수치 미분 numerical_differentiation
#     h=1e-50
#     return (f(x+h)-f(x))/h    나쁜 구현의 예

'''
h에 가급적 작은 값을 대입하고 싶었기에(가능하다면 h를 0으로 무한히 가깝게 하고 싶으니)\
1e-50이라는 작은 값을 이용한다.
이 값은 0.00...1 형태에서 소수점 아래 0이 50개라는 의미이다.
-> 반올림 오차rounding error 문제를 일으킨다.
-> 반올림 오차는 작은 값(가령 소수점 8자리 이하)이 생략되어 최종 계산 결과에 오차가 생기게 된다.

np.float32(1e-50)
#0.0

너무 작은 값을 이용하면 컴퓨터로 계산하는 데 문제가 된다.
우선 이 미세한 값 h로 10^-4 정도의 값을 사용하면 좋은 결과를 얻는다고 알려져 있다.
함수 f의 차분(임의 두 점에서의 함수 값들의 차이)과 관련한 것이다.

'진정한 미분'은 x 위치의 함수의 기울기(접선)에 해당하지만, 
'''
def numerical_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)