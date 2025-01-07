#10장 예외 처리




#10.1 예외 처리하기


#10.1.1 예외 처리란

'''
예외(exception)

예상치 못한 실수 또는 잘못된 무언가를 오류(error)라고 하며\
오류 상황에 대처하는 것을 예외 처리라고 한다.

프로그램에서도 굉장히 많은 오류 상황이 발생할 수 있다.
이를 어떻게 처리하느냐에 따라 완성도가 높고 사용하기 편리한 프로그램이 되거나\
갑자기 응답 없음 상태로 있다가 강제 종료돼서 모든 작업이 수포로 돌아가는 프로그램이 될 수도 있다.
'''

#10.1.2 예외 처리하기: try-except문

'''
다음은 사용자로부터 두 수를 입력받아 나누기한 결과를 출력하는 계산기 프로그램이다.
'''

print("나누기 전용 계산기입니다.")
num1=int(input("첫 번째 숫자를 입력하세요 : "))
num2=int(input("두 번째 숫자를 입력하세요 : "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

'''
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 삼

Traceback (most recent call last):
  File "c:/Users/dhals_zn0ga5j/OneDrive/바탕 화면/PythonWorkspace/ch10.py", line 30, in <module>
    num2=int(input("두 번째 숫자를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: '삼'
PS C:\Users\dhals_zn0ga5j\OneDrive\바탕 화면\PythonWorkspace>

삼을 입력하고 나니 오류 메시지를 출력하고 프로그램을 종료한다.
나누기 연산 부분을 보면 입력받은 두 값을 나누기 연산(num1/num2)하고 이를 다시 int()로 감싸서\
(int(num1/num2)) 정수형으로 변환한다.
그런데 입력한 삼은 정수로 변환할 수 없는 문자라서 오류가 발생한다.

오류 메시지를 보면 'ValueError'라는 오류 종류와 함께 상세한 설명을 함께 출력한다.
ValueError는 값이 잘못돼서 발생하는 오류이다.
이에 대한 예외 처리를 해보자.

오류가 발생할 때 예외 처리는 다음 형식으로 작성한다.
형식
try:
    실행할 명령1
    실행할 명령2
    ...
except:
    예외 처리 명령1
    예외 처리 명령2
    ...

먼저 실행하려는 코드 위에 try 키워드를 적고 뒤에 콜론을 붙인다.
그리고 실행하려는 코드를 모두 들여써서 try 문의 하위 명령문으로 작성한다.
그 아래 except 키워드를 적고 뒤에 어떤 오류에 대한 예외 처리인지를 명시한다.(여기서는 ValueError에 대한 처리)

이제 try 문의 하위에 있는 명령문을 실행하다 오류가 발생하면 프로그램을 종료하지 않고\
except 문의 오류 종류와 일치하는지 확인한다.
일치하면 except 문의 하위 명령문들이 실행된다.
만약 오류가 발생하지 않으면 except 문은 실행하지 않고 넘어간다.
'''

try:
    print("나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, (num1/num2)))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")

'''
이번엔 삼을 입력해보자.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 삼
오류 발생! 잘못된 값을 입력했습니다.

오류 메시지 대신 except 부분의 print() 문이 실행된다.
'''


#10.1.3 오류 메시지를 예외 처리로 출력하기: as


try:
    print("나누기 전용 계산기입니다.")
    num1=int(input("첫 분째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, (num1/num2)))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")

'''
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 0
Traceback (most recent call last):
  File "c:\PythonWorkspace\ch10.py", line 5, in <module>
    num2=int(input("두 번째 숫자를 입력하세요 : "))
ZeroDivisionError: division by zero

6과 0을 입력했을 때 오류 메시지가 뜨면서 프로그램을 종료한다.
메시지는 ZeroDivisionError가 나온다.-> 두 번째 값, 즉 나누기 수로 0을 넣어서 발생하는 오류
수학에서 어떤 수든 0으로 나눌 수 없다.

이번에는 ValueError와는 다른 종류의 오류라서 기존 except 문만으로는 예외 처리를 할 수 없다.
오류마다 각각 except 문을 추가해 예외 처리를 따로 해야 한다.

그런데 예외 처리마다 메시지를 직접 작성하는 것은 귀찮은 일이다.
이번에는 오류가 발생할 때 표시하는 오류 메시지를 가져와 출력하도록 예외 처리를 한다.
이를 위해 예외 처리 형식에서 except 뒤에 as 키워드와 변수명을 추가한다.
이와 같은 형식으로 작성하면 as 뒤에 지정한 변수명으로 오류 메시지를 확인할 수 있다.

형식
try:
    실행할 명령1
    실행할 명령2
    ...
except 오류 종류1
    예외 처리 명령1
    예외 처리 명령2
    ...
except 오류 종류2 as 변수명:
    예외 처리 명령1
    예외 처리 명령2
    ...

앞의 코드에 ZeroDivisionError에 대한 예외 처리를 추가해보자.
ZeroDivisionError에 대한 except 문을 작성하고 뒤에 as 키워드와 err이라는 이름의 변수를 넣고 콜론을 붙인다.
그리고 변수를 print() 문으로 출력한다.
'''

try:
    print("나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, (num1/num2)))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)

'''
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 0
division by zero    #예외 처리 전에 발생한 오류 메시지 중 ZeroDivisionError: 뒤에 나오는 내용

이처럼 어떤 문제인지 쉽게 알아볼 수 있는 메시지가 제공되는 오류는 따로\
예외 처리 메시지를 정의하지 않고도 간편하게 예외 처리를 할 수 있다.
'''

'''
이번엔 try 구문을 수정해보자.
먼저 nums라는 리스트를 추가로 정의한다.
두 수를 입력받는 부분은 같은데, 입력받은 두 수를 변수가 아닌 nums 리스트에 저장한다.
그리고 두 수를 연산한 결과도 리스트에 저장한다.
그런 다음 print() 문으로 리스트 값을 순서대로 출력한다.
'''

try:
    print("나누기 전용 계산기입니다.")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) #nums[0]
    nums.append(int(input("두 번째 숫자를 입력하세요 : "))) #nums[1]
    nums.append(int(nums[0]/nums[1]))   #연산 결과를 리스트에 추가, nums[2]
    print("{0} /{1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)

'''
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 0
6 / 3 = 2

만약 연산 결과를 리스트에 추가하는 부분을 코드에 넣지 않는다면?
'''

try:
    print("나누기 전용 계산기입니다.")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError(err):
    print(err)

'''
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 3

Traceback (most recent call last):
    File "c:\PythonWorkspace\ch10.py", line 7, in <module>
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
IndexError: list index out of range

동일하게 6과 3을 입력하니 이번에는 IndexError가 발생한다.
오류 메시지를 보면 리스트의 인덱스 범위를 벗어났다고 나온다.
현재 리스트에 입력받은 두 수 ([6, 3])만 들어 있어서 인덱스는 0, 1만 있다.
그런데 format() 함수로 nums[2]에 접근하려고 해서 발생하려는 오류이다.

ValueError나 ZeroDivisionError 때처럼 IndexError 구문을 추구하면 예외 처리를 할 수 있다.
그런데 이렇게 모든 오류에 대한 예외 처리를 프로그램 안에 작성하려면 코드가 한없이 길어진다.
그래서 코드 마지막에 다음과 같이 구문을 추가하면 지금까지 정의하지 않은 모든 오류를 예외 처리할 수 있다.
'''

try:
    print("나누기 전용 계산기입니다.")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError(err):
    print(err)
except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err)

'''
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 3
알 수 없는 오류가 발생했습니다.
list index out of range
'''

'''
*추가 개념. 예외 처리 클래스

ValueError, ZeroDivisionError, IndexError는 예외 처리를 위해 파이썬에 미리 정의되어 있는 클래스다.
이외에도 변수명이 없을 때 발생하는 NameError, 문법 오류가 있을 때 발생하는 SyntaxError, \
접근하려는 파일이 없을 때 발생한는 FileNotFoundError 등 다양한 클래스가 있다.
마지막에 사용한 Exception은 앞에 나온 예외 처리 클래스들의 부모 클래스다.

예외 처리 클래스를 모두 외울 필요는 없으며 오류가 발생할 수 있는 상황을 마주했을 때 적절한 예외 처리를 하면 된다.
'''



#10.2 오류 발생시키기


'''
지금까지 발생한 오류는 모두 어떨 때 오류가 발생하는지 파이썬에 형태가 미리 정의돼 있었다.
그런데 직접 작성한 프로그램에서 허용하지 않는 동작을 하려고 할 때도 의도적으로 오류를 발생시킬 수 있다.

형식
raise 오류 종류

계산기 프로그램을 수정해 한 자리 숫자끼리만 나누기를 할 수 있게 해보자.
나누기를 하기 전에 사용자로부터 입력받은 값들이 한 자리 숫자가 맞는지 확인한다.
그리고 조건에 맞지 않을 때, 즉 입력받은 숫자가 10 이상일 때는 의도적으로 ValueError를 발생시켜 except 문에서 예외 처리한다.
'''

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:    #입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 2
6 / 2 = 3

한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.

if 문에 의해 ValueError가 발생하고 이에 따라 예외 처리 구문이 실행돼 print() 문의 내용을 출력함
'''




#10.3 사용자 정의 예외 처리하기


'''
사용자가 직접 오류를 정의해 예외 처리하는 경우도 있다.

앞에서 만든 한 자리 숫자 나누기 프로그램에서 두 자리 이상의 수로 잘못 입력했을 때\
사용자 입력 중 어디가 잘못됐는지를 알려 주도록 코드를 수정해보자.
만자 두 자리 이상의 수를 입력할 때 발생하는 오류라는 의미로 BigNumberError라는 클래스를 만든다.
그리고 코드에서 새로운 오류를 정의해 예외 처리하려면 파이썬에 포함된 Exception이라는 클래스를 상속해야 한다.

그러면 앞에서 봤던 ValueError, IndexError와 비슷하게 사용자가 필요한 형태의 오류를 직접 정의해 처리할 수 있다.
클래스 내용은 일단 pass 문으로 둔다.

입력값이 10 이상인지를 확인하는 if 문에서 ValueError 대신 새롭게 정의한 BisNumberError를 발생시키고,\
except 문을 추가해 예외 처리한다.
'''

class BigNumberError(Exception):    # 사용자 정의 예외 처리, Exception 클래스 상속
    pass
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:    #입력받은 수가 한 자리인지 확인
        #raise ValueError
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError:  #사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
오류가 발생했습니다. 한 자리 숫자만 입력하세요.

프로그램을 실행하고 10과 5를 순차적으로 입력하면 BigNumberError가 발생하고\
예외 처리가 실행돼서 마지막에 추가한 Except 문의 안내 문구를 출력한다.
이 상태로는 ValueError와 큰 차이가 없다.

이번에는 BigNumberError 클래스를 완성해보자.
pass 문 대신 __init__() 생성자와 __str__() 메서드를 추가한다.
생성자에는 오류 메시지를 의미하는 msg를 전달받아 인스턴스 변수로 설정하고,\
__str__() 메서드에는 인스턴스 변수 msg를 반환하게 한다.
이제 BigNumberError를 발생시킬 때 필요한 문구를 추가해 더 자세한 오류 내용을 출력할 수 있다.
'''

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return self.msg

'''
오류가 발생하는 시점에 어떤 값을 입력했는지 출력해보자.
try 문에서 BigNumberError를 발생시키는 부분에 입력받은 두 값을 문자열 형태로 넣는다.
이 문자열은 __init__() 생성자의 msg로 들어가게 된다.
그런 다음 __str__() 메서드에 의해 msg 인스턴스 변수가 반환된다.
그리고 except 문에서는 as를 이용해 err이라는 이름으로 반환된 오류 내용을 받고 이를 print() 문으로 출력한다.
'''

class BigNuberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        #자세한 오류 메시지
        raise BigNuberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNuberError as err:    #사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)  #오류 메시지 출력

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
오류가 발생했습니다. 한 자리 숫자만 입력하세요.
입력값: 10, 5

프로그램을 실행하고 10과 5를 입력하면 이제는 오류 내용과 함께 사용자가 어떤 값을 입력했는지도 출력한다.

사실 BigNumberError 클래스의 __init__() 생성자와 __str__() 메서드를 따로 정의하지 않고\
그냥 pass로 두어도 동일하게 작동하지만 생성자에서 추가로 어떤 작업을 해야 한다거나 __str__() 메서드에서\
오류 메시지를 오류 코드와 함께 출력하고 싶은 경우에는 코드를 수정하면 된다.
가령 프로그램에 오류 코드를 다음과 같이 정의한다면 BigNumberError에서는 오류 코드 001을 출력하면 된다.

[001: 두 자리 숫자가 입력됨]

[002: 문자열이 입력됨]

[003: 공백이 입력됨]

코드에 반영하면 다음과 같다.
'''

class BigNuberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return "[오류 코드 001]" + self.msg #오류 메시지 가공

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        #자세한 오류 메시지
        raise BigNuberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNuberError as err:    #사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)  #오류 메시지 출력

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
오류가 발생했습니다. 한 자리 숫자만 입력하세요.
[오류 코드 001] 입력값 : 10, 5
'''

'''
*추가 개념. 스페셜 메서드(special method)

__init__()나 __str__()처럼 이름 앞뒤로 언더바가 2개씩 붙은 형태의 메서드
또는 언더바가 2개 들어간다는 의미에서 던더 메서드(dunder method:double underscore method)라고도 함
특별한 역할을 수행하기 위해 별도 처리하는 메서드
__init__() 메서드는 객체가 생성될 때 자동을 호출되고, __str__() 메서드는 print() 함수로 객체를 출력할 때 호출된다.

다음과 같이 코드를 작성해보자.
'''

class SpecialClass():
    def __init__(self):
        print("특별한 생성자")
    
    def __str__(self):
        print("특별한 메서드")

s=SpecialClass()    #특별한 생성자 출력
print(s)    #특별한 메서드 출력

'''
특별한 생성자
특별한 메서드

실행결과를 보면 객체가 생성될 때 자동으로 __init__() 메서드가 호출되어 특별한 생성자가 출력된다.
그리고 print() 함수로 객체 s를 출력하면 __str__() 메서드가 호출되어 특별한 메서드가 출력된다.
이외에도 객체 길이를 구할 때 호출되는 __len__(), 객체가 특정 요소를 포함하는지 확인할 때는 __contains__() 등이 있다
'''




#10.4 오류와 상관없이 무조건 실행하기: finally


'''
finally는 try 문에서 오류가 발생하든 말든 try 문을 벗어나는 시점에 무조건 실행되는 구문
finally는 try와 except로 이루어진 구문의 가장 밑에 정의한다.

형식
try:
    실행할 명령1
    실행할 명령2
    ...
except 오류 종류1:
    예외 처리 명령1
    예외 처리 명령2
    ...
except 예외 종류2:
    예외 처리 명령1
    예외 처리 명령2
    ...
finally:
    실행할 명령1
    실행할 명령2
    ...

앞에서 만든 계산기 프로그램에 finally 문을 추가해보자.
계산기를 이용하는 사람 모두에게 감사하다는 인사 메시지를 출력한다.
'''

class BigNuberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise BigNuberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNuberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:    #오류 발생 여부와 상관없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")

'''
*정상 값 입력일 때

한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 2
6 / 2 = 3
계산기를 이용해 주셔서 감사합니다.

*오류 값 입력일 때

한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
오류가 발생했습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
계산기를 이용해 주셔서 감사합니다.
'''

'''
프로그램을 실행하고 한 자리 수인 6과 2를 입력하면 계산 결과와 함께 finally 문에 정의한 print() 문을 실행한다.
다시 실행해서 오류가 발생하도록 10과 5를 순서대로 입력한다.
오류가 발생하고 한 자리 숫자만 입력하라는 오류 메시지와 함께 이번에도 fianlly 문이 실행되는 것을 볼 수 있다.

이와 같이 try 문의 마지막에 finally 문을 추가해서 오류 발생 여부와 상관없이 항상 실행되는 코드를 작성할 수 있다.
보통 try 문에서 파일이나 자원을 사용할 때 finally 문에서 열린 파일을 닫거나 자원을 해제하는 작업을 수행한다.
그러면 프로그램이 실행되는 과정에서 오류가 발생하고 예외 처리가 제대로 되지 않더라도 자원은 정상적으로 해제할 수 있다.
'''




#10.5 실습 문제: 치킨 주문하기


'''
*문제:손님들의 대기 시간을 줄이고자 자동 주문 프로그램을 만들었다.
    다음 코드를 확인하고 적절한 예외 처리 구문을 추가하라.

    while True:
    print("[남은 치킨 : {0}]".format(chicken))
    order=int(input("치킨을 몇 마리 주문하시겠습니까?"))
    if order>chicken:   #남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, chicken))
        waiting+=1  #대기번호 1증가
        chicken-=order  #주문 수만큼 치킨 감소

*조건
    1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리한다.
    대기 손님이 주문할 수 있는 최대 주문량은 10마리로 제한한다.
    치킨 소진 시 오류(SoldOutError)를 발생시키고 프로그램 종료한다.
'''

class SoldOutError(Exception):  #(3) 재고 소진 시 발생할 오류 정의
    pass

chicken=10  #남은 치킨 수
waiting=1   #대기번호, 1부터 시작

while True:
    try:    #(1) 예외 처리를 위한 try 문 추가
        print("[남은 치킨 : {0}]".format(chicken))
        order=int(input("치킨을 몇 마리 주문하시겠습니까?"))
        if order>chicken:   #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order<=0:  #(2) 입력값이 1보다 작은 수일 때
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, chicken))
            waiting+=1  #대기번호 1증가
            chicken-=order  #주문 수만큼 치킨 감소
        if chicken==0:  #(4) 남은 치킨 수가 0이면
            raise SoldOutError  #(4) 재료 소진으로 주문이 불가능하므로 오류 발생
    except ValueError:  #(1) ValueError 예외 처리
        print("잘못된 값을 입력했습니다.")
    except SoldOutError:    #(4) 재료 소진 시 발생하는 오류의 예외 처리
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break

'''
*해설

주어진 코드를 살펴보면 먼저 남은 치킨 수(chicken)와 대기번호(waiting)를 각각 10마리와 1번으로 초기화합니다.
반복문 안에서 사용자로부터 치킨을 주문받고 주문 수가 남은 치킨 수를 초과하면 "재료가 부족합니다."를 출력합니다.
그렇지 않은 경우에는 대기 번호 몇 번인 손님이 치킨을 몇 마리 주문했는지 출력한다.
그런 다음 대기번호는 1 증가시키고, 남은 치킨 수는 주문 수만큼 감소시킨다.

코드를 실행하면서 작동 원리를 살펴보자.
처음에는 치킨이 10마리 있으므로 5를 입력하고 enter를 눌러 5마리를 주문한다.

[남은 치킨 : 10]
치킨을 몇 마리 주문하시겠습니까? 5
[대기번호 1] 5마리를 주문했습니다.
[남은 시간 : 5]
치킨을 몇 마리 주문하시겠습니까?

대기번호 1번 손님이 치킨 5마리 주문했다는 문구가 나오고 남은 치킨은 5마리로 줄어들어 출력된다.
아직 치킨이 남아 있어서 다시 반복문이 실행되고 계속해서 주문을 받는다.
2마리를 더 주문해보자.2를 입력하고 enter를 누른다.

(생략)
[남은 치킨 : 5]
치킨을 몇 마리 주문하시겠습니까? 2
[대기번호 2] 2마리를 주문했습니다.
[남은 치킨: 3]
치킨을 몇 마리 주문하시겠습니까?

대기번호가 1 증가해 2가 되고 남은 치킨은 3마리로 줄어든다.
마지막으로 남은 치킨 수를 초과해 10을 입력해본다.

(생략)
[남은 치킨 : 3]
치킨을 몇 마리 주문하시겠습니까? 10
재료가 부족합니다.
[남은 치킨 : 3]
치킨을 몇 마리 주문하시겠습니까?

치킨이 3마리 남았는데 10마리 주문이 들어오니 재료가 부족하다는 메시지와 함께 남은 치킨 수는 그대로다.
정상적인 동작이다.
0마리를 주문하면 어떨까?

(생략)
[남은 치킨 : 3]
치킨을 몇 마리 주문하시겠습니까? 0
[대기번호  3] 0마리를 주문했습니다.
[남은 치킨 : 3]
치킨을 몇 마리 주문하시겠습니까?

0마리인데도 주문했다는 문구가 뜬다.
그러면 -1을 입력해보자.

(생략)
[남은 치킨 : 3]
치킨을 몇 마리 주문하시겠습니까? -1
[대기번호 4] -1마리를 주문했습니다.
치킨을 몇 마리 주문하시겟습니까? 10마리

남은 치킨이 4마리로 늘어나는 문제가 발생한다.
마지막으로 한글로 주문해보자.
10마리를 입력해본다.

(생략)
치킨을 몇 마리 주문하시겠습니까? -1
[대기번호 4] -1마리를 주문했습니다.
[남은 치킨 : 4]
치킨을 몇 마리 주문하시겠습니까? 10마리

Traceback (most recent call last)"
File "c:\PythonWorkspace\ch10.py", line6, in <module>
    order = int(input("치킨을 몇 마리 주문하시겠습니까?))
ValueError: invalid literal for int() with base 10: '10마리'

ValueError가 발생하면서 프로그램이 비정상적으로 종료한다.
이와 같이 잘못된 값이 입력됐을 때 남은 치킨 수가 0이 됐을 때 예외 처리를 작성하면 된다.


(1) 조건 1에서 1보다 작거나 숫자가 아닌 값이 입력될 때 ValueError로 예외 처리를 해야 하므로\
    코드를 try-except 문 사이에 넣는다.
    이때 while 문까지 통째로 넣으면 잘못된 값이 입력될 때 while 문 밖에 있는 except 문에서 예외 처리돼\ 
    프로그램이 바로 종료된다.
    그래서 잘못된 값을 입력하더라도 반복문이 계속 실행되도록 while 문 내부 코드만 try-except 문으로 감싼다.

(2) 여기까지 작성하면 숫자가 아닌 값을 입력했을 때 입력값을 정수형으로 변환하는 int(input(...)) 부분에서\
    오류가 발생하므로 except 문에서 예외 처리를 한다.
    하지만 '1보다 작거나'에 해당하는 조건이 처리되지 않았으므로 코드를 보완한다.
    입력값을 정수로 변환한 후 if 문으로 비교하므로 입력값이 1보다 작은 경우는 이 부분을 수정하면 된다.
    if 문에서 남은 치킨보다 주문량이 많은 경우(order<chicken)를 제외한 모든 경우는 else 문에서 정상 주문으로 처리된다.
    그 사이에 elif 문을 추가해 입력값이 1보다 작은지 비교하고 1보다 작으면 ValueError를 발생시킨다.

(3) 조건 1을 모두 처리했으니 조건 2, 3을 살펴보자.
    대기 손님이 주문할 수 있는 치킨은 총 10마리이므로 남은 치킨 수가 0이 되면 SoldOutError를 발생시키고\
    안내 문구를 출력한 후 프로그램을 종료한다.
    먼저 코드 가장 윗줄에 사용자 정의 오류인 SoldOutError 클래스를 정의한다.
    세부 동작은 구현하지 않고 pass로만 작성한다.

(4) 이제 while 문 안에서 남은 치킨 수가 0이 됐을 때 SoldOutError가 발생하면 된다.
    기존 if-else 문 아래에 새로운 if 문을 추가한다.
    그리고 SoldOutError를 처리하기 위한 except 문을 추가하고 조건 3에 제시한 안내 문구를 출력하도록\
    print() 문을 작성한다.
    또한, 더 이상 주문을 받을 수 없으므로 break로 while 문을 탈출해 프로그램을 종료하게 한다.


(생략)
[남은 치킨 : 2]
치킨을 몇 마리 주문하시겠습니까? 삼
잘못된 값을 입력했습니다.
[남은 치킨 : 2]
치킨을 몇 마리 주문하시겠습니까? 

프로그램이 비정상적으로 종료되지 않고 계속 주문을 받는다.
예외 처리를 적용해 탄탄하고 신뢰할 수 있는 좋은 프로그램을 완성할 수 있다.
'''

