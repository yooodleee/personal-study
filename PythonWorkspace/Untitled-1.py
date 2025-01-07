#8.1 표준 입력받기 : input()


answer=input("아무 값이나 입력하세요 : ")
print("입력한 값은 "+answer+"입니다.")

'''
+ 연산자로 문자열과 입력값을 연결해 출력한다.
문자열과 문자열이 아닌 숫자는 보통 str()로 감싸야 하지 않을까?

'''

answer=input("아무 값이나 입력하세요 : ")
print("입력한 값은 "+answer+"입니다.")
print(type(answer))

'''
결과는 str(문자열)이 나온다.
input()으로 입력받은 값은 항상 문자열로 인식한다.
+연산자로 연결해 출력해도 아무 문제가 없다.

단 10을 입력받아 이 값을 숫자 연산 목적(계산의 목적)이라면 반드시 int(answer)로 기입해야 한다.
'''

answer=input("아무 값이나 입력하세요 : ")
print("입력한 값은 "+answer+"입니다.")
print(type(answer)) #str(문자열)

print(type(int(answer)))    #int(정수)
answer=10
print(type(answer)) #int(정수)


dream=input("당신의 꿈은 무엇입니까?")
print(f"제 꿈은 {dream}입니다.")


#8.2 표준 출력 시 유용한 기능


#8.2.1 구분자 넣기 : sep


print("sep", "java")
print("python"+"java")

print("sep", "java")
print("sep", "java", sep=",")   # ,로 구분

print("python", "java", "javascript")
print("python", "java", "javascript", sep="vs")


#8.2.2 문장 끝 지정하기 : end


print("python", "java", sep=",", end="? ")
print("무엇이 더 재미있을까요?")


#8.2.3 출력 위치 지정하기 : file


import sys

print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

'''
import sys-> sys 모듈을 가져와 사용한다.

file은 print() 문의 실횅 결과를 어디에 출력할지 지정함

sys.stdout은 표준 출력(standard Output), 현재 표준 출력인 VSCode의 터미널에 결과를 출력

sys.stderr-> 표준 오류(standard error), 오류가 발생했을 때 터미널에 오류 메시지를 출력

설정한 두 값은 결과가 같아 보이지만, 실제 용도는 다르다.
보통 프로그램 실행 과정에서 몇 시에 어떤 작업을 어떤 방식으로 수행하고 있으며 실행결과가 어떠한지의 정보를\
기록할 때 로그를 남긴다.

로그를 남길 때 sys.stdout은 일반적인 내용을, sys.stderr는 오류가 발생할 때 관련 내용을 출력한다.
둘을 구분해 사용하면 프로그램이 의도치 않게 작동했을 때 오류 로그를 확인해 빠르게 상황을 파악하고 그에 맞는 조치를 취할 수 있다.

다만, 두 값은 어느 정도 규모가 있는 프로젝트를 진행할 때 필요한 기능이며, 심화 내용이므로 입문 단계에서는 '이런 기능이 있구나'\
정도만 알고 가자.

터미널 대신 파일에 출력하는 방법도 있다.
이때는 print() 문으로 출력하는 내용이 지정한 파일에 표시되고, 터미널에서는 출력 내용을 확인할 수 없다.
관련 기능은 open(), close()
'''


#8.2.4 공간 확보해 정렬하기 : ljust()와 rjust()


scores={"math":0, "english":50, "coding":100}

for subject, score in scores.items():
    print(subject, score)


scores={"math":0, "english":50, "coding":100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


#8.2.5 빈칸 0으로 채우기 : zfill()


for num in range(1, 21):
    print("대기 번호 : "+str(num))

for num in range(1, 21):
    print("대기 번호 : "+str(num).zfill(3))

print("v", "c", "tion", sep="a")


#8.3 다양한 형식으로 출력하기 : format()


print("{0}".format(500))

print("{0}".format(500))
print("{0: >10}".format(500))

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<10}".format(500))

print("{0:,}".format(100000000))
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

print("{0:^<+30,}".format(100000000))

#소수점을 포함하는 실수를 출력한다.

print("{0}".format(5/3))

#콜론 뒤에 f를 추가하면 소수점 이하 6자리까지 출력된다.

print("{0:f}".format(5/3))

#소수점 이하 숫자를 원하는 자리까지만 출력하고 싶다.f 앞에 점과 숫자를 붙인다.

print("{0:2f}".format(5/3))

print("{0:_>+5}".format(100))


#8.4 파일 입출력


#8.4.1 파일 열고 닫기 : open(), close()


'''
open("파일명", "모드", encoding="인코딩 형식")
'''

'''
모드 r: read-> 파일 내용을 읽어 옴

모드 w: write-> 파일에 내용을 씀, 같은 이름의 파일이 있으면 해당 파일을 덮어 써 기존 내용은 삭제됨

모드 a: append-> 파일에 내용을 씀(이어씀), 같은 이름의 파일이 있으면 기존 내용 끝에 이어씀
'''

'''
encoding은 파일 내용에 담긴 문자 표시와 관련한 것
값을 utf8로 설정하면 한글을 포함한 파일을 사용할 때 문제가 없다.
'''


score_file=open("score.txt", "w", encoding="utf8")
print("math:0", file=score_file)
print("english:50", file=score_file)
score_file.close()

'''
파일 쓰기를 완료하고 close()로 파일을 닫는다.
모든 파일은 열고 나면 반드시 닫아야 한다.
파일을 닫지 않으면 내용이 제대로 저장되지 않거나 소스 코드의 다른 위치에서 같은 파일에 접근하려고 할 때\
파일에 따라 문제가 발생할 수도 있다.
'''


#8.4.2 파일 쓰기 : write()


score_file=open("score.txt", "a", encoding="utf8")
score_file.write("science:80\n")
score_file.write("coding:100\n")
score_file.close()


#8.4.3 파일 읽기 : read(), readline(), readlines()


score_file=open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

'''
readline() 함수를 몇 번 실행해야 할 지 모를 때 while문을 사용하면\
파일에 남아 있는 동안 반복해서 읽어 올 수 있다.
더 이상 읽어 올 내용이 없을 때 반복문을 탈출한다.
'''

score_file=open("score.txt", "r", encoding="utf8")

while True:
    line=score_file.readline()
    if not line:
        break
    print(line, end="")

score_file.close()

'''
while 문의 조건을 True로 설정해서 탈출 조건을 만나기 전까지 반복 수행하게 한다.
반복할 때마다 파일에서 한 줄씩 읽어와 line이라는 변수에 저장한다.
if 문으로 line 변수에 내용이 있는지 확인하고 있으면 출력, 없으면 반복문을 탈출한다.
'''

score_file=open("score.txt", "r", encoding="utf8")

lines=score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()


#8.5 데이터를 파일로 저장하기 : pickle 모듈


'''
프로그램에서 사용하는 데이터를 파일 형태로 저장하거나 불러올 수 있게 하는 모듈

데이터를 저장할 때 dump() 함수를 사용함

dump(저장할 데이터, 저장할 파일명)
'''

import pickle

profile_file=open("profile.pickle", "wb")
profile={"name":"snoopy", "age":"30", "hobby":["soccor", "golf", "coding"]}
print(profile)

pickle.dump(profile, profile_file)
profile_file.close()

'''
데이터가 잘 저장됐는지 확인해본다.
앞에서 만든 파일을 다시 불러올 때는 load()를 사용하고 전달값으로 파일명을 넣는다.
'''

import pickle

profile_file=open("profile.pickle", "wb")
profile={"name":"smoopy", "age":"30", "hobby":["soccor", "golf", "coding"]}
print(profile)

pickle.dump(profile, profile_file)
profile_file.close()

profile_file=open("profile.pickle", "rb")
profile=pickle.load(profile_file)

print(profile)
profile_file.close()



#8.6 파일 한 번에 열고 닫기 : with 문


'''
with 작업 as 변수명:
    실행할 명령1
    실행할 명령2
    ...

open() 함수로 열린 파일은 as 뒤에 변수명으로 접근할 수 있다.
제어문이나 def 함수를 정의할 때처럼 문장 끝에 콜론을 붙인다.
with 문에서 실행할 명령문들은 들여쓰기를 반드시 한다.
'''

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

import pickle

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#8.7 실습 문제 : 보고서 파일 만들기

'''
파일명은 '1주차.txt', '2주차.txt',...로 만든다.
실행하면 소스 코드와 동일한 위치에 다음과 같이 50개 파일을 생성한다.
'''

import pickle

weekly_file=open("weekly.pickle", "w", encoding="utf8")

for line in range(1, 51):
    weekly_file.write("-{}주차 주간보고-\n".format(line))
    weekly_file.write("부서: \n")
    weekly_file.write("이름: \n")
    weekly_file.write("업무 요약: \n")
    print(weekly_file)

weekly_file.close()


