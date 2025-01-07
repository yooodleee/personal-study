#6장 제어문




#6.1 조건에 따라 분기하기: 조건문


#6.1.1 조건이 하나일 때: if 문

#조건에 따라 동작이 달라진다-> 분기한다
#형식: if 조건 : (다음 줄에) 실행할 명령

weather="비" #weather라는 변수에 '비'라는 값을 저장

if weather=="비":   #조건(weather가 '비'인가?)-> 참이라면 "우산을 챙기세요" 출력
    print("우산을 챙기세요")    #실행할 print()문은 if 위치를 기준으로 4칸 들여쓰기(중요)

#들여쓰기 여부에 따라 동작이 완전히 달라지니 주의하자!
#들여쓰기를 위한 공백 개수가 하나만 달라도 코드는 제대로 작동하지 않는다!


#추가 개념 콜론과 들여쓰기

#콜론(:)과 들여쓰기는 문법적 강제 사항으로, 실행 구간을 정의하는 역할을 한다.
#잘못 사용하는 경우에는 SyntaxError나 IndentationError가 발생함
#if, while, for문이나 뒤에서 배우는 def, try, except 등의 구문은 뒤에 콜론을 붙이고 하위 명령문들을 들여쓰기 해서 한 묶음임을 표시함

#if 편의점에 초코과자가 있으면:
    #초코과자를 사와    if문이 참일 때 실행
#딸기 과자를 사와   if문과 상관없이 항상 실행

#if 편의점에 초코과자가 있으면:
    #초코과자를 사와
    #딸기과자를 사와    마지막 문장을 들여쓰기를 해서 작성하면 초코파이가 있을 때만 초코과자와 딸기과자를 사오고, 없을 때는 아무것도 사오지 않는다.(if문이 참일 때 항상 실행)



#6.1.2 조건이 여러 개일 때: elif 문
    

weather=="맑음"
if weather=="비":
    print("우산을 챙기세요.")   #if문의 조건과 맞지 않아 print()문을 실행하지 않고 프로그램 종료

weather=="미세먼지"
if weather=="비":   #if문은 처음 딱 1번만 사용할 수 있음
    print("우산을 챙기세요.")   #1번
elif weather=="미세먼지":   #elif 문은 필요한 만큼 여러 번 사용할 수 있음
    print("마스크를 챙기세요.") #2번

#둘 다 아닐 때는 아무것도 출력하지 않는다.
#조건이 더 있다면 elif 문을 밑에 추가하면 됨
#elif문도 if문과 마찬가지로 끝에 콜론(:)을 붙이고, 실행할 문장을 모두 들여쓰기를 해야한다!!



#6.1.3 모든 조건에 맞지 않을 때: else문

#if문과 elif문의 조건에 모두 해당하지 않을 때 어떤 명령을 실행하고 싶다면 사용함

weather=="맑음"
if weather=="비":
    print("우산을 챙기세요.")
elif weather=="미세먼지":
    print("마스크를 챙기세요.")
else:   #앞의 조건에 모두 해당하지 않을 때 실행
    print("준비물이 필요 없어요.")



#6.1.4 input()으로 값 입력받아 비교하기

#사용자로부터 어떤 값을 입력받는 용도로 사용한다.
#사용자가 값을 입력하고 엔터를 누르면 이 값은 항상 문자열 형태로 변수에 저장된다.
#즉, 숫자 3을 입력해도 문자열 '3'으로 인식한다는 점에 주의하자

weather=input("오늘 날씨는 어때요?")
print(weather)



weather=input("오늘 날씨는 어때요?")

if weather=="비":
    print("우산을 챙기세요.")   #비를 입력했을 때
elif weather=="미세먼지":
    print("마스크를 챙기세요.") #미세먼지를 입력했을 때
else:
    print("준비물이 필요 없어요.")  #맑음을 입력했을 때



weather=input("오늘 날씨는 어때요?")

if weather=="비" or weather=="눈":  #or 연산자:조건 중 하나라도 참이면 print() 실행
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")


#input() 함수는 입력값을 항상 문자열로 인식한다-> 정수형으로 입력받아도 문자열이 됨
#온도를 비교하기 위햐 정수형으로 변환해야 하므로 input() 함수를 다시 int()로 감싸준다.

weather=int(input("오늘 기온은 어때요?"))   #입력값을 정수형으로 형변환
temp=str(range(1,31))

if 30<=temp:    #30도 이상이면
    print("너무 더워요, 외출을 자제하세요")
elif 10<=temp and temp<30:  #10도 이상 30도 미만이면, and 연산자는 조건이 둘 다 참일 때 참, 10<=temp<30
    print("활동하기 좋은 날씨예요")
elif 0<=temp and temp>10:   #0도 이상 10도 미만이면, 0<=temp<10
    print("외투를 챙기세요")
else:   #그 외 모든 경우(0도 미만이면)
    print("너무 추워요, 나가지 마세요")


weather=int(input("오늘 기온은 어때요?"))

if temp>=30:
    print("너무 더워요, 외출을 자제하세요")
elif temp>=10:
    print("활동하기 좋은 날씨예요")
elif temp>=0:
    print("외투를 챙기세요")
else:
    print("너무 추워요, 나가지 마세요")
   


#6.2 같은 일 반복하기: 반복문



print("대기 번호 : 1")
print("대기 번호 : 2")
print("대기 번호 : 3")
print("대기 번호 : 4")


#6.2.1 범위 안에서 반복하기: for 문


#형식: for 변수 in 반복 대상(1.반복 대상에서 변수로 값 가져오기) :  (3.반복 대상으로 돌아가기/반복해서 더 이상 가져올 값이 없으면 반복문을 벗어남)
      #실행할 명령1
      #실행할 명령2 (2.실행)
      #...

#반복문을 나타내는 키워드인 for와 in 연산자 사이에 변수를 넣고 in 뒤에 반복 대상을 지정함
#반복 대상에는 리스트나 딕셔너리, 튜플 또는 문자열이 들어간다.
#if 문과 마찬가지로 for 문 끝에 콜론(:)을 붙이고 다음 줄에 반복 실행할 명령문을 작성한다.
#이때도 for 문에 속한 문장임을 알 수 있게 들여쓰기(4칸)를 해서 구분한다.


for waiting_no in[1,2,3,4,5]:   #반복 대상으로 리스트를 사용함
    print("대기 번호 : {0}".format(waiting_no)) #{0}의 위치에 waiting_no의 값이 들어감

#대기 손님이 5명일 때 반복문을 사용하면 코드가 2줄로 작성되고 결과는 동일하게 나온다!
#반복 대상이 무수히 많아질 때-> range() 함수를 사용하면 편하다./지정한 범위 안에서 연속한 정수를 반환
#형식: range(숫자)/ range(시작 숫자, 끝 숫자)/ range(시작 숫자, 끝 숫자, 간격)

for waiting_no in range(5): #0부터 5직전까지(0~4), range(1,6):1부터 6직전까지(1~5)
    print("대기 번호 : {0}".format(waiting_no))

for waiting_no in range(1,6,2): #1부터 6직전까지(1~5)에서 2씩 간격 주기
    print("대기 번호 : {0}".format(waiting_no))

orders=["아이언맨", "토르", "스파이더맨"]    #리스트 
for customer in orders:     #orders 리스트를 변수 customer에 저장
    print("{0}님, 커피가 준비됐습니다.픽업대로 와주세요.".format(customer))


#6.2.2 조건을 만족할 동안 반복하기:while 문

#for 문은 리스트와 같은 반복 대상에서 값을 하나씩 가져와 반복 작업을 수행
#while 문은 조건을 만족하는 동안 끝없이 반복함
#형식: while 조건:
        #실행할 명령1
        #실행할 명령2


customer="토르" #손님 닉네임
Index=5 #초깃값, 부르는 횟수 최대 5번

while Index>=1: #부르는 횟수가 1 이상일 떄만 실행
    print("{0}님, 커피가 준비됐습니다.".format(customer))
    Index-=1    #횟수 1회 차감
    print("{0}번 남았어요.".format(Index))
    if Index==0:    #5번 모두 불렀다면/다시 while 문의 조건으로 돌아가면 index>=1 조건을 더이상 만족하지 않으므로 거짓(False)이므로 while 문을 벗어남
        print("커피를 폐기")

customer="아이언맨"
index=1

#while True:
#    print("{0}님, 커피가 준비됐습니다.호출 {1}회".format(customer, index))
#    index+=1    #코드에 while 문을 탈출하게 하는 구문이 없어서 while 문을 끝없이 반복 수행함-> 무한 루프(infinite loop)에 빠졌다

#무한 루프 발생 시 프로그램은 강제 종료해야 하며, Ctrl+C 를 누른다.

customer="토르"
person=None

while person!=customer:
    print("{0}님, 커피가 준비됐습니다.".format(customer))
    person=input("이름이 어떻게 되세요?")   #토르님, 커피가 준비됐습니다.이름이 어떻게 되세요?->토르(커피를 주문한 손님과 닉네임이 일치하면 while 문 탈출)



#6.2.3 흐름 제어하기: continue와 break


#continue-> 이후 명령들을 실행하지 않고 다음 반복 대상으로 넘어갈 떄 사용
#break-> 반복문을 즉시 탈출할 때 사용


absent=[2,5]    #결석한 학생 출석번호

for student in range(1,11): #출석번호 1~10
    if student in absent:   #결석한 학생이면
        continue    #다음 학생으로 넘어가기(결석 학생을 실행하지 않고 다음 반복 대상으로 넘어감)
    print("{0}번 학생, 책을 읽어보세요.".format(student))


absent=[2,5]    #결석한 학생 출석 번호
no_book=[7]     #책을 가져오지 않은 학생 출석 번호

for student in range(1,11): #출석번호 1~10번(정수 1~10을 변수 student에 저장, 10개의 숫자)
    if student in absent:   #결석한 학생이면
        continue    #다음 학생으로 넘어감
    elif student in no_book:    #책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지.{0}번 학생은 교무실로 따라와요".format(student))
        break   #반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요".format(student))


#continue와 break은 자신이 속한 가장 가까운 반복문에 대해 동작한다.
#반복문 안에 또 다른 반복문이 있는 이중 반복문일 때 내부 반복문에서 contine나 break을 사용하면 모든 반복문이 아닌 내부 반복문만 탈출하고 외부 반복문은 계속 수행한다.



#6.2.4 for 문 한 줄로 작성하기

#형식: [동작 for 변수 in 반복 대상]
#for 문은 정확한 용어로 리스트 컴프리헨션(list comprehension)이라고 한다.
#for 뿐만 아니라 if 문의 조건도 함께 사용할 수 있다.


students=[1,2,3,4,5]
print(students)

students=[i+100 for i in students]  #한 줄 for 문으로 각 항목에 100 더하기
print(students) #반복 대상인 students 리스트에서 i 라는 변수로 값을 하나씩 가져와서 i 변수의 값에 100을 더한 후 이 값을 다시 students에 저장해 새로운 리스트로 만들라는 의미

#students=[students[0]+100, students[1]+100, students[2]+100, students[3]+100, students[4]+100]
#students=[1+100, 2+100, 3+100, 4+100, 5+100]
#한 줄 for 문은 반복 대상의 값들에 각각 어떤 동작을 수행하고, 수행한 결과들을 모아 새로운 리스트로 만든다.


#추가 개념 한 줄 for 문 작성 시 주의할 점

#한 줄 for 문을 작성할 때 사용한 변수 i 는 임의로 사용한 이름이므로 다른 변수명을 사용해도 된다.
#다만, '변수 위치'와 '변수로 어떤 동작을 하는 위치'에서 변수명이 동일해야 하는 점을 주의하자


students=["Iron man", "Thor", "Spider man"]
print(students)

students=[len(i) for i in students] #한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
print(students) #띄어쓰기를 포함한 각 이름의 길이 8,4,10을 새로운 리스트로 만들어서 students에 저장한다.

#students=[len(students[0]), len(students[1]), len(students[2])]
#students=[len("Iron man"), len("Thor"), len("Spider man")]


students=["Iron man", "Thor", "Spider man"]
print(students)

students=[i.upper() for i in students]  #한 줄 for 문으로 각 이름을 모두 대문자로 변경
print(students)




#6.3 실습 문제 : 택시 승객 수 정하기

#손님이 총 50명일 때, 조건을 만족하는 총 탑승객 수를 구하시오.(count())

#조건.손님별 운행 소요시간은 5~50분에서 난수로 정한다.(range(5,51))
#조건.운행 소요시간 5~15분인 손님만 매칭한다.(range(5,16))
#조건.매칭되면 [0], 매칭되지 않으면 []로 표시한다.


#내가 풀었을 때

sonim=[range(1,51)]
time=range(5,51)

for matching_sonim in sonim:
    if time in time>=5 and time <=15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(sonim, time))
    elif time in time<5 and time >15:
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(sonim, time))
        break
    print("총 탑승객 : {0}명".format(count(matching_sonim)))




#해설 
    
from random import *    #(1)random 모듈 추가

cnt=0   #(2) 총 탑승객 수

for i in range(1,51):   #(3) 손님 총 50명
    time=randrange(5,51)    #(4) 변수 정의 소요시간 5~50분
    if 5<=time<=15: #(5) 소요시간 5~15분인 손님만 매칭
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))    #매칭 성공 출력
        cnt+=1  #총 탑승객 수 증가 처리

    else:   #(6) 매칭 실패 시
        print("[ ] {0}번째 손님 (소요 시간 : {1}분)".format(i, time))   #매칭 실패 출력

    print("총 탑승객: {0}명".format(cnt))   #총 탑승객 수 출력



#셀프 체크
    
#편의점에서 동일한 상품 2개를 구매하면 상품 1개를 무료로 제공하는 2+1 이벤트를 진행한다.
#구매 상품 수에 따라 가격을 계산하는 프로그램을 작성하시오

#조건.상품 1개의 가격은 1000원이다.
#조건.고객은 3의 배수에 해당하는 상품을 구매한다고 가정한다.
#상품은 각각 스캔하며, 한 상품을 스캔할 때마다 '2+1 상품입니다.'를 출력한다.


price=1000  #상품 가격
goods=3 #구매 상품 수 
total=0 #총 가격
for i in range(1,goods+1):  #구매 상품 수가 3인 경우 1~3 반복 수행
    print("2+1 상품입니다.")
    if i %3==0: #3의 배수인 경우 가격을 더하지 않음
        continue
    total+=price

price("총 가격은 "+str(total)+"원입니다.")