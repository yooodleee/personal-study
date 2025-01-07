#7장 함수(function)




#7.1 함수 정의하기


#입력값(x)에 따라 결과, 즉 출력값(y)이 달라지는 어떤 동작(f(x))을 수행함
#함수의 입력값-> 전달값
#출력값-> 반환값

#앞에서 배운 함수들은 파이썬에서 특정 기능을 하도록 미리 만들어 둔 함수-> 내장 함수
#사용자가 직접 코드를 작성해 만든 함수-> 사용자 정의 함수
#형식: def 함수명():
        #실행할 문장1
        #실행할 문장2
        #...

#함수를 나타내는 def라는 키워드가 오고 한칸 띄운 후 함수명을 적는다.
#함수명은 소문자로 작성하는데 언더바(_)를 사용할 수 있다.
#함수명 뒤에는 소괄호(())와 콜론(:)을 붙인다.
#다음 줄에는 함수가 어떤 동작을 하는지 작성한다.-> 함수 본문, 함수 본문은 함수에 속한다는 표시로 들여쓰기함(4칸 권장)
#이와 같은 형식으로 함수를 만드는 것-> 함수 정의


#7.1.1 실습: 은행 계좌 개설하기

def open_account():
    print("새로운 계좌를 개설합니다.") 

#이 코드는 함수를 만들기만 한다-> 아무 결과를 출력하지 않는다.
#실제로 함수가 동작하게 하려면 함수를 사용해야 한다.
#함수를 사용할 때는 함수명에 소괄호만 붙이면 된다.

def open_account():
    print("새로운 계좌를 개설합니다")   #open_account() 함수 정의

open_account()  #앞에 정의한 open_account() 함수 호출

#함수명으로 함수를 사용할 때 함수를 호출한다고 한다.
#함수를 호출할 때는 호출한 함수가 앞에 정의돼 있어야 한다.


#추가 개념 함수명 짓기

#함수의 동작을 드러낼 수 있게 짓는 것이 좋다.
#문자로 시작한다.
#단어가 여럿일 때는(open, account) 언더바(_)로 구분한다.
#일반적으로 변수는 명사, 함수는 동사를 사용한다.
    #변수명:account_number-> 계좌번호(명사)
    #함수명:open_account-> 계좌를 개설하다(동사)




#7.2 전달값과 반환값



#전달값과 반환값을 포함하는 함수
#형식: def 함수명(전달값1, 전달값2, ...):
        #실행할 문장1
        #실행할 문장2
        #...
        #return 반환값

#함수명 옆에 있는 소괄호 안에 필요한 개수만큼 전달값을 넣는다.
#전달값은 함수를 사용하려고 호출할 때 함수에 전달하는 값이다.
#함수 본문에서는 전달값들을 활용해 어떤 동작을 수행한다.
#동작이 끝나면 끝에 있는 return 문으로 함수를 호출한 위치에 값을 반환한다.-> 반환하는 값이라서 반환값
#반환값은 보통 1개지만, 여러 값을 반환해야 하는 경우에는 쉼표로 구분해 튜플 형태로 반환할 수도 있다.




#7.2.1 실습: 입급하기



#개설한 개좌에 돈을 입금하는 프로그램을 코딩해보자

def open_account():
    print("새로운 계좌를 개설합니다.")  #open_account() 함수 정의

open_account()  #open_account() 함수 호출


def deposit(balance, money):    #입금 처리 함수(예금을 뜻하는 deposit, 입금하려는 금액의 money, 현재 잔액을 뜻하는 balance)
    print("{0}원을 입금했습니다.잔액은 {1}원 입니다.".format(money, balance + money))
    return balance + money    #입금 후 잔액 정보 반환/여기까지가 함수 정의

balance= 0   #초기 잔액(입금 내역이 없음, 초깃값=0), balance 변수에 초깃값으로 0 저장
balance= deposit(balance, 1000)  #1000원 입금(앞에 정의한 deposit() 함수를 호출), deposit() 함수는 전달값을 받아 동작을 수행하고 값을 반환함->이 값을 받아 다시 balance 변수에 저장
#balance 변수에 deposit() 함수의 반환값을 다시 저장


#함수 정의에도 balance 변수가 있고, 함수 호출에도 balance 변수가 있다.-> 두 변수는 이름은 같지만 같은 변수가 아니다.
#함수 정의에 있는 balance는 전달값(0)을 저장하는 새로운 변수, money 또한 1000이라는 값을 저장하는 새로운 변수-> 둘은 함수 안에서만 사용 가능
#함수를 정의할 때 전달값을 받는 balance, money 변수를 매개변수(parameter)라고 한다.

#함수의 동작 수행이 끝나면 마지막에 return 문으로 값을 반환한다.
#반환하는 값은 함수 밖에 정의한 balance 변수에 저장한다.
#balance는 현재 잔액을 나타내는 변수인데, 1000원을 입금해 잔액이 변경됐으므로 deposit() 함수의 반환값을 받아 저장한다.
#변수에 어떤 값을 저장할 때처럼 함수를 호출하고 나서 반환하는 값을 변수에 다시 저장하는 것.


#함수에서 return 문으로 실행하고 나면 값을 반환함과 동시에 함수를 빠져나간다.
#return 문 밑에 어떤 코드가 있다면 이 부분은 실행되지 않는다.-> 반복문을 탈출하는 break 문의 작동방식과 비슷하다.
#만약 함수를 호출하고 반환값을 저장하지 않으면 어떻게 될까?
#함수가 어떤 값을 반환하기는 하지만, 이 값을 받아서 저장한 곳이 없으므로 반환값을 사용할 수 없다.-> 함수가 반환하는 값을 사용하려면 반드시 반환값을 저장할 변수를 명시해야 한다.



#7.2.2 실습: 출금하기


#출금을 처리하는 함수

def open_account(): #계좌 개설 함수, open_account() 함수 정의
    print("새로운 계좌를 개설합니다.")

open_account()  #open_account() 함수 호출


def deposit(balance, money):    #입금 처리 함수
    print("{0}원을 출금했습니다.잔액은 {1}원 입니다.".format(money, balance + money))
    return money + balance    #입금 후 잔액 반환, deposit() 함수 정의


def withdraw(balance, money):   #출금 처리 함수
    if balance >= money:  #잔액이 출금액보다 많으면
        print("{0}원을 출금했습니다.잔액은 {1}원 입니다.".format(money, balance - money)) #조건을 만족하지 않으면(잔액<출금액) else 문으로 가서 출금 실패를 안내하고 기존 잔액을 반환한다.
        return balance - money    #출금 후 잔액 반환
    else:
        print("잔액이 부족합니다.잔액은 {0}원 입니다.".format(balance))
        return balance  #기존 잔액 반환, withdraw() 함수 정의

balance= 0   #초기 잔액
balance= deposit(balance, 1000)   #1000원 입금, deposit() 함수 호출

#출금

balance= withdraw(balance, 2000) #2000원 출금 시도
balance= withdraw(balance, 500)  #500원 출금 시도, withdraw() 함수 호출

#첫번째 출금 시도(2000원으로 전달값을 넘긴다.deposit() 함수를 호출한 후이므로 현재 잔액이 1000원이다.)
#잔액이 출금하려는 금액보다 적으므로 출금에 실패한다.(출금 시도액:2000 > 잔액:1000)
#두번째 출금 시도(출금액을 500원으로 전달한다.잔액이 더 많아서 정상적으로 출금되고 출금 후 잔액도 반환된다.)


#7.2.3 실습: 수과료 부과하기

def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()


def deposit(balance, money):
    print("{0}원을 입금했습니다.잔액은 {1}원 입니다.".format(money, balance + money))
    return balance + money

def withdraw_night(balance, money): #업무 시간 외 출금
    commission= 100  #출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money- commission

balance= 0
balance= deposit(balance, 1000)

#업무 시간 외 출금 시도
commission, balance= withdraw_night(balance, 500)    #튜플 형태로 반환하는 값 2개를 각각 변수에 저장
print("수수로 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

#1000원을 입금한 상태에서 500원을 출금하니 업무 시간 외 수수료 100원을 제외한 400원이 잔액으로 표시된다.
#return 문을 보면 수수료(commission)와 기존 잔액에서 출금액과 수수료를 뺀 금액(balance-money-commission)을 쉼표로 구분해 함께 반환한다.
#이런 형태가 튜플이다.-> 쉼표로 구분해 값을 여러 개 적으면 함수를 호출하는 쪽에서도 한 번에 여러 값을 변수에 저장할 수 있다.
#코드를 보면 commission과 balance 변수에 각각 수수료와 출금 후 잔액 정보를 저장한다.


#추가 개념 들여쓰기와 띄어쓰기

#코딩할 때 중요한 것 중 하나가 바로 가독성이다.-> 읽기 쉽도록 코드를 작성하는 것
#탭, 스페이스 등으로 들여쓰기나 띄어쓰기를 불규칙적으로 쓰면 코드를 볼 때 굉장히 읽기 어렵다.
#지금 작성하는 코드를 미래의 자신이 알아보기 쉽게 들여쓰기, 띄어쓰기 등 코드를 작성하는 방식을 통일하도록 사람들끼리 일종의 약속을 함
#파이썬 스타일 가이드(style guide)

#print() 함수 안에서 문자열과 변수를 +로 묶어서 출력할 때 +와 변수 사이를 붙이거나 한 칸씩 띄어 쓰거나 결과는 동일하다.
#또한 함수를 호출하며 쉼표로 값을 구분할 때도 쉼표와 값 사이를 띄우거나 붙이거나 동작은 같다.
#하지만 예제 코드에서 작성한 대로 띄어 쓰기를 추천한다.




#7.3 함수 호출하기



#7.3.1 기본값 사용하기


#굳이 무엇이다 라고 말하지 않아도 당연히 그 값이겠거니
#사용할 값을 직접 정의할 수 있는 것-> 기본값, 매개변수에 미리 지정해 둔 값
#기본값이 있으면 전달값을 일일이 적지 않아도 기본값을 그대로 사용함-> 함수 호출 간편
#물론, 기본값이 있다고 해도 호출할 때 전달값을 포함하면 기존 함수처럼 전달값을 대입해 사용할 수 있다.


def profile(name, age, main_lang):
    print("나이: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))   #\t: 탈출 문자(간격)

profile("찰리", 20, "파이썬")
profile("루시", 25, "자바")

#나이: 찰리      나이: 20        주 사용 언어: 파이썬
#나이: 루시      나이: 25        주 사용 언어: 자바


#둘의 나이가 같고 현재 같은 학교를 다니며 같은 수업을 듣는다면?
#모두 20세, 파이썬을 다룬다면?-> 전달값 3개 중에 나이와 주 사용 언어는 생략 가능하겠구나!

def profile(name, age=20, main_lang="파이썬"):  #age와 main_lang(매개변수)에 각각 20, "파이썬"을 미리 저장(기본값)
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("찰리")
profile("루시")

#이름: 찰리      나이: 20        주 사용 언어: 파이썬
#이름: 루시      나이: 20        주 사용 언어: 파이썬



#추가 개념 전달값 작성 순서

#함수를 정의할 때 일반 전달값과 기본값이 있는 전달값을 함께 사용하는 경우-> 반드시 일반값을 먼저 적어야 함
#기본값이 있는 전달값을 먼저 적으면 오류가 발생한다.(SyntaxError-> 문법적 오류!)


def buy(item1, item2="음료수"): #일반값(item1) 먼저 정의 후, 기본값(item2) 정의
    print(item1, item2)

buy("빵")   #빵 음료수


#7.3.2 키워드 인자 사용하기

#함수를 호출할 때 전달값뿐만 아니라 어디에 전달할지 명시적으로 지정한 것-> 키워드 인자(keyword argument)
#보통 함수에 전달값이 많고 기본값이 잘 정의돼 있을 때 대부분 기본값을 그대로 사용하면서 필요한 부분만 집어서 값을 전달하고자 할 떄 유용함
#순서에 구애받지 않으므로 함수에서 사용 가능한 키워드 인자만 알고 있다면 사용할 수 있다는 장점!

def profile(name, age, main_lang):  #함수 정의에서의 순서와 호출에서의 순서가 다름
    print(name, age, main_lang)

profile(name="찰리", main_lang="파이썬", age=20)    #함수 호출 부분-> 전달값 3개의 순서가 뒤죽박죽
profile(main_lang="자바", age=25, name="루시")      #어디에 어떤 값을 전달할지 정해줌

#profile(name="루시", 25, "파이썬")-> SyntaxError(잘못된 함수 호출:키워드 인자를 먼저 작성해야 함!)


#추가 개념 위치 인자

#함수를 호출할 때 함수에서 정의된 순서대로 입력하는 전달값-> 위치 인자(positional argument)

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile("찰리", 20, "파이썬")   #위치 인자: "찰리", "20", "파이썬"



#7.3.3 가변 인자 사용하기


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age))
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")

#이름: 찰리      나이: 20
#파이썬 자바 C C++ C#
#이름: 루시      나이: 25
#코틀린 스위프트


#결과가 2줄로 나눠 출력되어 내용을 파악하기 불편하다
#실행 결과를 한 줄로 출력하고 싶을 때-> end, 함수를 호출할 때 기본값을 가지는 매개변수
#end 매개변수의 기본값은 "\n"-> 문장을 수행한 후 기본으로 줄 바꿈  
#형식: print(출력할 내용, sep=" ", end="\n", flush=False)


#print()를 호출할 때 키워드 인자 방식으로 end에 다른 값을 넣으면 이를 줄 바꿈 대신 사용하게 된다.
#print()에 end=" "를 넣으면 줄 바꿈 대신 한 칸 띄어 쓴 후 이어서 다음 print()의 실행결과를 출력한다.
#end의 값을 빈칸이 아닌 !나 ,로 변경하면 변경한 값을 문장의 마지막에 사용하고 다음 문장을 이어서 출력한다.

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")

#이름: 찰리      나이: 20         파이썬 자바 C C++ C#
#이름: 루시      나이: 25         코틀린 스위프트


#여기서 출력할 사람이 훨씬 더 많아지게 된다면?-> 함수 자체를 변경해야 하고 호출 부분에서도 변경해야 한다.
#가변 인자(variable argument)-> 개수가 변할 수 있는 인자
#함수에서 전달값 앞에 *를 추가하면 가변 인자가 됨
#가변 인자는 전달값이 몇 개가 들어오든 묶어서 튜플로 인식한다.-> 호출할 때마다 전달값의 개수가 달라져도 상관없음
#형식: 함수명(전달값1, 전달값2,..., *가변인자):
        #실행할 문장1
        #실행할 문장2
        #...
        #return 반환값

def profile(name, age, *language):      #가변인자 
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(language, type(language)) #전달값을 출력할 때 가변 인자로 받은 전달값은 정말 튜플로 인식할까?(type(language))

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트", "", "", "")

#이름: 찰리      나이: 20         ('파이썬', '자바', 'C', 'C++', 'C#', '자바스크립트') <class 'tuple'>
#이름: 루시      나이: 25         ('코틀린', '스위프트', '', '', '') <class 'tuple'>


#언어를 튜플 형태가 아닌 기존처럼 하나씩 출력하게 하자.
#값이 튜플이므로 for문을 사용하면 가변 인자로 전달받은 값들을 하나씩 사용할 수 있음
#언어를 줄 바꿈 없이 한 줄에 표시하기 위해 end=" "
#모든 언어 정보를 출력하고 나면 다음 호출 결과를 출력할 떄 줄 바꿈하도록 아무 내용이 없는 print()도 작성하자.


def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}".format(name, age), end=" ")   #print(language, type(language))
    
    for lang in language:
        print(lang, end=" ")    #언어를 모두 한 줄에 표시
    print() #줄 바꿈 목적

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트", "", "", "")


#추가 개념 함수 안에서 함수 호출하기


def add(item):
    print(item, "붓기")

def americano():    #americano() 함수 안에서 또 다른 함수인 add()를 호출한다.
    add("뜨거운 물")
    add("에스프레소")

print("아메리카노 만드는 법")
americano()

#아메리카노 만드는 법
#뜨거운 물 붓기
#에스프레소 붓기


#기본값은 함수에서 매개변수에 미리 지정해 둔 값으로 기본값이 있으면 전달값을 넣지 않아도 된다.
#기본값이 있어도 함수를 호출할 때 전달값을 포함하면 기본값 대신 전달값을 대입해 사용한다.




#7.4 변수의 범위: 지역변수와 전역변수


'''glasses=10

def rent(people):
    glasses=glasses-people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    print("전체 3D 안경 개수: {0}".format(glasses))

    rent(2)
    print("남은 3D 안경 개수: {0}".format(glasses))'''

#위 코드의 결과는 오류(glasses라는 변수가 아직 할당되지 않았는데 사용됨)
#코드 앞에서는 glasses=10으로 변수를 정의했는데 왜 오류가 뜰까?

#지역변수(local variable)-> 함수 안(지역)에서만 사용할 수 있는 변수, 매개변수를 포함해 함수 안에서 새롭게 정의하는 변수는 모두 해당
#전역변수(global variable)-> 모든 곳(전역)에서만 사용할 수 있는 변수
#두 변수는 사용할 수 있는 범위가 다르다!


glasses=10  #지역변수->전역변수 glasses의 값에는 아무 영향 미치지 않음

def rent(people):
    glasses=20  #변수 정의 추가(전역변수) !=지역변수, 이름은 같지만 서로 다른 변수
    glasses=glasses-people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2)
print("남은 3D 안경 개수 : {0}".format(glasses))


'''전체 3D 안경 개수: 10
[함수 내부] 남은 3D 안경 개수: 18
남은 3D 안경 개수 : 10'''

#global 키워드를 변수 앞에 붙이면 전역변수를 함수 안에서 사용하겠다는 의미!
#함수 안에 global glasses라고 작성하면 전역 공간에 정의한 변수를 함수 안에서 그대로 사용할 수 있고 값도 변경가능하다.


glasses=10  

def rent(people):
    global glasses  #전역 공간에 있는 glasses 변수를 함수 안에서 사용하겠다는 표시
    glasses=glasses-people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2)
print("남은 3D 안경 개수 : {0}".format(glasses))

#함수 안에 전역변수를 자주 사용하면 코드 관리가 복잡해진다-> 꼭 필요한 경우가 아니라면 되도록 사용하지 말자!
#전역 변수가 없다면...


glasses=10

def rent_return(glasses, people):   #전체 3D 안경 수와 대여 관객 수를 전달받음
    glasses=glasses-people  #전달값을 담은 glasses 사용
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    return glasses

print("전체 3D 안경 개수: {0}".format(glasses))
glasses=rent_return(glasses, 2) #함수 안에서 수정된 glasses 값을 반환받음
print("남은 3D 안경 개수: {0}".format(glasses))

#함수를 정의할 때 전달값을 잘 지용하면 함수 외부 상황은 몰라도 함수 기능에 충실하면서도 간결하게 작성 가능하다.
#함수 안에 정의한 지역변수는 함수 안에서만 접근할 수 있다.
#지역변수는 외부에서 접근할 수 없다.
#서로 다른 함수에서 같은 이름의 지역변수를 정의할 수 있으며, 이때 두 변수는 서로 관련이 없다.


x=3 #지역변수

def add():  #함수 정의
    x=6 #전역변수
    x+=3
add()#함수 호출

print(x) #3




#7.5 실습 문제: 표준 체중 구하기



#표준 체중을 구하는 프로그램을 작성하시오
#남자: 키*키*22
#여자: 키*키*21

'''조건1:표준 체중은 별도 함수로 계산한다.(단, 키는 m(미터) 단위로 받는다)
    함수명:std_weight
    전달값:키(height), 성별(gender)'''

'''조건2:실행결과에서 표준 체중은 소수점 이하 둘째 자리까지 표시한다.'''


def std_weight(height, gender):     #(1) 표준 체중 계산 함수 정의
    if gender=="male":
        return height*height*22
    else:
        return height*height*21

height=175      #(2) 전달값(키, cm단위)을 저장한 변수 정의
gender="male"   #(2) 전달값(성별)을 저장한 변수 정의
#weiht=std_weight(height/100, gender)-> (3) 함수 호출(키는 cm 단위에서 m단위로 변환)

weight=round(std_weight(height/100, gender), 2)     #(5) 반올림해서 소수점 둘째 자리까지 표시
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender,weight))  #(4) 결과 출력


#해설

#(2) 전달값을 작성한다.키가 175cm이고 성별이 남자이므로 이 값을 담은 height와 gender 변수를 정의




#셀프 체크


#미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수를 만들어보자



'''조건1.get_air_quality라는 이름으로 함수를 만든다.
    조건2.이 함수는 전달값으로 미세먼지 수치를 입력받는다.
    조건3.이 함수는 대기질 상태를 반환한다.
    조건4.미세먼지 수치에 따른 대기질 상태는 다음과 같다.
    좋음:0~30
    보통:31~80
    나쁨:81~150
    매우 나쁨:151이상
    조건5.함수에 전달되는 전달값은 항상 0이상의 값이라고 가정한다.'''


def get_air_quality(dust):
    if dust<=30:
        print("좋음")
    elif dust<=80:
        print("보통")
    elif dust<=150:
        print("나쁨")
    else:
        print("매우 나쁨")

#테스트 코드
print(get_air_quality(15))  #좋음
print(get_air_quality(85))  #나쁨