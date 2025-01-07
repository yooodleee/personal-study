#3장 연산자




#산술 연산자:사칙연산 기호를 사용함(+-*/)


print(1+1)
print(2-1)
print(5*12)
print(9/3) #결과는 3.0



print(2**3) #2의 3제곱:8
print(10%3) #10을 3으로 나눈 나머지인 1
print(10//3)
#정수와 정수의 나누기 결과로 정수값을 얻으려면 //을 사용한다->우리가 원하는 정수 형태의 결과




#비교 연산자:부등호(>,>=,<,<=)


print(10>3) #True
print(4>=7) #False
print(10<3) #False
print(5<=5) #True

#비교 연산자 ==:같다(파이썬에서는 등호를 같다는 의미가 아니라 값을 대입한다는 의미!)
#비교 연산자 !=:다르다

print(3==3) #True
print(4==2) #False
print(3+4==7) #True
print(1!=3) #True


#논리 연산자

'''
수식, 조건 등이 참인가 거짓인가를 판별
and:둘다 모두 참이면 참
or:둘 중 하나라도 참이면 참
not:값이 참이면 거짓, 거짓이면 참(반대로 출력)
'''

print((3>0)and(3>5)) #False, (3>0)은 참이지만 (3>5)는 거짓이므로 False
print((3>0)or(3>5)) #True, (3>0)이 참 둘 중 하나라도 참이면 참을 출력
print(not(1!=3)) #False, 1은 3이 아니다는 참이지만 논리 연산자 not을 만나 True의 반대값 False를 출력


'''
단축 평가(short circuit evaluation)

논리 연산자 and와 or는 앞의 연산 결과에 따라 뒤의 연산이 수행되지 않을 수도 있다.
and 연산자는 앞뒤 연산이 모두 참일 때 Ture가 된다.
그래서 앞의 연산이 이미 False라면 뒤의 연산은 결과가 참이건 거짓이건 상관없으므로 수행되지 않는다.

or연산자는 앞뒤 연산 중 하나라도 참일 때 True가 되는데 앞의 연산이 이미 True라면\
뒤의 연산은 하지 않아도 상관없으므로 수행되지 않는다.
'''

print(5>4>3)
#5>4는 참이므로 다음 수식을 확인한다, 4>3도 참이므로 결과는 True

print(4>5>3)
#4>5는 거짓이므로 뒤의 연산 결과에 상관없이 False가 된다.
#뒤의 수식을 수행하지 않고 결과를 출력함(참고로 a>b>c는 a>b and b>c와 같다)




#연산자의 우선순위

print(2+3*4) #14
print((2+3)*4) #20

#모든 연산자에 대한 우선순위를 외울 필요는 없다.중요한 몇 가지만 알고 나머지는 필요할 때 확인하면 된다.
#다음의 연산자는 아래로 갈수록 우선순위가 낮아진다.

'''
 [], {}, (): 리스트, 딕셔너리, 세트, 튜플
 **:거듭제곱
 *, /, //, %: 곱셈, 나눗셈, 정수 나눗셈, 나머지
 +,-: 덧셈, 뺄셈
 not, in, <, <=, >, >=, !=, ==: 부정, 비교 연산자
 and, or: 논리 연산자
 =: 대입 연산자

'''

#변수로 연산하기

number=2+3*4
print(number)
number=2+3*4+2
print(number) #16

number=2+3*4
print(number)
number=number+2 #(2+3*4)+2와 결과는 같다, number를 다시 정의하는 과정인데 코드가 짧아진다.(변수로 연산하기)
print(number) #16

#복합 대입 연산자(augmented assignment operator):대입 연산자와 산술 연산자를 합침

'''
 +=:왼쪽 값에 오른쪽 값을 더한 후 왼쪽 값에 대입-> number=number+2-> number+=2
 -=:왼쪽 값에 오른쪽 값을 뺀 후 왼쪽 값에 대입-> number=number-2-> number-=2
 *=:왼쪽 값에 오른쪽 값을 곱한 후 왼쪽 값에 대입-> number=number*2 -> number*=2
 /=:왼쪽 값에 오른쪽 값을 나눈 후 왼쪽 값에 대입-> number=number/2-> number/=2
 **=:왼쪽 값에 오른쪽 값을 거듭제곱한 후 왼쪽 값에 대입-> number=number**2-> number**=2
 //=:왼쪽 값에 오른쪽 값을 나눈 후 몫을 왼쪽 값에 대입-> number=number//2-> number//=2
 %=:왼쪽 값에 오른쪽 값을 나눈 후 나머지를 왼쪽 값에 대입-> number=number%2-> number%=2
'''

number=2+3+4
print(number) #9
number+=2
print(number) #number=number+2와 동일, 11

number-=2 #number=number-2, 9
print(number)
number*=2 #number=number*2, 18
print(number)
number/=2 #number=number/2, 9.0
print(number) 
number**=2 #number=number**2, 81.0
print(number) 
number//=2 #number=number//2, 40.0
print(number)
number%=2 #number=number%2, 0.0
print(number)



#함수로 연산하기, 함수(function):특정 기능을 수행하도록 미리 만들어 둔 명령어

#숫자 처리 함수

'''
abs(x):x의 절댓값
pow(x,y):x를 y만큼 거듭제곱한 값
max():가장 큰 값
min():가장 작은 값
round(x,d):x를 반올림한 값, d는 표시할 소수점 이하 자릿수, d가 없으면 소수점 이하 첫째 자리에서 반올림한 정수
'''

print(abs(-5)) #-5의 절댓값, 5
print(pow(4,2)) #4의 2제곱, 16
print(max(5,12)) #가장 큰 값, 12
print(min(5,12)) #가장 작은 값, 5
print(round(3.14)) #3.14를 소수점 이하 첫째 자리에서 반올림한 정수, 3
print(round(4.687, 2)) #4.687을 소수점 이하 셋째 자리에서 반올림한 값, 4.69


#math 모듈, 모듈(module)

'''
어떤 기능을 하는 코드를 모아 놓은 파이썬 파일을 의미함
직접 만들수도 있고 파이썬에 이미 만들어져 있는 모듈을 가져와서 사용할 수도 있음

프로그램에 모듈의 기능을 가져다 쓰려면 사용하기 전에 다음 형태의 구문을 추가해야 함
형식:from 모듈명 import 기능, 기능 부분에 *를 넣으면 모듈 안 모든 기능을 가져다 쓰겠다는 의미

Tip:*는 와일드카드 문자(Wildcard character)로, 모든 것을 지칭할 때 사용함
예를 들어 윈도우 탐색기에서 파일을 검색할 때 검색창에 *.png를 입력하면 확장자가 png인 모든 파일(예: desk,png, book.png)을,\
py*.txt로 입력하면 py로 시작하고 확장자가 txt인 모든 파일(예:python.txt, pyper.txt)을 검색함

floor():내림
ceil():올림    가우스가 생각나는 이유?ㅎ
sqrt():제곱근 
'''

from math import * #math 모듈의 모든 기능을 가져다 쓰겠다는 의미

result=floor(4.99) #4.99의 내림, 4
print(result) 
result=ceil(3.14) #3.14의 올림, 4
print(result)
result=sqrt(16) #16의 제곱근, 4.0
print(result)

'''
모듈의 기능을 가져다 쓸 떄 구문을 다음과 같이 작성해도 된다.

import 모듈명

단, 이 방법을 사용할 때는 기능 앞에 기능이 속한 모듈명을 점(.)으로 연결해서 적어야 함
'''

import math #math 모듈의 기능을 가져다 쓰겠다는 의미

result=math.floor(4.99) #math.을 함께 작성, 4
print(result)
result=math.ceil(3.14) #4
print(result)
result=math.sqrt(16) #4.0
print(result)



#random 모듈:파이썬에서 제공하는 함수 중에 무작위로 숫자를 뽑아 주는 함수

from random import * #random 모듈의 모든 기능을 가져다 쓰겠다는 의미

print(random())
print(random())
print(random())

'''
실행 결과가 모두 0이상 1미만 사이의 수를 출력함, 실행될 때마다 매번 다른 수가 출력됨
->random() 함수는 0이상 1미만(1을 불포함)에서 난수를 뽑는 기능을 함
'''

'''
Note:from random import*에 밑줄이 생기면서 "Unused import(s) ..."라는 경고문은 왜 뜨는 걸까?

VsCode에 파이썬 코드를 분석하는 Pylint라는 확장 프로그램이 설치돼 있을 때 나타날 수 있는 경고문으로,\
현재 작성 중인 코드 안에서 random 모듈의 모든 기능을 사용하지 않으므로 필요한 부분만 가져다 쓰도록 안내하는 거임

예를 들어, 작성 중인 코드에서 random(), randint()함수만 필요하다면 다음과 같이 코드를 작성하면 경고가 사라진다.
'''

from random import random, randint #random 모듈의 random(), randint() 함수를 가져다 쓰겠다는 의미

#프로그램에서 사용하는 기능만 가져다 쓰면 좋겠지만, 어느 기능을 쓸지 명확하지 않다면 입문 단계에서는 *로 작성해도 좋다.

print(random()*10)
#0.0 이상 10.0 미만에서 난수 생성
print(int(random()*10))
#0이상 10 미만 정수에서 난수 생성(random() 결과를 int()로 감싸서 정수로 변환)
print(int(random()*10)+1)
#1이상 11 미만 정수에서 난수 생성(random() 결과를 정수로 변환해 1을 더함)



#예를 들어, 1~45까지 정수 범위 안에서 로또 번호를 뽑으려면 다음처럼 작성함.

print(int(random()*45)+1)

'''
random() 함수로 생성한 난수에 45를 곱해 0.0 이상 45.0 미만인 난수를 생성함.
그리고 이를 int()로 감싸서 정수로 변환하고 여기에 1을 더함.그러면 1이상 46미만인 정수에서 난수를 생성함

그런데 범위를 매번 계산하려면 매우 귀찮겠지...random 모듈에는 원하는 범위 안에서 난수를 뽑을 수 있는 함수들이 있음

randrange(시작 숫자, 끝 숫자):주어진 범위 안에서 정수인 난수 생성(끝 숫자 미포함)
randint(시작 숫자, 끝 숫자):주어진 범위 안에서 정수인 난수 생성(끝 숫자 포함)
'''

print(randrange(1,46)) #1이상 46 미만에서 난수 생성
print(randint(1,45)) #1이상 45 이하에서 난수 생성

#만약 6번 반복하면 중복된 결과값이 나올 수도 있다.각 문장은 서로 영향을 주지 않는 독립 사건이기 때문이다.

print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

#이럴 때는 random 모듈에서 제공하는 sample() 함수를 이용하면 된다.




#실습 문제: 스터디 날짜 정하기

'''
조건:날짜를 무작위로 뽑는다/ 월별 일수가 다르므로 최소 일수인 28일 이내로 정한다(28일까지만 날짜 선정)
매월 1~3일은 스터디를 준비해야 하므로 제외한다
실행 결과: 오프라인 모임 날짜는 매월 18일로 선정됐습니다.
'''

from random import *

date=randint(4,28) #4~28일 중에서 무작위 날짜 뽑기, randint로 뽑은 정수를 date 변수에 저장함
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정됐습니다.")
#문자열과 숫자를 함께 출력해야 하므로 str()로 date 변수를 감싸서 문자열로 형변환해야 하는 점을 주의하자!


#자율 학습


'''
조건:월과 날자를 무작위로 뽑는다/월별 일수가 다르므로 최대 일수 31일 이내로 정한다.
로또 번호는 1~45이내의 정해진 범위 내에서만 6자리를 출력함
실행 결과: "2024년 1월 11일 로또 당첨 번호는 6,5,45,7,31,12 입니다!"
'''

from random import *

month=randint(1,12)
date=randint(1,31)

number1=randint(1,45)
number2=randint(1,45)
number3=randint(1,45)
number4=randint(1,45)
number5=randint(1,45)
number6=randint(1,45)

print("2024년 "+str(month)+"월 "+str(date)+"일 로또 당첨 번호는 "+str(number1)+",\
      "+str(number2)+", "+str(number3)+", "+str(number4)+", "+str(number5)+", "+str(number6)+" 입니다!")


#셀프 체크

#연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보시오

#조건:섭씨 온도를 저장하기 위한 변수를 만든다/화씨 온도=(섭씨 온도*9/5)+32/섭씨 온도와 화씨 온도를 출력한다
#실행 결과: 섭씨 온도=30, 화씨 온도:86.0, 섭씨 온도:10 화씨 온도 50.0

celsius=30
fahrenheit=(celsius*9/5)+32
print("섭씨 온도 : "+str(celsius))
print("화씨 온도 : "+str(fahrenheit))
