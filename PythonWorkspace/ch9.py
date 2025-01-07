#9장 클래스




#9.1 게임 소개


'''
세 종족 사이에 전쟁을 그린 이 게임은 유닛(unit)을 최대한 빠르게 많이 만들어 적을 궤멸시키는 것이 목표이다.
세 종족 중 한 종족을 선택해 게임을 플레이하는 형태로 구현해보자.
가장 기본 유닛인 보병부터 만들어보자.
유닛의 이름과 체력, 공격력 정보를 각각의 변수에 저장하고 유닛이 생성됐다는 내용과 함께 유닛 정보를 출력하자.
'''

name="보병" #이름
hp=40   #체력
damage=5    #공격력

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

'''
이번에도 이름과 체력, 공격력 정보를 변수에 담아 유닛을 생성한다.
name, hp, damage 라는 변수가 이미 쓰였으므로 각각의 변수 앞에 tank_를 붙여서 탱크 유닛을 만들고 내용을 출력하자.
'''

name="보병"
hp=40
damage=5

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name="탱크"
tank_hp=150
tank_damage=35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))

'''
다음으로 두 유닛을 사용해 공격하는 내용을 구현해 보자.
공격 부분은 두 유닛이 공통으로 사용한다.
그래서 함수로 정의해보자.
앞에서 작성한 코드에 이어서 다음 내용을 추가한다.
'''

def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]".format(name, location, damage))

'''
보병과 탱크가 1시 방향을 공격하도록 attack() 함수로 명령을 내려보자
'''

attack(name, "시", damage)  #보병 공격 명령
attack(tank_name, "1시", tank_damage)   #탱크 공격 명령

'''
실행해 보니 두 유닛 모두 명령한 대로 공격하는 것을 볼 수 있다.
이번엔 탱크를 하나 더 만들어 보자.
tank2_를 붙여 변수를 만들어보자.
새로운 탱크를 만들고 공격도 추가한 다음 지금까지 작성한 전체 코드를 실행해 보자.
'''

name="보병" #보병
hp=40
damage=5

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name="탱크"    #탱크
tank_hp=150
tank_damage=35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name="탱크"   #새로운 탱크 2 추가
tank2_hp=150
tank2_damage=35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):     #공격 함수
    print("{0} : {1} 방향 저군을 공격합니다.[공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage) #보병 공격 명령 
attack(tank_name, "1시", tank_damage)   #탱크 공격 명령
attack(tank2_name, "1시", tank2_damage) #탱크 2 공격 명령

'''
유닛을 추가하면 추가할 때마다 같은 방법으로 코드를 추가해야 한다.
서로 다른 종류의 유닛들이 최소 수십 개에서 수백 개까지 존재하는 경우도 있다.
또한 유닛마다 서로 다른 정보(이름, 체력, 공격력 등)가 있는데, 이런 방법으로 관리하는 것은 다소 무리가 있다.
'''




#9.2 클래스와 객체 생성하기


'''
이 경우 클래스가 필요하다고 할 수 있다.
클래스를 붕어빵 틀에 비유해 보자.
붕어빵을 만들 떄 틀에다가 반죽과 속재료를 넣고 불에 구우면 똑같은 모양의 붕어빵을 여러 개 만들 수 있다.
반죽과 속재료를 바꿔도 항상 같은 모양의 붕어빵이 만들어 진다.


*클래스의 기본 형식

클래스를 나타내는 class 뒤에 클래스 명을 적고 콜론(:)을 붙인다.
클래스명은 일반적으로 하나 또는 여러 단어의 조합으로 만드는데, 각 단어의 첫 글자는 대문자로 작성함
그다음 줄부터는 클래스에 속한 내용임을 표시하기 위해 들여쓰기를 한다.

클래스 안에는 필요한 함수를 정의하는데, 클래스 안에 정의하는 함수를 매소드(method)라고 한다.
일반 함수와 다르게 첫 번째 전달값 위치에는 self라고 넣는다.
메서드의 첫 번쨰 전달값 위치에는 항상 self를 넣는다.
메소드의 각 명령문은 메소드 소속임을 표시하기 위해 들여쓰기도 해준다.

*형식

class 클래스명:
    def 메서드명1(self, 전달값1, 전달값2, ...):
    실행할 명령1
    실행할 명령2
    ...

    def 메서드명2(self, 전달값1, 전달값2, ...):
    실행할 명령1
    실행할 명령2
    ...

'''

'''
앞에서 작성한 유닛 생성 코드를, 클래스를 사용해 다시 만들어 보자.

클래스명은 Unit이라고 정의하자.
Unit 클래스 안에 메서드 하나를 만드는데, 이름은 __init__(언더바를 앞뒤로 2개씩)으로 한다.
첫 번쨰 전달값으로 self를 넣고 나머지 전달값으로 이름, 체력, 공격력을 넣는다.
메서드 안에는 전달값을 받는 변수를 정의하자.
변수의 형식은 다음과 같다.

*형식
self.변수명= 값
메서드 안에 정의한 변수를 인스턴스 변수라고 한다.(클래스 안에서 사용하는 변수)

마지막으로 생성한 유닛 정보를 print() 문으로 출력하자.
'''

class Unit:
    def __init__(self, name, hp, damage):
        self.name=name      #인스턴스 변수 name(self.name)에 전달값 name 저장
        self.hp=hp      #인스턴스 변수 hp(self.hp)에 전달값 hp 저장
        self.damage=damage  #인스턴스 변수 damage(self.damage)에 전달값 damage 저장

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

'''
클래스도 함수와 마찬가지로 정의만 해서는 아무런 동작도 하지 않는다.
다음은 클래스를 사용해 유닛을 직접 만들어 보자.

*형식
객체명=클래스명(전달값1, 전달값2, ...)  #self를 제외한 나머지 전달값

보병 둘과 탱크 하나를 만들어 보자.
'''

class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1=Unit("보병", 40, 5)    #보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2=Unit("보병", 40, 5)    #보병2 생성, 전달값으로 이름/체력/공격력 전달
tank=Unit("탱크", 150, 35)      #탱크 생성, 전달값으로 이름/체력/공격력 전달

'''
실행하면 유닛들이 생성된다.
클래스 하나로 서로 다른 유닛 3개를 만들었는데, 이렇게 만들어진 유닛들을 객체(object)라고 한다.
-> soldier1, soldier2, tank는 객체이고, 붕어빵도 객체이다.
이렇게 만들어진 객체를 클래스의 인스턴스(instance)라고 한다.
-> soldier1, soldier2, tank 객체는 Unit 클래스의 인스턴스이고, 붕어빵은 붕어빵 틀의 인스턴스이다.
'''

'''
객체와 인스턴스는 사실 같은 개념이다.
객체를 만드는 것은 결국 클래스의 인스턴스를 만드는 것이다.
보통 객체를 단독으로 부를 때는 객체로, 클래스와 연결지어 부를 때는 인스턴스로 표현한다.
'''

'''
클래스는 서로 관련 있는 변수(인스턴스 변수)와 함수(메서드)들의 집합이다.
게임에서 보병과 탱크는 모두 이름, 체력, 공격력이 있다.
이는 유닛들의 공통 속성이므로 하나의 틀, 즉 클래스로 정의할 수 있다.

클래스 안에는 메서드를 여러 개 정의할 수 있으며, 각 메서드의 첫 번째 전달값 위치에는 self를 넣어야 한다.
__init_() 메서드는 클래스에 필요한 값을 전달받아 self로 클래스의 인스턴스 변수를 정의한다.
'''



#9.2.1 생성자: __init__()


'''
Unit 클래스에 __init__() 메서드를 정의했다.이를 생성자(constructor)라고 한다.
생성자는 사용자가 따로 호출하지 않아도 객체를 생성할 때 자동으로 호출되는 메서드이다.
클래스를 만들 때 __init__라는 이름으로 메서드를 정의하면 자동으로 생성자가 된다.
객체를 생성할 때 생성자가 자동으로 호출되므로 생성자의 전달값 개수만큼 값을 전달해야 한다.
단, self는 기본으로 포함하므로 제외한다.

Unit 클래스의 코드를 다시 살펴보자.
__init__() 생성자 부분을 보면 self를 제외하고 name, hp, damage를 전달값으로 받는다.
유닛, 즉 객체를 생성할 때는 값을 3개씩 전달한다.
'''

class Unit:
    def __init__(self, name, hp, damage):   #생성자, self 외 전달값 3개
        self.name=name
        self.hp=hp
        self.damage=damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1=Unit("보병", 40, 5)    #객체 생성
soldier2=Unit("보병", 40, 5)    #객체 생성  
tank=Unit("탱크", 150, 35)      #객체 생성

'''
만약 전달값을 3개가 아닌 1개 또는 2개만 넘기면 어떻게 될까?

    soldier3=Unit("보병")   #전달값 3개 중 1개만 넘김

TypeError 발생-> 전달값을 1개만 넘기니 오류가 발생함(hp와 damage에 해당하는 전달값 2개가 없다.)

    soldier3=Unit("보병", 40)   #전달값 3개 중 2개만 넘김

TypeError 발생-> 전달값을 2개만 넘기니 오류가 발생함(damage에 해당하는 전달값 1개가 없다.)

객체를 생성할 때는 self를 제외하고 __init__() 생성자에 정의한 개수만큼 전달값을 넘겨줘야 한다.
만약 클래스에 따로 생성자를 정의하지 않았다면 전달값 없이 클래스명만으로 객체를 생성하면 된다.

*형식
변수명=클래스명()

'''



#9.2.2 인스턴스 변수


'''
메서드에 정의한 변수를 인스턴스 변수라고 하며 self와 함께 사용한다.
Unit 클래스에서는 name, hp, damage가 인스턴스 변수이고, self.name과 같은 형식으로 전달값을 받아 정의한다.
'''

class Unit:
    def __init__(self, name, hp, damage):   #생성자, self 외 전달값 3개
        self.name=name  #인스턴스 변수 name
        self.hp=hp  #인스턴스 변수 hp
        self.damage=damage  #인스턴스 변수 damage

        print("{} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

'''
공중을 날아다니는 전투기 유닛을 만들어 보자.
전투기 유닛은 지금까지 동일한 방식으로 생성하는데, 이번엔 클래스 밖에서 인스턴스 변수 정보를 출력해보자.
클래스 안에는 self.으로 인스턴스 변수에 접근할 수 있었는데, 클래스 밖에서는 객체로 접근한다.
객체로 접근할 때는 객체명 뒤에 점(.)을 찍고 인스턴스 변수명을 적으면 된다.
'''

stealth1=Unit("전투기", 80, 5)  #객체 생성, 체력 80, 공격력 5
#인스턴스 변수 접근
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1, stealth1.damage))

'''
객체명이 stealth1이므로 이 객체의 인스턴스 변수에는 stealth1.name과 stealth1.damage로 접근해 값을 출력한다.

stealth2라는 이름으로 전투기 유닛을 하나 더 생성하는데, 해당 전투기는 은폐 기능까지 있다고 가정하자.
'''

stealth2=Unit("업그레이드한 전투기", 80, 5)

'''
Unit 클래스의 인스턴스 변수에는 name, hp, damage만 있어서 은폐 상태를 관리할 수 없다.
그래서 업그레이드한 전투기만을 위한 특별한 인스턴스 변수를 하나 정의하자.
cloaking이라고 하고, True일 때는 은폐 상태, Flase일 때는 일반 상태이다.
cloaking 변수를 만들고 True라고 값을 설정해 은폐 상태로 변경한다.
'''

stealth2=Unit("업그레이드한 전투기", 80, 5)
#특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking=True

'''
은폐 상태일 떄는 cloaking 변수의 값이 True이므로 if 문으로 값이 True인지 확인하자.
'''

stealth2=Unit("업그레이드한 전투기", 80, 5)
#특별한 인스턴스 변수 정의
stealth2.cloaking=True
if stealth2.cloaking==True: #은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))


'''
다른 전투기는 stealth1이었으니 앞에서 같은 방식으로 코드를 작성한 후 실행해보자


if stealth1.cloaking==True:
    print("{0}는 현재 은폐 상태입니다.".format(stealth1.name))

실행하면 오류가 발생함-> Unit 클래스에는 처음과 변함없이 name, hp, damage라는 3개의 인스턴스 변수만 있고 cloaking이 없다.
stealth1에서 클래스에 정의하지 않은 cloaking 변수에 접근하니 오류가 발생한다.

stealth2는 클래스 외부에서 직접 cloaking이라는 인스턴스 변수를 정의했다.
이는 Unit 클래스의 모든 객체가 아닌 오직 stealth2에만 해당하는 인스턴스 변수이다.
그래서 stealth1.cloaking으로 접근할 때와 달리 stealth2,cloaking으로 접근해 값을 비교하는 데 아무런 문제가 없다.

*두 객체의 인스턴스 변수 비교

(stealth1의 인스턴스 변수)   (stealth2의 인스턴스 변수)

name                        name
hp                          hp
damage                      damage
-                           cloaking

이와 같이 클래스로부터 객체를 만든 다음, 객체만을 위한 인스턴스 변수가 필요한 경우에는 클래스 외부에서 별도로 정의할 수 있다.
이때 해당 객체를 제외한 다른 객체들은 새로 정의한 인스턴스 변수를 알지 못하며 사용할 수도 없다.-> 오직 한 객체만을 위한 인스턴스 변수가 된다.
-> 인스턴스 변수는 클래스의 메서드에서 정의하거나 객체를 통해 직접 정의할 수 있다.
'''



#9.2.3 메서드

'''
메서드는 클래스 내부에 정의한 함수로, 클래스 안에 여러 개를 만들 수 있다.
메서드는 일반 함수와 달리 첫 번째 전달값으로 self를 넣고, 메서드 안에서 self.으로 인스턴스 변수에 접근할 수 있다.

이번에는 공격할 수 있는 유닛만을 위한 새로운 클래스를 정의해보자.
AttackUnit은 Unit 클래스와 동일하게 __init__() 생성자에서 name, hp, damage 인스턴스 변수를 정의하는데, print() 문으로 출력하는 내용은 따로 없다.
'''

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage

'''
공격 동작을 위한 메서드를 만들자.
메서드명은 attack으로 하고 전달값에는 기본적으로 넣어야 하는 self와 공격 방향을 의미하는 location을 넣는다.

공격하러 갈 유닛의 이름과 공격 방향 정보, 공격력을 출력하자.
유닛의 이름과 공격력은 클래스의 생성자에 인스턴스 변수로 이미 정리돼 있으므로 self.으로 접근해 사용한다.
공격 방향은 명령을 받을 때마다 달라질 수 있으므로 인스턴스 변수가 아닌 전달값을 그대로 사용한다.
이때 self. 없이 사용한다는 점을 주의하자
'''

''''
코드를 작성할 때 너무 문장이 길어서 한 줄로 표현하기 어렵거나 보기 좋게 두 줄 이상으로 나눠 적으려면
나누려는 부분에 역슬래시(\)를 넣고 줄바꿈을 한다.그러면 실행할 때 한 문장으로 인식한다.
'''

class AttackUnit:   #공격 유닛
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage
    
    def attack(self, location): #전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다.[공격력{2}]"\
              .format(self.name, location, self.damage))    #공간이 좁아서 2줄로 나눔

'''
공격받아 피해를 입는 동작을 정의해보자/
적군의 공격 유닛은 종류별로 공격력이 다르고 상황에 따라 피해 규모가 달라질 수 있으므로 피해량에 해당하는 damage를 전달값으로 받는다.
유닛의 현재 체력 정보에서 damage의 값만큼 빼준다.
만약 공격받은 후 남은 체력이 0 이하라면 유닛을 사용할 수 없으므로 유닛을 파괴 처리한다.
'''

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage
    
    def attack(self, location): #전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다.[공격력{2}]"\
              .format(self.name, location, self.damage))    #공간이 좁아서 2줄로 나눔(\)
    
    def damaged(self, damage):  #damage만큼 유닛 피해
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage)) #피해 정보 출력
        self.hp -= damage   #유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))    #남은 체력 출력
    
        if self.hp <= 0:  #남은 체력이 0 이하이면(들여쓰기 주의!!-> damaged 함수에 포함된 내용이므로)
            print("{0} : 파괴됐습니다.".format(self.name))  #유닛 파괴 처리

'''
AttackUnit 클래스의 객체를 만들어 사용하는데, 이번에는 화염방사병이라는 새로운 유닛을 만들어보자.
화염방사병 유닛을 하나 만들고 5시 방향으로 공격 명령을 내려 보자.
'''

flamethrower1=AttackUnit("화염방사병", 50, 16)  #객체 생성, 체력 50, 공격력 16
flamethrower1.attack("5시") #5시 방향으로 공격 명령

'''
공격하는 와중에 적군으로부터 피해를 입는다고 가정하고 25만큼의 피해를 받도록 하자.
'''

flamethrower1.damaged(25)
flamethrower1.damaged(25)

'''
화염방사병 : 25만큼 피해를 입었습니다.
화염방사병 : 현재 체력은 25입니다.
화염방사병 : 25만큼 피해를 입었습니다.
화염방사병 : 현재 체력은 0입니다.
화염방사병 : 파괴됐습니다.
'''

'''
추가 개념. self


self는 객체인 자기 자신을 의미한다.
생성자 또는 메서드에서 self를 전달값에 넣는다-> 객체를 받는다는 뜻
메서드 안에서 self.을 사용하는 것은 객체의 인스턴스 변수 또는 메서드에 접근하겠다는 의미가 된다.

flamethrower1은 AttackUnit 클래스의 인스턴스이다.
flamethrower1 객체를 생성할 때는 name, hp, damage 정보만 전달하지만, 
자동으로 호출되는 __init__() 생성자의 첫 번째 전달값에 있는 self에 flamethrower1 객체도 전달한다고 보면 된다.
그래서 생성자 안에 작성한 self.name=name 은 flamethrower1.name=name 과 같은 의미이다.

2가지만 기억하면 된다.

1. 클래스의 메서드에는 첫 번째 전달값으로 self를 적어야 한다.
2. 클래스 안에서는 변수 또는 메서드에 접근하려면 self.name 또는 self.attack(...)처럼 인스턴스 변수 또는 메서드명 앞에 self.을 함께 적어야 한다.
'''




#9.3 클래스 상속하기



#9.3.1 상속이란

'''
9.2.3 메서드에서 유닛 중에서 공격할 수 없는 유닛도 있다고 했는데, 유닛들의 수송을 담당하는 수송선과 부상당한 유닛을 치료해주는 \
의무병이 이에 해당한다.
이런 유닛은 공격 명령이 포함된 AttackUnit 클래스로 생성할 수 없다.
그래서 처음에 만든 Unit 클래스를 수정해 보자.

damage 인스턴스 변수를 포함해 공격과 관련된 내용은 AttackUnit 클래스에 있으므로 Unit 클래스는 일반적인 유닛을 위한 클래스로 수정한다.
모든 유닛은 이름과 체력 정보가 있어야 하므로 name, hp 인스턴스 변수는 남겨 두고 공격력인 damage 인스턴스 변수는 없앤다.
코드를 간결하게 하기 위해 print() 문도 삭제한다.
'''

class Unit:
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp  #공격력인 damage 삭제

'''
이번에는 AttackUnit 클래스를 살펴보자.
__init__() 생성자 부분만 보면 Unit 클래스와 겹치는 부분이 있다.
'''

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name=name  #공통 부분
        self.hp=hp  #공통 부분
        self.damage=damage

'''
일반 유닛도 name, hp 인스턴스 변수가 있고 공격 유닛에도 name, hp 인스턴스 변수가 있다.
만약 유닛의 특성에 따라 공격 유닛, 공중 유닛, 지상 유닛 등으로 확장된다면 클래스마다 name, hp 인스턴스 변수를 일일이 넣어야 될 것이다.

하지만 파이썬에는 상속이라는 개념으로 클래스 공통되는 부분을 중복으로 작성하지 않고 재사용할 수 있다.
AttackUnit 클래스는 Unit 클래스의 name, hp 인스턴스 변수를 포함하면서 추가로 damage 인스턴스 변수를 정의하고 있으므로\
Unit 클래스부터 상속받으면 Unit 클래스의 name, hp 인스턴스 변수를 정의하지 않아도 그대로 사용할 수 있다.

다른 클래스로부터 상속받을 때 클래스명 뒤에 소괄호를 적고 상속받을 클래스명을 명시하면 된다.
이때 두 클래스는 실생활에서 자식이 부모로부터 상속받는 관계와 비슷하여 자식 클래스와 부모 클래스라고 한다.

*형식:
class 자식 클래스(부모 클래스):

AttackUnit 클래스의 __init__() 생성자에 name, hp 인스턴스 변수를 정의하는 부분은 다음과 같이 부모 클래스인 unit 클래스의\
__init__() 생성자를 호출하는 방식으로 코드를 간소화할 수 있다.이때 self도 함께 넘겨 줘야 한다.
'''

class AttackUnit(Unit):
    def __init_(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage=damage

'''
이제 AttackUnit 클래스는 Unit 클래스의 모든 인스턴스 변수와 메서드를 그대로 사용할 수 있다.
AttackUnit 클래스만을 위한 인스턴스 변수와 메서드도 추가할 수 있다.

전체 코드는 다음과 같다.
'''

class Unit: #일반 유닛
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp

class AttackUnit(Unit): #공격 유닛, Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   #부모 클래스의 생성자 호출
        self.damage=damage
    
    def attack(self, location): #전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다.[공격력{2}]"\
              .format(self.name, location, self.damage))
    
    def damaged(self, damage):  #damage만큼 유닛 피해
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage)) #피해 정보 출력
        self.hp-=damage #유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, hp)) #남은 체력 출력
        if self.hp<=0:  #남은 체력이 0 이하라면
            print("{0} : 파괴됐습니다.".format(self.name))  #유닛 파괴 처리

'''
Unit 클래스가 간소화됐고, AttackUnit 클래스는 Unit 클래스를 상속하도록 변경됐다.
하지만 AttackUnit 클래스는 부모 클래스로부터 상속받은 name, hp 인스턴스 변수를 그대로 사용할 수 있다.
'''


#9.3.2 다중 상속


'''
비행 기능을 정의하는 클래스를 별도로 만들자.
클래스명은 Flyable이라 하고 __init__() 생성자에는 비행할 때 속도를 의미하는 flying_speed를 인스턴스 변수로 넣는다.
공중 유닛은 무게나 크기, 종류, 비행 속도 업그레이드 여부에 따라 비행 속도가 달라진다.
비행 동작은 fly() 메서드로 정의한다.
Flyable 클래스는 비행 기능만 제공하므로 어떤 유닛인지에 대한 정보는 포함하지 않는다.
대신 fly() 메서드를 호출할 때 유닛의 이름과 비행 방향 정보를 전달받는다.
'''

class Flyable:
    def __init__(self, flying_speed):   #비행 속도
        self.flying_speed=flying_speed
    
    def fly(self, name, location):  #유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다.[속도{2}]"\
               .format(name, location, self.flying_speed))
        
'''
인스턴스 변수를 공부할 때 상대방에게 보이지 않는 은폐라는 특수 기능을 가진 전투기를 소개했다.
전투기는 비행하며 공격할 수 있는 공중 공격 유닛이다.
'공중+공격 유닛'이 합쳐져 있으니 지금까지 만든 클래스 중에서 '공격' 유닛 AttackUnit 클래스와\
'공중' 유닛 Flyalbe 클래스를 조합하면 공중 공격 유닛을 만들 수 있다.

공중 공격 유닛을 위한 새로운 클래스를 만들어 보자.
이름은 FlyalbeAttackUnit으로 하고, Attackunit 클래스와 Flyable 클래스를 함께 상속받는다.
클래스를 2개 이상 상속받는 것을 다중 상속(multiple inheritance)라고 한다.

*형식:
class 자식 클래스(부모 클래스1, 부모 클래스2, ...):

__init__() 생성자 안에서 상속받은 클래스들의 __init__() 생성자를 각각 호출하면 된다.
'''

class FlyalbeAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): #유닛 이름, 체력, 공격력, 비행 속도
        AttackUnit.__init__(self, name, hp, damage) #유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)    #비행 속도

'''
완성한 클래스로 요격기라는 새로운 유닛을 만들어보자.
요격기는 미사일 여러 발을 한 번에 발사하는 강력한 공중 공격 유닛이다.
FlyableAttack 클래스로 새로운 객체를 만들고 이름은 interceptor로 한다.
생성자에는 유닛 이름, 체력, 공격력, 비행 속도 정보를 전달한다.
그런 다음 Flyable 클래스에 정의한 fly() 메서드를 호출하는데, 이때 이동할 유닛 이름과 방향 정보를 전달값으로 넘긴다.
'''

interceptor=FlyalbeAttackUnit("요격기", 200, 6, 5)
#요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사/유닛 이름, 체력, 공격력, 비행 속도
interceptor.fly(interceptor.name, "3시")    #3시 방향으로 이동

'''
먼저 유닛에 공통 요소인 이름과 체력을 담은 일반 유닛 클래스 Unit이 있다.
Unit 클래스를 상속받아 공격력까지 표시하는 공격 유닛 클래스 AttackUnit도 정의했다.
비행 기능이 있는 Flyable 클래스를 정의했다.(비행 속도 정보와 비행 동작 메서드만 가짐)
공중 공격 유닛을 위해 AttackUnit 클래스와 Flyable 클래스를 다중 상속하는 FlableAttackUnit 클래스를 만들었다.

복습할 때 그림을 통해 클래스 간 관계를 파악하는 것도 좋다!!
'''

class Unit: #일반 유닛
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp

class AttackUnit(Unit): #공격 유닛, Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   #부모 클래스의 생성자 호출
        self.damage=damage
    
    def attack(self, location): #전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다.[공격력{2}]"\
              .format(self.name, location, self.damage))
    
    def damaged(self, damage):  #damage만큼 유닛 피해
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage)) #피해 정보 출력
        self.hp-=damage #유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))    #남은 체력 출력
        if self.hp<=0:  #남은 체력이 0 이하라면
            print("{0} : 파괴됐습니다.".format(self.name))  #유닛 파괴 처리

class Flyable:  #비행 기능
    def __init__(self, flying_speed):   #비행 속도
        self.flying_speed=flying_speed
    
    def fly(self, name, location):  #유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다.[속도{2}]"\
              .format(name, location, self.flying_speed))

class FlyalbeAttackUnit(AttackUnit, Flyable):   #공중 공격 유닛
    def __init__(self, name, hp, damage, flying_speed): #유닛 이름, 체력, 공격력, 비행 속도
        AttackUnit.__init__(self, name, hp, damage) #이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)    #비행 속도

#요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
#유닛 이름, 체력, 공격력, 비행 속도

interceptor=FlyalbeAttackUnit("요격기", 200, 6, 5)
interceptor.fly(interceptor.name, "3시")    #3시 방향으로 이동



#9.3.3 메서드 오버라이딩


'''
이번엔 지상 유닛의 이동 속도를 의미하는 speed 인스턴스 변수를 Unit 클래스에 추가해보자.
이동 동작을 나타내는 move() 메서드를 정의하고 공중 유닛과 구분하는 문구를 추가해서 어떤 유닛이 몇 시 방향으로 이동하는지를 출력하자
'''

class Unit: #일반 유닛
    def __init__(self, name, hp, speed):    #speed 추가
        self.name=name
        self.hp=hp
        self.speed=speed    #지상 이동 속도
    
    def move(self, location):   #이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도{2}]"\
              .format(self.name, location, self.speed))

'''
Unit 클래스를 변경하고 나면 Unit 클래스를 상속받는 자식 클래스에 영향을 끼치게 된다.
speed 인스턴스 변수를 새로 추가했으니 __init__() 생성자를 사용하는 부분은 변경해줘야 한다.

먼저 공격 유닛인 AttackUnit 클래스에 speed 인스턴스 변수를 추가하자.
'''

class AttackUnit(Unit): #Unit 클래스 상속
    def __init__(self, name, hp, damage, speed):    #speed 추가
        Unit.__init__(self, name, hp, speed)    #speed 추가
        self.damage=damage
        
'''
AttackUnit 클래스가 변경됐으니 AttackUnit 클래스를 상속받는 FlyableAttackUnit 클래스도 수정해야 한다.
공중 공격 유닛은 비행 속도인 flying_speed가 이미 정의돼 있고, 지상에서는 이동하지 못하므로 지상 이동 속도를 0으로만 설정한다.
'''

class FlyableAttack(AttackUnit, Flyable):   #공중 공격 유닛
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit(self, name, hp, damage, 0)   #지상 이동 속도 0
        Flyable(self, flying_speed) #비행 속도

'''
잘 반영됐는지 확인하기 위해 지상 이동 속도를 포함한 새로운 공격 유닛을 만들어 보자.
지상 유닛 중에서 가장 속도가 빠른 호버 바이크를 추가하자.
AttackUnit 클래스로 호버 바이크 객체를 생성하는데, 전달값으로 지상 이동 속도 10을 포함해 체력 80, 공격력 20을 넣는다.
'''

hoverbike=AttackUnit("호버 바이크", 80, 20, 10) #지상 이동 속도 10

'''
FlyableAttackUnit 클래스도 수정했으니 공중 공격 유닛도 하나 만들어보자.
우주 순양함의 크기는 엄청 크며 체력과 공격력 또한 굉장히 높다.
체력 500, 공격력 25, 비행 속도 3으로 하자.
'''

spacecrusier=FlyalbeAttackUnit("우주 순양함", 500, 25, 3)   #비행 속도 3

'''
새로 만든 두 유닛을 함께 이동시켜 보자.
호버 바이크는 지상 유닛이므로 move() 메서드로 이동하고, 우주 순양함은 공중 유닛이므로 fly() 메서드로 이동한다.
'''

hoverbike.move("11시")
spacecrusier.fly(spacecrusier.name, "9시")

'''
코드를 작성하고 실행 보면 각 유닛의 이동 방향과 속도 정보가 모두 잘 표시된다.

그런데 실행 결과처럼 나오면 공중 공격 유닛인 우주 순양함이 지상 유닛 이동에 포함돼 보인다.
또한, 많은 지상 유닛과 공중 유닛을 이동할 때마다 지상 유닛인지 공중 유닛인지 구분해 move()와 fly() 메서드를 사용하는 번거롭다.
.fly() 메서드를 사용할 때 유닛의 이름 정보까지 전달해야 하는 불편함도 있다.

이럴 때 메서드 오버라이딩(메서드 재정의 method overriding)을 사용할 수 있다.
상속 관계일 때 자식 클래스에서 부모 클래스에 정의한 메서드를 그대로 사용하지 않고 같은 이름으로 메서드를 새롭게 정의해 사용한다.

FlyableAttackUnit 클래스가 상속받는 부모 클래스는 AttackUnit 클래스와 Flyable 클래스이다.
이 중에서 AttackUnit 클래스는 Unit 클래스를 상속받으므로 결국 FlyableAttackUnit 클래스에도 Unit 클래스의 모든 내용을 그대로 사용할 수 있다.

여기서는 Unit 클래스에 정의한 move() 메서드를 FlyableAttackUnit 클래스에 오버라이딩 해보자.
메서드 오바라이딩할 때는 부모 클래스에 정의한 메서드를 그대로 자식 클래스에서 동일한 이름과 전달값으로 정의하고,\
메서드 동작만 원하는 대로 변경하면 된다.

공중 공격 유닛이 이동이므로 메서드 동작에 안내 문구를 추가하자.
공중으로 날아다니므로 또 다른 부모 클래스인 Flyable 클래스에 정의한 fly() 메서드를 호출하면 된다.
이때 유닛 이름과 이동할 위치 정보를 함께 전달한다.
'''

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):   #Unit 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

'''
메서드를 새로 정의했으니 제대로 적용되는지 다시 한번 유닛들을 이동시켜 보자.
지상과 공중 구분 없이 모두 move() 로만 이동하자.
fly() 메서드를 사용할 때와 달리 유닛 이름까지 전달해야 하는 번거로움을 줄일 수 있다.
'''

hoverbike.move("11시")
spacecrusier.move("9시")    #오버라이딩한 move() 메서드 호출
#spacecrusier.fly(spacecrusier.name, "9시")

'''
상속 관계는 변함이 없지만 Unit 클래스에 move() 메서드를 정의함으로써 Unit 클래스로 생성한 객체들은 모두 move() 메서드를 사용해\
지상에서 이동할 수 있다.
하지만 공중 공격 유닛인 FlyableAttackUnit 클래스로 생성한 객체들은 지상이 아닌 공중 비행을 한다.
따라서 Flyable 클래스의 fly() 메서드를 사용해야 한다.

그런데 유닛이 많아지면 개별적으로 관리하기 어려우므로 move() 메서드를 오버라이딩해서 재정의한 메서드에서 fly()를 호출하도록 바꿨다.
이러면 같은 move() 메서드를 호출하더라도 AttackUnit 클래스로 만들어진 유닛은 부모 클래스인 Unit 클래스의 move() 메서드를,\
FlyableAttackUnit 클래스로 만들어진 유닛은 오버라이딩한 FlyableAttackUnit 클래스의 move() 메서드를 호출하게 된다.

지금까지 작성한 전체 코드를 보자.
'''

class Unit: #일반 유닛
    def __init__(self, name, hp, speed):    #speed 추가
        self.name=name
        self.hp=hp
        self.speed=speed    #지상 이동 속도
    
    def move(self, location):   #이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도{2}]"\
              .format(self.name, location, self.speed))

class AttackUnit(Unit): #공격 유닛, Unit 클래스 상속
    def __init__(self, name, hp, damage, speed):    #speed 추가
        Unit().__init__(self, name, hp, speed)  #speed 추가
        self.damage=damage
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다.[공격력{2}]"\
              .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴됐습니다.".format(self.name))

class Flyable:  #비행 기능
    def __init__(self, flying_speed):   #비행 속도
        self.flying_speed=flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.".format(self.name, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):   #공중 공격 유닛
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    def move(self, location):   #Unit 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

hoverbike=AttackUnit("호버 바이크", 80, 20, 10) #호버 바이크, 지상 이동 속도 10
spacecrusier=FlyableAttackUnit("우주 순양함", 500, 25, 3)   #우주 순양함, 비행 속도 3

hoverbike.move("11시")
spacecrusier.move("9시")    #오버라이딩한 move() 메서드 호출




#9.4 동작 없이 일단 넘어가기: pass


'''
게임에서 유닛은 무한정으로 만들 수 없다.
이번에는 건물 유닛을 짓기 위한 클래스를 만들어보자.
건물 유닛도 일반 유닛처럼 이름과 체력이 있어서 적군으로부터 공격받아 체력이 0이 되면 파괴된다.
Unit 클래스에 공통 속성이 있으니 다른 유닛과 마찬가지로 이를 상속받는다.
건물 유닛을 지을 때는 어느 위치에 지을지를 플레이어가 정하는데, 이를 location이라고 하자.

건물 유닛을 클래스로 정의할 때 __init__() 생성자의 세부 내용은 다른 작업을 먼저하고 나서 나중에 코드로 작성하자.
이럴 때 pass를 사용하자.
pass는 아무것도 하지 않고 일단 그냥 넘어간다는 의미로 사용한다.
흐름 제어하기의 continue와 break에서 배운 역할을 떠올려 보자.
'''

class BuildingUnit(Unit):   #건물 유닛
    def __init__(self, name, hp, location):
        pass

supply_depot=BuildingUnit("보급고", 500, "7시")

'''
이렇게만 작성한 상태에서 실행하면 supply_depot 객체가 오류 없이 잘 생성된다.
pass 때문에 __init__() 생성자는 실제로 완성되지 않았지만, 마치 완성된 것처럼 보인다.

pass는 다른 곳에서도 사용할 수 있다.
앞의 코드에 이어서 함수 2개를 만들어 보자.
게임 시작을 알리는 game_start() 함수와 게임 종료를 알리는 game_over() 함수이다.
game_start()에서는 실행할 문장 부분에 print() 문으로 안내 문구로 출력하지만, game_over()에서는 pass만 작성한다.
'''

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")   #game_start() 함수 정의

def game_over():
    pass    #game_over() 함수 정의

game_start()    #함수 호출
game_over()     #함수 호출

'''
실행하면 게임 시작을 알리는 안내 문구만 출력한다.
game_start() 함수에서는 정의한 동작을 수행하고, game_over() 함수는 pass로 아무 동작 없이 그냥 넘어간다.
함수뿐 아니라 if문, for문, while문 등에서도 pass로 당장은 세부 동작을 정의하지 않은 채로 뒀다가 나중에 다시 코드로 완성할 수 있다.

이 절에서 작성한 전체 코드는 다음과 같다.
'''

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot=BuildingUnit("보급고", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()




##9.5 부모 클래스 호출하기: super()


'''
건물 유닛 클래스를 만들 때 pass로만 남겨둔 __init__() 생성자의 코드를 완성해보자.
Unit 클래스를 상속받으므로 Unit 클래스의 __init__() 생성자를 활용하면 된다.
건물은 이동할 수 없으므로 speed 정보는 0으로 하고 다음 줄에서 location 인스턴스 변수를 정의한다.
'''

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        self.location=location

'''
클래스에서도 이름을 직접 적지 않고도 부모 클래스에 접근하는 방법이 있다.
super()는 상속하는 부모 클래스의 메서드를 사용할 때 필요하다.

앞의 코드를 다음과 같이 수정하면 동일한 동작을 수행한다.
단, super()를 사용하는 문장에서는 self를 함께 사용하지 않으니 주의하자!
'''

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)   #Unit.__init__(self, name, hp, 0)과 달리 self를 사용하지 않는다!
        self.location=location

'''
하지만 부모 클래스를 2개 이상 상속하는 다중 상속일 때는 어떨까?
새로운 파이썬 파일(super.py)을 만들어서 다음과 같이 코드를 작성하자.
'''

'''
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

troopship=FlyableUnit()

일반 유닛인 Unit 클래스와 비행 기능인 Flyable 클래스를 정의한다.
이 둘을 부모 클래스로 하는 공중 유닛인 FlyableUnit을 정의하고 생성자에서 super()로 부모 클래스의 생성자를 호출하게 된다.
공중 유닛 중에서 유닛의 수송을 담당하는 수송선을 생성하는 코드를 적고 실행해 보면 결과는 다음과 같다.

Unit 생성자

부모 클래스는 분면 Unit과 Flyable인데, super()로 생성자를 호출했을 때 Unit 클래스의 생성자가 호출된다.
부모 클래스의 상속 순서를 Unit, Flyable에서 Flyable, Unit으로 바꾼 후 다시 실행해 보자.
'''

'''
class Flyalbe(Flyable, Unit):   #상속 순서 변경
    def __init__(self):
        super().__init__()

Flyable 생성자

이번에는 Flyable 클래스의 생성자가 호출되는 것을 볼 수 있다.
즉, 다중 상속을 받은 클래스에서 super()로 부모 클래스에 접근할 때는 순서상 가장 먼저 상속받은 클래스에 접근한다.
그러므로 다중 상속을 할 때 모든 부모 클래스의 생성자를 호출하려면 super()를 사용하지 않고\
다음과 같이 각 부모 클래스의 이름을 명시해서 접근해야 한다.

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self) #Unit 클래스 생성자 호출
        Flyable.__init__(self)  #Flyable 클래스 생성자 호출

Unit 생성자
Flyable 생성자

실행해 보면 부모 클래스의 생성자를 모두 호출하는 것을 확인할 수 있다.
최종 코드는 다음과 같다.

class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):   #상속 순서 변경
    def __init__(self):
        Unit.__init__(self) #Unit 클래스 생성자 호출
        Flyable.__init__(self)  #Flyable 클래스 생성자 호출

troopship=FlyableUnit()

'''



#9.6 게임 완성


'''
지금까지 배운 클래스 내용을 바탕으로 실제 플레이하는 것처럼 텍스트 기반 게임을 완성해보자.
super()를 공부하며 작성한 비교 코드를 제외하고 9장에서 만든 코드들을 보완하는 방향으로 진행한다.
'''


#9.6.1 게임 준비하기

'''
가장 기본인 Unit 클래스부터 살펴보자.

(1) 실제 게임에서는 유닛이 생성될 때마다 각 유닛의 고유 소리를 울려서 유닛 생성을 알려준다.
    여기서는 소리 대신 __init__() 생성자에 print()문을 추가해 어떤 유닛을 생성했는지 안내 문구를 출력한다.

(2) move() 메서드에서는 유닛 이동과 관련한 안내 문구를 2번이나 출력하므로 첫 번째 출력문인 [지상 유닛 이동] 문구는 삭제한다.

(3) 공격 유닛인 AttackUnit 클래스를 만들면서 적군으로부터 공격받을 때 호출되는 damaged() 메서드를 정의했다.
그런데 일반 유닛도 공격할 수는 없지만, 공격받을 수는 있다.
따라서 damaged() 메서드를 Unit 클래스로 이동하고 AttackUnit 클래스에서는 제외했다.

'''

class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛을 생성했습니다.".format(name))  #(1) 안내 문구 출력
    
    def __init__(self, location):
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))
    
    def damaged(self, damage):  #(3) AttackUnit 클래스에서 Unit 클래스로 이동
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴됐습니다.".format(self.name))

'''
AttackUnit 클래스는 Unit 클래스를 damaged() 메서드를 이동하는 것 외에는 수정할 부분이 없다.
'''

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage

    def __init__(self, location):
        print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]"\
              .format(self.name, location, self.damage))
    
'''
보병은 강화제라는 특수 기술이 있다.
특수 기술을 사용하면 일정 시간 동안 이동 속도와 공격 속도가 아주 빠르게 증가한다.
그 대신 체력이 10만큼 소모되므로 현재 남은 체력이 10보다 클 때만 사용할 수 있다는 조건이 필요하다.
다른 부분은 제외하고 특수 기술을 사용할 수 있는지 여부와 체력 소모에 대해서만 작성하자.

기존에는 AttackUnit 클래스로 보병, 탱크 등 지상 유닛을 생성했지만, 이제는 각 유닛을 직접 클래스로 정의하자.
먼저 보병 유닛을 위한 Soldier 클래스를 만든다.

(1) 보병은 공격 유닛이다.
    따라서 AttackUnit 클래스를 상속받아 AttackUnit 클래스의 생성자로 체력, 공격력, 이동 속도를 설정한다.

(2) 강화제 기능을 위해 booster() 메서드를 만든다.
    체력이 10보다 크면 체력 10을 소모한 후 강화제를 사용한다는 안내 문구를 출력하고,\
    10보다 작으면 강화제 사용이 불가능하다는 문구를 출력한다.
'''

class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 50, 1)
    
    def booster(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))

'''
보병에 이어 탱크를 위한 Tank 클래스를 만든다.
탱크는 특수 기술로 시지 모드가 있는데 지상에 고정하고 2배의 공격력과 사정거리를 제공한다.

(1) 보병과 동일하게 AttackUnit 클래스를 상속받는다.

(2) 시지 모드를 개발하면 해당 시점부터 모든 탱크를 시지 모드로 전환할 수 있다.
    이미 만든 탱크도, 앞으로 만들 탱크도 모두 포함되낟.
    이렇게 한 클래스로 만들어진 객체에 일괄적으로 무언가를 적용하려면 인스턴스 변수가 아닌 클래스 변수를 정의해야 한다. 
    코드에서는 siege_developed라는 이름으로 클래스 변수를 정의한다.
    이때 정의 위치가 어딘지 꼭 확인하자.

(3) 시지 모드 개발이 완료됐다고 해서 모든 탱크가 항상 시지 모드여야 하는 것은 아니다.
    그래서 시지 모드인지 아닌지를 확인하기 위해 siege_mode라는 인스턴스 변수를 정의한다.
    처음에는 일반 모드일 테니 시지 모드를 해제 상태, 즉 False로 둔다.
'''

class Tank(AttackUnit): #(1) AttackUnit 클래스 상속
    siege_developed=False   #(2) 시지 모드 개발 여부, 클래스 변수로 정의

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode=False   #(3) 시지 모드(해제 상태), 인스턴스 변수로 정의

'''
클래스 변수는 클래스명과 함께 어디서든 사용할 수 있다.
Tank.siege_developed라고 하면 Tank 클래스의 클래스 변수에 직접 접근해 시지 모드가 개발됐는지를 확인할 수 있다.
또한, 인스턴스 변수가 객체마다 각각 다른 값을 가진다면 클래스 변수는 모든 객체가 동일한 값을 가진다는 점이 다르다.

정리하면 인스턴스 변수는 클래스의 메서드에 정의하거나 객체를 통해 직접 정의하며, 객체마다 서로 다른 값을 가질 수 있다.
반면에 클래스 변수는 클래스명 바로 밑에 정의하고 클래스로부터 만들어진 모든 객체에 값이 일괄 적용된다.

다음으로 시지 모드와 일반 모드를 전환하기 위한 set_siege_mode() 메서드를 정의한다.

(1) set_siege_moed() 메서드가 호출되면 현재 시지 모드가 개발됐는지를 먼저 확인한다.
    시지 모드가 개발되지 않았으면 호출한 곳으로 바로 되돌아간다.

(2) 시지 모드가 개발된 상태라면 탱크 객체의 시지 모드 설정 여부를 확인한다.

(3) 현재 일반 모드이면 시지 모드로 전환하고 공격력을 증가시키는 문구를 출력한다.

(4) 시지 모드이면 일반 모드로 전환하고 공격력을 감소시키고 필요한 문구를 출력한다.

(5) 마지막으로 인스턴스 변수인 siege_mode의 값을 Ture 또는 False로 변경해 시지 모드 설정 또는 해제 상태를 저장한다.
'''

class Tank(AttackUnit):
    siege_developed=False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode=False
    
    def set_siege_mode(self):   #t시지 모드 설정
        if Tank.siege_developed==False: #(1) 시지 모드가 개발되지 않았으면 바로 전환
            return 
        if self.siege_mode==False:  #(2) 시지 모드 여부 확인
            print("{0} : 시지 모드로 전환합니다.".format(self.name))   #(3) 시지 모드 전환  
            self.damage*=2      #(4) 공격력 2배 증가
            self.siege_mode=True    #(5) 시지 모드 설정
        else:   #현재 모드일 때
            print("{0} : 시지 모드를 해제합니다.".format(self.name))   #(4) 일반 모드 전환
            self.damage//=2 #(4) 공격력 2배 감소
            self.siege_mode=False   #(5) 시지 모드 해제

'''
공중 유닛을 위해 만든 Flyable 클래스는 수정할 필요가 없으므로 그대로 둔다.
공중 공격 유닛을 위한 FlyableAttackUnit 클래스는 move() 메서드에서 [공중 유닛 이동] 문구문 없앤다.
move() 메서드를 호출하면 실제로는 부모 클래스인 Flyable 클래스의\
fly() 메서드가 실행되면서 어느 방향으로 날아가는지를 출력하기 때문
'''

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
              .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

'''
마지막으로 전투기를 위한 Stealth 클래스를 만들자

(1) 전투기는 공중 공격 유닛이므로 FlyableAttackUnit 클래스를 상속받는다.

(2) 전투기는 은폐라는 특수 기술이 있어서 사용하면 상대방이 볼 수 없다.
    은폐 기술은 편의상 업그레이드가 완료됐다고 가정하자.
    부모 클래스인 FlyableAttackUnit 클래스의 생성자로 기본 정보를 설정한다.

(3) 은폐 여부를 확인하기 위해 cloacked 인스턴스 변수를 추가로 정의한다.

(4) 은폐 모드를 설정하기 위한 cloacking() 메서드를 정의한다.
    탱크의 시지 모드와 비슷하게 은폐 모드 여부에 따라서 설정(True)과 해제(False)하도록 if-else문으로 작성한다.

(5) 은폐 모드 설정 여부를 True 또는 Flase로 cloacked 인스턴스 변수에 저장한다.
    확인을 위한 문구도 함께 출력한다.
'''

class Stealth(FlyableAttackUnit):   #(1) FlyalbeAttackUnit 클래스 상속
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)   #(2) 부모 클래스 생성자로 기본 정보 설정
        self.cloacked=False #(3) 은폐 모드(해제 상태), 인스턴스 변수 정의
    
    def cloacking(self):    #(4) 은폐 모드를 메서드로 정의
        if self.cloacked==True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloacked=False #(5) 은폐 모드 해제
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloacked=True  #(5) 은폐 모드 설정

'''
지금까지 작성한 전체 코드이다.
게임이 작동하는 데 필요한 클래스를 모두 완성했다.
'''

class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛을 생성했습니다.".format(self.name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴됐습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]"\
              .format(self.name, location, self.damage))

class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1)
    
    def booster(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))

class Tnak(AttackUnit):
    siege_developed=False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode==False

    def set_siege_mode(self):
        if Tank.siege_developed==False:
            return 
        if self.set_siege_mode==False:
            print("{0} : 시지 모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.set_siege_mode=True
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name))
            self.damage//2
            self.siege_mode=False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
              .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)
        self.cloacked=False
    
    def cloacking(self):
        if self.cloacked==True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloacked=False
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloacked=True



#9.6.2 게임 실행하기
            
'''
지금까지 만든 클래스들을 사용해 게임을 실행해 보자.
게임 시작부터 종료까지 수행할 동작을 순차적으로 정리해보자.

게임 시작

유닛 생성(보병3, 탱크 2기, 전투기 1기)

전군 1시 방향으로 이동

탱크 시지 모드 개발

공격 준비(보병 강화제, 탱크 시지 모드, 전투기 은폐 모드)

전군 1시 방향 공격

전군 피해

게임 종료

동작을 하나씩 코드로 작성해보자.
'''


#게임 시작과 유닛 생성

'''
기존 코드 밑에 게임의 시작과 종료를 알리는 함수를 각각 정의한다.
게임을 하다가 이길 수 없다고 판단되면 졌지만 좋은 게임이었다는 의미로 채팅창에 'Good Game'을 입력하고 퇴장하도록 한다.
'''

#게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

#게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

'''
게임을 시작함과 동시에 보병 3기, 탱크 2기, 전투기 1기를 만든다.
객체명은 편의상 각 유닛 클래스명의 앞 두 글자와 숫자로 정의한다.
예를 들어, 보병은 Soldier의 so와 숫자를 더한 so1, so2, so3으로 한다.
'''

game_start()

#보병 3기 생성
so1=Soldier()
so2=Soldier()
so3=Soldier()

#탱크 2기 생성
ta1=Tnak()
ta2=Tank()

#전투기 1기 생성
st1=Stealth()

'''
실행하면 게임을 시작하고 종류별로 유닛을 생성한다.
유닛은 총 6기를 만들었다.
유닛을 각각 이동하려면 코드가 길어지니 유닛이 이동하거나 공격할 때 한꺼번에 처리하도록 리스트로 관리한다.
attack_units라는 이름으로 리스트를 만들고 모든 유닛을 추가한다.
'''

#유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units=[]
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)



#전군 이동과 탱크 시지 모드 개발

'''
유닛이 모였으니 적군을 공격하러 가보자.
1시 방향으로 모든 유닛을 이동하자.
모든 유닛은 Unit 클래스를 상속받았으므로 Unit 클래스의 move() 메서드를 사용할 수 있다.
또한, 모든 유닛은 리스트로 관리하고 있어서 반복문을 사용하면 편리한다.
'''

#전군 이동
for unit in attack_units:
    unit.move("1시")

'''
이동하는 와중에 탱크의 시지 모드 개발이 완료됐다고 가정하자.
탱크 자체도 굉장히 강하지만, 시지 모드의 화력은 그 이상으로 개발의 필요성이 있다.
Tank 클래스에 정의한 클래스 변수 siege_developed에는 Tank.siege_developed로 접근할 수 있고 값은 True로 설정한다.
'''

Tank.siege_developed=True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")



#공격 준비와 전군 공격

'''
전쟁 직전에 각 유닛의 특수 기술을 사용해 더 강력한 공격을 한다.
보병은 강화제, 탱크는 시지 모드, 전투기는 은폐 모드를 각각 사용한다.
리스트로 관리되는 유닛들이 서로 다른 기술을 사용해야 한다.
이들을 구분하려면 isinstance() 함수를 사용한다.

이 함수는 객레가 특정 클래스의 인스턴스인지를 확인할 수 있다.
각 유닛 객체가 Soldier 클래스의 인스턴스인지,\
Tank 또는 Stealth 클래스의 인스턴스인지를 확인해 각 유닛에 맞는 특수 기술을 사용하도록 한다.

형식
isinstance(객체명, 클래스명)
'''

#공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Soldier):
        unit.booster()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):
        unit.cloacking()

'''
공격 준비가 끝났다.
모든 유닛에 공격 명령을 내려 1시 방향을 공격하게 하자.
이때는 부모 클래스인 AttackUnit의 attack() 메서드를 활용하자.
'''

#전군 공격
for unit in attack_units:
    unit.attack("1시")



#전군 피해와 게임 종료

'''
공격하는 과정에서 우리 편도 피해를 입었다.
Unit 클래스의 damaged() 메서드를 호출하는데, 피해는 5~20의 난수 값을 지정한다.
random 모듈을 사용하기 위해 첫 줄에 import한다.
'''

from random import *

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20))

'''
우리 유닛들이 모두 전사했다고 가정하자.
본진에는 공격 유닛이 남아 있지 않아서 이대로는 승산이 없다.
패배를 인정하고 'Good Game'을 출력한 후 게임에서 나가자.
게임을 종료한다.
'''

#게임 종료
game_over()



#9.7 게임 최종 리뷰

'''
게임 프로젝트에 사용한 모든 클래스의 상속 관례를 정리해보자.

가장 기본이 되는 일반 유닛인 Unit 클래스를 공격 유닛인 AttackUnit 클래스가 상속받는다.
그리고 AttackUnit 클래스를 상속받아 지상 공격 유닛인 보병과 탱크를 위한 Soldier, Tank 클래스를 정의한다.
공중 유닛을 위해 비행 기능을 제공하는 Flyable 클래스를 정의한다.
공중 공격 유닛인 FlyableAttackUnit 클래스는 Flyable 클래스와 AttackUnit 클래스를 다중 상속받는다.
다시 FlyableAttackUnit 클래스를 상속받아 전투기 유닛을 위한 Stealth 클래스를 정의한다.

최하위에 위치한 Soldier, Tank, Stealth 클래스는 각 유닛이 보유한 특수 기술을 메서드로 정의한다.
공격, 이동, 피해 등 공통으로 처리되는 동작은 상속 관계에 따라 부모 클래스에 정의한 것을 그대로 사용한다.
공중 공격 유닛은 지상이 아닌 공중으로 날아서 이동하므로 Unit 클래스의 move() 메서드를 오버라이딩해\
Flyable 클래스의 fly() 메서드를 호출하도록 재정의한다.
재정의한 덕분에 모든 유닛은 지상과 공중 구분 없이 모두 move() 메서드로 이동 동작을 처리할 수 있다.

게임 전체 코드는 다음과 같다.
'''

from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛을 생성했습니다.".format(self.name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴됐습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]"\
              .format(self.name, location, self.damage))

#보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1)
    
    def booster(self):  #강화제: 일정 시간 동안 속도, 공격력 증가, 체력 10 감소
        if self.hp>10:
            self.hp-=10
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))

#탱크 유닛
class Tack(AttackUnit):
    #시지 모드: 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed=False   #시지 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode=False   #시지 모드(해제 상태)
    
    def set_siege_mode(self):
        if Tank.siege_developed==False: #시지 모드가 개발되지 않았으면 바로 전환
            return 
        #현재 일반 모드일 때
        if self.siege_mode==False:
            print("{0} : 시지 모드로 전환합니다.".format(self.name))
            self.damage*=2  #공격력 2배 증가
            self.siege_mode=True    #시지 모드 설정
        #현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name))
            self.damage//=2 #공격력 절반으로 감소
            self.siege_mode=False   #시지 모드 해제

#비행 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
              .format(self.name, location, self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

#전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)
        self.cloacked=False     #은폐 모드(해제 상태)
    
    #은폐 모드
    def cloaking(self):
        #현재 은폐 모드일 때
        if self.cloacked==True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloacked=False 
        #현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloacked=True

#게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

#게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

#실제 게임 진행
game_start()    #게임 시작

#보병 3기 생성
so1=Soldier()
so2=Soldier()
so3=Soldier()

#탱크 2기 생성
ta1=Tank()
ta2=Tank()

#전투기 1기 생성
st1=Stealth()

#유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units=[]
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta1)
attack_units.append(st1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시지 모드 개발
Tank.siege_developed=True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

#공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier):
        unit.booster()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):
        unit.cloacking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))

#게임 종료
game_over()




#9.8 실습 문제: 부동산 프로그램 만들기

'''
문제: 주어진 코드를 활용해 부동산 프로그램을 작성하세요.

class House:
    #매물 초기화: 위치, 건물 종류, 매물 종료, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    
    #매물 정보 표시
    def show_detail(self):
        pass

조건1:생성자로 인스턴스 변수를 정의한다.
    매물 정보를 표시하는 show_detail() 메서드에서는 인스턴스 변수를 순서대로 출력한다.

조건2:실행결과에 나온 3가지 매물을 객체로 만들고 총 매물 수를 출력한 뒤 show_detail() 메서드를 호출해 각 매물 정보를 표시함

실행 결과
총 3가지 매물이 있습니다.
강남 아파트 매매 10억 원 2010년
마포 오피스텔 전세 5억 원 2007년
송파 빌라 월세 500/50만 원 2000년

'''

class House:
    #매물 초기화: 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):    #(1) self.을 붙여 인스턴스 변수 정의
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, \
              self.price, self.completion_year) #(2) 인스턴스 변수의 값 순서대로 출력

houses=[]   #(3) houses 리스트 생성
house1=House("강남", "아파트", "매매", "10억 원", "2010년") #(4) House 클래스로 객체 3개 생성
house2=House("마포", "오피스텔", "전세", "5억 원", "2007년")
house3=House("강남", "빌라", "월세", "500/50만 원", "2000년")

houses.append(house1)   #(5) houses 리스트에 객체 추가
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다.".format(len(houses)))    #총 매물 수 출력
for house in houses:    #(7) 반복문으로 매물 정보 출력
    house.show_detail()

'''
해설

(1) House 클래스의 생성자는 전달값에 넘어온 값들로 인스턴스 변수를 만든다.
    인스턴스 변수는 앞에 self.을 붙여야 한다.

(2) show_detail() 메서드는 특별한 내용이 없으므로 print() 문으로 인스턴스 변수를 순서대로 출력만 하면 된다.

(3) 여러 매물을 관리해야 하므로 houses라는 리스트를 생성한다.
    여기서는 리스트에 추가될 매물 정보가 준비되지 않았으므로 값이 없는 빈 상태로 정의한다.

(4) House 클래스로 각 매물 정보를 전달해 객체 3개를 생성한다.

(5) 생성한 객체들을 append() 함수로 houses 리스트에 추가한다.

(6) 총 매물 수를 출력해야 하므로 print() 문을 작성한다.
    각 매물은 houses 리스트에 객체로 저장돼 있다.
    따라서 houses 리스트에 객체가 몇 개 있는지 확인하면 총 매물 수가 된다.
    문자열의 길이를 확인하는 len() 함수로 리스트의 길이를 확인한다.

(7) 마지막으로 각 매물의 정보를 표시하기 위해 객체별로 show_detail() 메서드를 호출한다.
    객체는 리스트로 관리하고 있으므로 반복문을 사용하면 같은 코드를 반복 작성하지 않고\
    짦은 코드로 원하는 동작을 구현할 수 있다.
'''

