#8장 입출력



'''시용자가 키보드로 입력하는 값을 받기 위한 input() 함수와 
화면에 내용을 출력하기 위한 print() 함수-> 표준 입출력(standard input/output)
파일로부터 내용을 읽어와서 프로그램에서 사용하거나 
프로그램 안에서 어떤 내용을 직접 쓰는 파일 입출력(file input/output)'''


#8.1 표준 입력받기: input() 



#입력은 프로그램에 값을 넣는 것-> 키보드로 값을 입력받는 것


answer=input("아무 값이나 입력하세요: ")
print("입력한 값은 "+answer+" 입니다.")

#print()문을 보면 +연산자로 문자열과 입력값을 연결해 출력한다.
#str()로 감싸지 않았는데 숫자 10을 입력해도 제대로 출력하는 이유는 왜 그럴까?


answer=input("아무 값이나 입력하세요: ")
print("입력한 값은 "+answer+" 입니다.")
print(type(answer))     #두 경우 모두 str(문자열)로 나온다.-> input() 함수로 입력받은 값은 항상 문자열로 인식한다.


'''아무 값이나 입력하세요: 나도코딩
입력한 값은 나도코딩 입니다.
<class 'str'>
아무 값이나 입력하세요: 1010
입력한 값은 1010 입니다.
<class 'str'>
'''

#그러나 10을 입력받아 이 값을 숫자 연산 목적으로 사용하려면 반드시 int(answer)로 자료형을 바꿔야 한다.

answer=input("아무 값이나 입력하세요: ")
print("입력한 값은 "+answer+" 입니다.")
print(type(answer))     #<class 'str'>
print(type(int(answer)))    #<class 'int'>
answer=10
print(type(answer)) #<class 'int'>




#8.2 표준 출력 시 유용한 기능



'''표준 출력은 기본 출력 장치를 통해 프로그램을 수행한 결과를 사용자에게 보여준다-> VScode의 터미널
표준 입력에 input() 함수가 있다면 표준 출력에는 print() 함수가 있다.

쉼표를 사용해 값을 구분하거나 +연산자를 통해 서로 다른 자료형의 데이터를 형변환해서 출력해봤다.
자동으로 줄 바꿈을 하지 않기 위해 end를 사용하는 방법에 대해서도 알아봤다.
이외에도 표준 출력을 다양하게 활용할 수 있는 유용한 기능을 배워보도록 하자.'''


#8.2.1 구분자 넣기: sep(separator)

#print() 함수 정의에서 sep 매개변수의 기본값은 공백(" ")이다.
#기본값 대신 다른 값을 넣어 print() 함수를 실행하면 해당 값을 구분 기호로 사용한다.

print("파이썬", "자바")     #값을 공백으로 구분
print("파이썬" , "자바", sep=",")   #값을 쉼표로 구분

print("파이썬", "자바", "자바스크립트")     #파이썬 자바 자바스크립트
print("파이썬", "자바", "자바스크립트", sep="vs")   #파이썬 vs 자바 vs 자바스크립트, 값을 'vs'로 구분


#8.2.2 문장 끝 지정하기: end

#end의 기본값은 줄 바꿈(\n)
#print()함수는 문장을 출력한 후 기본으로 줄 바꿈하고 print() 함수를 2개 이상 연속해서 사용하면 각각 다른 줄에 실행결과를 출력한다.
#end에 다른 값을 넣어 주면 문장 끝을 줄 바꿈 대신 지정한 값으로 바꿀 수 있다.

print("파이썬", "자바", sep=",", end="? ")
print("무엇이 더 재미있을까요?")    #파이썬, 자바? 무엇이 더 재미있을까요?


#8.2.3 출력 위치 지정하기: file


import sys  #sys 모듈을 가져와서 사용함

print("파이썬", "자바", file=sys.stdout)    #file-> print() 문의 실행결과를 어디에 출력할지 지정
print("파이썬", "자바", file=sys.stderr)    

#sys.stdout: 표준 출력(standard output), 현재 표준 출력인 터미널에 결과를 출력하시오
#sys.stderr은 표준 오류(standard error): 오류가 발생했을 때 터미널에 오류 메시지를 띄우시오


'''
설정한 값은 결과가 같아 보이지만, 실제 용도는 다름
프로그램 실행 과정에서 몇 시에 어떤 작업을 어떤 방식으로 수행하며 실행 결과가 어떤지의 정보를 기록하는 것을 로그(log)를 남긴다.
로그를 남길 때 sys.stdout은 일반적인 내용을, sys.stderr는 오류가 발생했을 때 관련 내용을 출력한다.
둘을 구분해 사용하면 프로그램이 의도치 않게 작동했을 때 오류 로그를 확인해서 빠르게 상황을 파악하고 그에 맞는 조치를 취할 수 있다.
다만, 두 값은 어느 정도 규모가 있는 프로젝트를 진행할 때 필요한 기능이고, 이는 심화 내용이므로 입문 단계에서는 뉘앙스만 알고가자.
'''



#8.2.4 공간 확보해 정렬하기: ljust()와 rjust()


#성적 정보를 출력하는 코드이다.

scores={"수학": 0, "영어": 50, "코딩": 100} #scores 딕셔너리

for subject, score in scores.items():   #(key, value)
    print(subject, score)

#subject와 score라는 이름으로 key와 value를 대입할 두 변수를 지정, 반복대상을 scores.items()로 작성->scores 딕셔너리의 key와 value가 차례로 subject와 scoer 변수에 대입된다.
'''수학 0
영어 50
코딩 100'''

#ljust()-> 함수에 숫자를 넣어 전달하면 숫자 값만큼 미리 공간을 확보하고 해당 공간에서 왼쪽 정렬(rjusg()는 오른쪽 정렬)

scores={"수학": 0, "영어": 50, "코딩": 100} #scores 딕셔너리

for subject, score in scores.items():   
    print(subject.ljust(8),str(score).rjust(4), sep=":")    #sep 값에 콜론(:)으로 지정해 과목명(subject)과 점수(score)를 구분한다.

'''
과목명이 담긴 subject 변수에 ljust(8)로 접근해 출력한다.-> 전달값8에 의해 공간을 총 8칸 확보한다, ljust() 함수로 왼쪽 정렬한다.
#rjust() 함수는 오른쪽 정렬하므로 전달값4에 의해 공간을 4칸 확보하고 값을 오른쪽 정렬한다.
#점수를 제외한 나머지 공간은 과목명과 마찬가지로 빈칸으로 출력한다.
'''


#8.2.5 빈칸 0으로 채우기: zfill()


for num in range(1, 21):    #1~20의 숫자
    print("대기 번호 : "+str(num))

for num in range(1, 21):
    print("대기 번호 : "+str(num).zfill(3))     #zfill()-> 전달하는 숫자(3)만큼 공간을 확보하고 문자열 앞의 빈칸을 0으로 채운다.




#8.3 다양한 형식으로 출력하기: format()
    


print("{0}".format(500))    #{0}위치에 값 500 출력

#format() 함수의 소괄호 안에 넣은 값이 중괄호({}) 위치에 들어가 출력됨
#중괄호({}) 부분을 수정하면 다양한 형태로 문자열을 출력할 수 있다.

print("{0: >10}".format(500))    #빈칸으로 두기(공백), 오른쪽 정렬(>), 공간 10칸 확보(10)

'''
500
       500  (10칸)
'''

'''
{0: >10}-> 공간 10칸을 확보한 상태에서 오른쪽 정렬하고 나머지 공간은 빈칸으로 둔다
콜론 뒤에 오는 공백, >, 10은 각각 빈칸으로 두기, 오른쪽으로 두기, 오른쪽으로 정렬하기, 지정한 만큼(10) 공간 확보하기
공백 대신 {0:_>10} 또는 {0:a>10}처럼 밑줄이나 다른 문자를 입력해 해당 값으로 나머지 공간을 채울 수도 있다.
단, 나머지 공간을 빈칸으로 두려는 경우에는 {0:>10}과 같이 콜론과 부등호 사이에 공백을 생략해도 된다.
'''

print("{0: >+10}".format(500))  #빈칸으로 두기, 오른쪽 정렬, + 기호 붙이기, 공간 10칸 확보
print("{0: >+10}".format(-500)) #음수일 때

'''
      +500
      -500
'''

print("{0:_<10}".format(500))   #빈칸을 _로 채우기, 왼쪽 정렬, 공간 10칸 확보

#500_______

print("{0:,}".format(100000000000)) #3자리마다 쉼표 찍기
print("{0:+,}".format(100000000000))    # +기호 붙이기, 3자리마다 쉼표 찍기
print("{0:+,}".format(-100000000000))   # 음수일 때, 3자리마다 쉼표 찍기(헷갈림 주의!!-> {0:-,}아님 주의)

'''
100,000,000,000
+100,000,000,000
-100,000,000,000
'''

print("{0:^<+30}".format(100000000000)) #빈칸을 ^로 채우기, 왼쪽 정렬, + 기호 붙이기, 공간 30칸 확보, 3자리마다 쉼표 찍기

#+100000000000^^^^^^^^^^^^^^^^^

print("{0}".format(5/3))    #소수점을 포함하는 실수를 출력

#실수값을 출력할 때 round() 함수로 반올림할 수 있는데, format() 함수로도 가능하다.
#1.6666666666666667

print("{0:f}".format(5/3))  #콜론(:) 뒤에 f를 추가하면 연산 결과가 소수점 이하 6자리까지 출력됨

#1.666667


'''
소수점을 원하는 자리까지만 출력하고 싶다면 f 앞에 점(.)과 숫자(n)을 붙인다.
-> 소수점 이하 n+1 번째 자리에서 반올림해서 소수점 이하 n 번째 자리까지 출력함
만약 소수점 이하 둘째 자리까지 출력하고 싶다면 콜론 뒤에 .2f라고 적으면 된다.
'''

print("{0:.2f}".format(5/3))    #소수점 이하 둘째 자리까지 출력, 1.67


'''
위치를 표시하는 중괄호 안에서 인덱스 뒤에 콜론을 붙이고 정해진 순서에 맞춰 필요한 항목을 선택해 명시하면 된다.
빈칸 채우기는 정렬할 때 추가하는 사항이다.
정렬만 넣거나 빈칸 채우기와 정렬을 함께 넣는 것은 가능하지만, 빈칸 채우기만 넣는 것은 안된다.

형식: {인덱스:[[빈칸 채우기]정렬][기호][공간 확보][쉼표][.자릿수][자료형]}
'''



#8.4 파일 입출력


#8.4.1 파일 열고 닫기: open(), close()


#파일을 열떄-> open() 함수: open("파일명", "모드", encoding="인코딩 형식")
#파일명: 열어 볼 파일의 이름/ 모드: 파일을 어떤 방식으로 여는지를 의미함/ encoding: 파일 내용에 담긴 문자 표시와 관련한 것(값을 utf8로 설정하면 한글을 포함한 파일을 사용할 때도 문제없음)


#모드의 종류

'''
1. r: 읽기(read)-> 파일 내용을 읽어 오기 위한 모드
2. w: 쓰기(write)-> 파일에 내용을 쓰기 위한 모드, 같은 이름의 파일이 있으면 해당 파일을 덮어 써서 기존 내용은 삭제됨
3. a: 이어쓰기(append)-> 파일에 내용을 쓰기 위한 모드, 같은 이름의 파일이 있으면 기존 내용 끝에 이어서 씀
'''

#학교 성적 정보를 담은 텍스트 파일을 만들어 보자


score_file=open("score.txt", "w", encoding="utf8")  #score.txt 파일을 쓰기 모드로 열기(w)
print("수학: 0", file=score_file)   #score.txt 파일에 내용 쓰기
print("영어: 50", file=score_file)  #score.txt 파일에 내용 쓰기
score_file.close()  #score.txt 파일 닫기

'''
실행하면 아무것도 출력하지 않음-> print() 문에서 file 값을 score_file로 설정했기 때문
실행결과를 표준 출력(터미널)이 아닌 파일에 출력함
VSCode의 탐색기를 보면 소스 코드 파일과 동일한 위치(Python Workspace 폴더)에 score.txt 파일이 새로 생긴 것을 볼 수 있다.

파일을 열어 보면 결과가 출력되어 있다.
수학: 0
영어: 50
'''

#open() 함수 호출 결과를 저장하는 score_file을 파일 객체라고 한다-> 여기서는 파일 데이터를 담은 상자(변수) 정도로 생각하자

'''
코드 마지막 줄에서는 파일 쓰기를 완료하고 close() 함수를 호출한다.
close() 함수는 지정한 파일을 닫는 함수-> 모든 파일은 열고 나면 반드시 닫아야 함
파일을 닫지 않으면 내용이 제대로 저장되지 않거나 소스 코드의 다른 위치에서 같은 파일에 접근하려고 할 때 파일에 따라 문제가 발생할 수 있음
'''



#8.4.2 파일 쓰기: write()


#쓰기 모드로 열면 파일을 덮어 쓰므로 이어 쓰기 모드(a)로 연다.


score_file=open("score.txt", "a", encoding="utf8")  #score.txt 파일에 이어 쓰기 모드로 열기(a)

score_file.write("과학: 80\n")  #write() 함수는 줄 바꿈이 없으므로 \n 추가
score_file.write("코딩: 100\n")
score_file.close()

'''
수학: 0
영어: 50
과학: 80
코딩: 100
'''



#8.4.3 파일 읽기: read(), readline(), readlines()

#파일에 작성한 내용을 터미널에 출력해보자

score_file=open("score.txt", "r", encoding="utf8")  #score.txt 파일을 읽기 모드로 열기
print(score_file.read())    #파일 전체 읽어 오기(read는 파일 내용 전체를 한 번에 읽어 오는 함수)
score_file.close()


#readline() 함수-> 한 줄씩 끊어서 읽어올 수도 있다.

score_file=open("score.txt", "r", encoding="utf8")

print(score_file.readline(), end="")    #한 줄씩 읽어 오고 커서는 다음 줄로 이동
print(score_file.readline(), end="")    #end 값을 설정해 줄 바꿈 중복 수행 방지
print(score_file.readline(), end="")
print(score_file.readline(), end="")

score_file.close()


#하지만 대부분은 파일을 열어 보기 전까지 총 몇 줄인지 알 수 없다.
#readline() 함수를 몇 번 실행해야 할 지 모호함-> while 문을 사용하자
#파일에 내용이 남아 있는 동안 반복해서 읽어 올 수 있다-> 더 이상 읽어 올 내용이 없을 때 반복문을 탈출한다.

score_file=open("score.txt", "r", encoding="utf8")

while True:     #while 문의 조건을 True로 설정해서 탈출 조건을 만나기 전까지 반복 수행하게 함
    line=score_file.readline()
    if not line:    #더 이상 읽어 올 내용이 없을 때(반복할 때마다 파일에서 한 줄씩 읽어와서 line이라는 변수에 저장)
        break   #반복문 탈출
    print(line, end="")     #읽어 온 내용 출력

score_file.close()


#비슷한 방법으로 파일 내용을 한꺼번에 불러와서 리스트에 저장해 두고 리스트를 반복하면서 내용을 출력할 수도 있다.
#readlines() 함수-> 파일 내 모든 줄을 읽어와서 lines라는 리스트에 저장함
#while 문 대신 for 문을 사용해 리스트 데이터를 순서대로 읽어 온다(반복 대상이 리스트이므로 while보다는 for-> 데이터를 읽어오기 수월)

score_file=open("score.txt", "r", encoding="utf8")
lines=score_file.readlines()    #파일에서 모든 줄을 읽어 와 리스트 형태로 저장

for line in lines:  #lines에 내용이 있을 때까지 읽어 온 내용 출력
    print(line, end="")

score_file.close()



#8.5 데이터를 파일로 저장하기: pickle 모듈

'''
프로그램을 실행하다 보면 많은 변수가 생겼다가 사라지고, 변수의 값도 자주 변하기 쉽다.
print() 함수로 데이터가 어떻게 바뀌는지 확인할 수 있지만, 프로그램을 종료하고 나면 흔적이 없어진다.

만약 리스트 데이터를 다시 사용해야 하거나 다른 프로그램에서 같은 데이터가 필요하다면?
다른 누군가가 만든 리스트 데이터를 가져와서 사용해야 한다면?

프로그램은 실행이 끝나면 모든 데이터가 사라지므로 끝나기 전에 어딘가 저장해야 함-> pickle
프로그램에서 사용하는 데이터를 파일 형태로 저장하거나 불러올 수 있게 하는 모듈
pickle 모듈로 데이터를 파일에 저장할 때 dump() 함수를 사용
'''

#형식: dump(저장할 데이터, 저장할 파일명)

'''
어떤 사람의 프로필 데이터를 만들고 저장해보자
pickle 모듈을 가져다 쓰기 위해 import 한다.

    import pickle

파일 하나를 여는데, 파일명은 profile.pickle로 하고, 모드는 w(쓰기)로 한다.
그런데 pickle 모듈로 저장하는 파일은 텍스트(text)가 아닌 바이너리(binary) 형태이다.

*텍스트 파일: 사람이 읽을 수 있는 글자(한글, 영어, 숫자 등)로 이루어진 파일로, 보통 txt 형식으로 저장함.글꼴, 글자 크기, 색상 등 서식 정보 없이 단순한 글자만 저장할 수 있음
*바이너리 파일: 컴퓨터가 인식할 수 있는 이진수(0, 1)로 이루어진 파일로, JPG, PNG 같은 이미지 파일, MP3 같은 음악 파일, EXE 같은 실행 파일 등이 해당

파일의 형태에 따라 파일 열기 모드는 구분해서 사용한다.
1. t(텍스트 text)-> 파일을 텍스트 모드로 열기.읽기 모드일 떄는 rt, 쓰기 모드일 때는 wt로 사용.텍스트 모드는 기본값이므로 t는 생략 가능
2. b(바이너리 binary)-> 파일을 바이너리 모드로 열기.읽기 모드일 때는 rb, 쓰기 모드일 때는 wb로 사용

따라서 profile.pickle 파일을 열기 위해 open() 함수를 사용할 때 w 모드 뒤에 b를 붙여 wb라고 해야 올바르게 저장된다.
파일에 한글이 포함됐다 하더라도 별도의 encoding은 저장할 필요 없음

    profile.pickle=open("profile.pickle", "wb")

profile 변수를 하나 만들고 이름, 나이, 취미를 딕셔너리 형태로 정의한다.
취미는 여러 개 담을 수 있게 리스트 형태로 넣는다.

작성한 데이터를 dump() 함수를 사용해 파일로 작성한다.
'''


import pickle   #pickle 모듈 가져다 쓰기

profile_file=open("profile.pickle", "wb")   #바이너리 형태로 저장(wb)
profile={"이름": "스누피", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  #profile 데이터를 파일에 저장
profile_file.close()

'''
실행하면 profile에 들어 있는 데이터를 터미널에 출력한다.
탐색기를 보면 소스 코드 파일과 동일한 위치(PythonWorkspacepace 폴더)에 profile.pickle이라는 파일이 생긴 것을 볼 수 있다.
이 파일은 바이너리 형태라서 VSCode나 다른 에디터에서 열어도 내용을 확인할 수 없다.
'''


'''
추가 개념. pickle 모듈 사용 시 오류가 발생한다면?

AttributeError-> 소스 코드를 작성 중인 파일명이 pickle.py여서 my_pickle,py 등 다른 이름으로 변경해야 함

import할 때 같은 경로(폴더)에 있는 파일을 먼저 인식하므로 사용하려는 모듈과 같은 이름으로 파일을 생성하면 안됨!
'''

#데이터가 잘 저장됐는지 확인해보자
#파일을 다시 불러올 떄-> load() 함수를 사용
#형식: load(불러올 파일명)


import pickle

profile_file=open("profile.pickle", "wb")   #바이너리 형태로 저장
profile={"이름":"스누피", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  #profile 데이터를 파일에 저장
profile_file.close()

profile_file=open("profile.pickle", "rb")   #읽어 올 때도 바이너리 형태 명시
profile=pickle.load(profile_file)   #파일에 있는 정보를 불러와서 profile에 저장

print(profile)
profile_file.close()

'''
{'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}
{'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}
'''



#8.6 파일 한 번에 열고 닫기: with 문


'''
파일로 어떤 작업을 할 때 open() 함수로 파일을 열면 반드시 close() 함수로 닫아야 함
close() 함수를 항상 잊지 말아야 하는 부담을 해소할 순 없을까?

with 문은 파일을 열고 나서 close() 함수를 호출하지 않아도 자동으로 닫아준다.

with 작업 as 변수명:
    실행할 명령1
    실행할 명령2
    ...

with 뒤에 오는 작업 위치에 파일을 여는 open() 함수가 들어간다.
open() 함수로 열린 파일은 as 뒤에 있는 변수명으로 접근할 수 있다.
with 문에서 실행할 명령문들은 이에 속해 있음을 표시하도록 반드시 들여쓰기(4칸)해야 함
'''


'''
pickle 모듈로 파일 내용을 불러오는 작업을 with로 다시 구현해보자.
profile.pickle 파일을 바이너리 읽기 모드인 rb로 열어서 profile_file이라는 변수에 저장한다.
with 문 안에서는 profile_file 변수로 파일에 접근할 수 있다.
이제 pickle 모듈의 load() 함수로 이 파일 내용을 가져와 출력한다.
'''


import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


#study.txt라는 텍스트 파일을 w(쓰기)로 열고 encoding은 utf8로 저장한다.

'''
이렇게 만들어진 파일을 study_file 변수에 담고 다음 줄에서 write() 함수로 파일에 쓸 내용을 작성한다.
다음 줄에서 write() 함수로 파일에 쓸 내용을 작성한다.
'''

import pickle

with open("study.txt", "w", encoding="utf8") as study_file:    #새로운 파일 생성
    study_file.write("파이썬을 열심히 공부하고 있어요") 

'''
실행하면 터미널에는 아무것도 출력되지 않고 study.txt 파일만 생성된다.
이제 생성한 파일을 with 문으로 읽어보자.
r(읽기) 모드로 열고 같은 변수명인 study_file로 지정하며, read() 함수로 파일 내용을 읽어 와서 출력한다.
'''

import pickle

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

#실행하면 write() 함수로 작성한 파일 내용을 그대로 출력한다.
#with 문을 사용하면 파일을 읽고 쓰는 코드가 간결해지며 매번 close() 함수를 사용하지 않아도 된다는 장점이 있다.




#8.7 실습 문제: 보고서 파일 만들기



#문제.회사에서 매주 1회 보고서를 작성할 때, 1~50주차까지 보고서 파일을 만드는 파일을 작성하시오

#조건1. 파일명은 '1주차.txt', '2주차.txt'...로 만든다.완성 코드를 실행하면 소스 코드와 동일한 위치에서 50개 파일을 생성한다.

#조건2.각 파일에는 각 주차에 해당하는 내용이 포함돼 있다.(부서, 이름, 업무 요약)

'''
import pickle


with open("{0}주차.txt".format(str(range(1, 51))), "w", encoding="utf8") as report_file:
    for i in range(1, 51):
    report_file.write("-{0}주차 주간보고-\n부서: \n이름: \n업무 요약: ".format(str(range(1, 51))))

with open("{0}주차.txt".format(str(range(1, 51)))) as report_file:
    print(report_file.read())
    '''


for i in range(1, 51):  #숫자 1~50
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("-{0}주차 주간보고-".format(i))
        report_file.write("\n부서: ")   #줄 바꿈 처리
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")

