print(5+3)
print(2*8)
print(6/3)
print(3*(3+1)) #정수형

print('풍선')
print("나비") #''와 ""는 사용에 있어 큰 차이는 없다만 꼭 짝을 맞춰야 한다
print("abcdefg")
print("10")
print("파이썬"*3)  #결과:파이썬파이썬파이썬->문자열에 정수가 곱해져 있다면 그만큼 문자열을 반복하여 출력한다

print(5>10)
print(5<10) #불(boolean)은 참과 거짓을 판별한다, True와 False값만을 가짐
print(True) #불값이 그대로 있다면 불값을 출력함
print(False)
print(not True) #not은 반대됨, 따라서 not True는 False를, not False는 True를 출력
print(not False)
not(5>10) #5>10은 False인데, not을 한번 더 만나므로 결과값은 True
print(not(5>10))

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 개인데, 이름은 연탄이에요")
print("연탄이는 4살이고, 산책을 아주 좋아해요")
print("연탄이는 수컷인가요?")
print("네")

name="연탄이" #변수는 사용하기 전에 정의한다, 그리고 가능한 알아보기 쉽게 정의하자
animal="개" #변수는 어떤 값을 저장하는 공간, 대입 연산자(=)
age=4
hobby="산책"
is_male=True
print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 "+animal+"인데, 이름은 "+name+"에요")
print(name+"는 " +str(age)+"살이고, "+hobby+"을 아주 좋아해요")

name="해피"
animal="고양이"
age=4
hobby="낮잠"
print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 "+animal+"인데, 이름은 "+name+"에요")
print(name+"는 " +str(age)+"살이고, "+hobby+"을 아주 좋아해요")
print(name,"는",age,"살이고,",hobby,"을 아주 좋아해요") # +연산자 대신에 ,콤마를 사용할 수도 있지만 공백도 같이 출력된다

print(int("3")) #형변환->값의 자료형을 다른 형태로 바꾸는 것

print(int(3.5)) #int()->값을 정수형으로 형변환

print(float("3.5")) #float()은 값을 실수형으로 형변환
print(float(3))
print(str(3)+"입니다") #str은 값을 문자형으로 형변환시켜줌
print(str(3.5)+"입니다")

print(type(3)) #정수(int)
print(type("3")) #문자열(str)
print(type(3.5)) #실수(float)
print(type(str(3))) #정수(int)를 문자열(str)로 형변환

station="사당"
print(station+"행 열차가 들어오고 있습니다.")
station="신도림"
print(station+"행 열차가 들어오고 있습니다.")
station="인천공항"
print(station+"행 열차가 들어오고 있습니다.")

status="상품 준비"
print("주문 상태 : "+status)
status="배송 중"
print("주문 상태 : "+status)
status="배송 완료"
print("주문 상태 : "+status)
