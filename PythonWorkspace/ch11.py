#11장 모듈과 패키지




#11.1 모듈 다루기


'''
소프트웨어는 전체 프로그램을 바꾸지 않고 코드 일부만 교체하거나 추가할 수 있게 만들면\
유지보수도 쉽고 코드의 재사용성도 놓아진다.
파이썬에서는 서로 관련이 있거나 비슷한 기능을 하는 함수, 클래스 등을 담고 있는 파일을 제공-> 모듈(module)

자동차가 일체형이 아닌 부품(모듈)으로 이루어져 있으면 수리가 쉽듯, 파이썬에서도 개발을\
용이하게 하기 위해 프로그램의 기능을 독립적인 작은 단위로 나누는 작업-> 모듈화(modularization)

파이썬에는 이미 많은 모듈이 정의돼 있지만, 개발하다 보면 새로운 모듈이 필요할 때가 있다.
이 장에서는 직접 모듈을 만들어보자.
'''


#11.1.1 모듈 만들기

'''
작업 폴더에(PythonWorkspace 폴더) 안에 theater_module.py라는 이름으로 파이썬 파일을 새로 만든다.
이 파일에 사람 수에 따른 영화표 가격을 계산하는 함수 3개를 정의한다.

첫 번째 print() 함수에는 1인당 영화표 가격을 일반가 10000원
두 번째 price_morning() 함수에는 조조 할인가 6000원
세 번째 prcie_soldier() 함수에는 군 할인가 4000원으로 계산해 출력.

각 함수는 모두 사람 수를 의미하는 people을 전달받는다.
코드를 다음과 같이 작성한다.

#일반가
def price(people):
    print("{0}명, 영화표 가격은 {1}원입니다.".format(people, people*10000))

#조조 할인 가격
def price_morning(people):
    print("{0}명, 조조 할인 영화표 가격은 {1}원입니다.".format(people, people*6000))

#군인 할인 가격
def prcie_soldier(people):
    print("{0}명, 군인 할인 영화표 가격은 {1}원입니다.".format(people, people*4000))

Ctrl+S를 눌러 저장하면 이것으로 모듈 생성은 끝이다.
이제 이 파일을 다른 파일에서 가져다 사용할 수 있다.
'''



#11.1.2 모듈 사용하기

'''
생성한 모듈을 새로운 파일(ch11.py)에서 사용해보자.
주의할 점은 theather_module.py 파일과 모듈을 사용할 파일은 서로 같은 경로(같은 폴더)에 있어야 한다.

모듈을 사용하는 방법에는 가장 기본적인 import 문이 있다.
import 문을 작성할 때 파일명에 확장자 .py를 제외한 theather_module만 적으면 된다.-> 모듈명
import 문을 작성한 이후에는 모듈에 정의한 함수를 그대로 사용할 수 있다.
모듈에 속한 함수를 사용할 때는 모듈명 뒤에 점(.)을 찍고 나서 함수명을 적는다.

3개 함수를 호출해서 각각 3, 4, 5를 전달한다.
'''

import theater_module   #모듈 가져오기

theater_module.price(3) #3명
theater_module.price_morning(4) #조조 할인, 4명
theater_module.prcie_soldier(5) #군인 할인, 5명

'''
그런데 theater_module 모듈은 영어 단어 2개로 돼 있어서 모듈을 사용할 때마다\
긴 이름을 적기 귀찮다.
이럴 때 as로 모듈에 별명을 붙여 줄 수 있다.
movie를 줄여 mv라고 하자.
import 뒤에 as mv를 추가하면 theather_module이라는 모듈을 mv로 간단하게 호출할 수 있다.
실행 결과는 동일.
'''

import theater_module as mv #별명 mv로 사용

mv.price(3)
mv.price_morning(4)
mv.prcie_soldier(5)

'''
이번에는 from~improt 형식을 사용해보자.

형식
from 모듈명 import 기능(또는 함수)

from 뒤에 모듈명을 적고 모듈에서 가져다 사용할 기능이나 함수를 import 뒤에 적는다.
먼저 모든 기능을 가져다 쓴다.(*)
from~import 문으로 가져온 모듈은 모듈명과 점 부분을 적어 줄 필요 없이 모듈의 함수명만 적으면 된다.
'''

from theater_module import *    #모든 기능

price(3)    #theather_module 작성할 필요 없음
price_morning(4)
prcie_soldier(5)

'''
모든 기능이 필요하지 않을 때고 있다.
이럴 때는 from~import 문 뒤에 * 대신 사용하려는 함수명만 적는다.
가져올 함수가 여러 개일 때는 쉼표로 구분한다.

price() 함수와 price_morning() 함수만 가져와보자.
사람수는 5, 6, 7로 전달해 3개 함수를 모두 호출한다.
'''

from theater_module import price, price_morning #일부 함수만 가져와 사용

price(5)
price_morning(6)
#prcie_soldier(7)-> import 하지 않아서 사용 불가

'''
from~import 문에서도 as를 사용해 별명을 지을 수 있다.
price_morning() 함수명을 별명으로 바꾸자.
이때 price()와 price_morning() 함수는 가져오지 않으니 price를 별명으로 사용하자.

from~import 문 뒤에 as price를 추가하고 함수를 price()로 호출한다.
이제 실제로 호출하는 함수는 theather_module 모듈의 price()가 아니라 price_soldier()이다.
'''

#price_soldier를 별명인 price로 대체 사용
from theater_module import prcie_soldier as price
price(5)    #price_soldier() 함수 호출



#11.2 패키지 다루기


'''
파이썬에서는 패키지(package)가 있다.
여러 모듈을 모아 놓은 집합을 의미한다.
패키지는 보통 여러 모듈을 한 폴더 안에 담아 구성한다.

프로그램의 규모가 커지면 모듈 하나만으로 관리하기 어렵다.
그래서 관련 있는 기능끼리 모듈로 모으로 다시 모듈을 합쳐 패키지로 묶는다.
잘 만들어진 패키지가 있으면 파이썬 프로그램을 개발할 때 해당 패키지를 설치해 바로 사용할 수 있다.
그러면 어떤 기능이 필요할 때 코드를 처음부터 새로 작성할 필요가 없다.
'''



#11.2.1 패키지 만들기


'''
작업 폴더(PythonWorkspace) 안에 새로운 폴더를 하나 만들고 이름은 travel로 짓는다.
VSCode의 탐색기에서 작업 폴더명 옆에 New Folder 아이콘을 클릭하면 입력란이 나타난다.
여기에 travel을 입력한다.

여기서는 태국 패키지여행 상품을 위한 모듈인 thailand.py 파일과\
베트남 패키지여행 상품을 위한 모듈인 vietnam.py 파일을 만든다.
마지막으로 __init__.py 파일도 만든다.
이렇게 만든 3개 파일로 새로운 travel 패키지를 생성한다.

태국 패키지여행 상품을 위한 thailand.py 파일부터 내용을 채운다.
ThailandPackage라는 이름의 클래스를 만들고 detail()이라는 메서드를 정의한다.
이 메서드를 호출하면 태국 피키지여행 상품에 대한 요약 정보가 출력된다.


#tahiland.py

class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원")

        
vietnam.py 파일에 VietnamPackage라는 이름으로 베트남 패키지여행 클래스를 정의한다.


#vietnam.py

class VietnamPackage:
    def detail(self):
        print("[베트남 3박 5일 패키지 ] 다낭 효도 여행 60만 원")


__init__.py 파일은 일단 그대로 두고, ch11.py에서 travel 패키지를 사용해보자.
이때 앞에서 작성한 2개 파일은 반드시 저장해야 한다.


*__init__.py

__init__.py 파일은 해당 폴더가 패키지라는 것을 명시하기 위해 만든다.
폴더에 __init__.py 파일을 만들어 두면 해당 폴더를 패키지로 인식한다.
그런데 파이썬 3.3 버전부터는 이 파일이 없어도 상관없다.
다만, 호환성 문제를 위해 파일을 생성해 두는 것을 권장한다.
'''



#11.2.2 패키지 사용하기


'''
ch11.py 파일에서 travel 패키지를 사용해보자.
패키지명(travel) 뒤에 점을 찍고 모듈명(tahiland)을 적어 import 문으로 가져오면 된다.
그리고 ThailandPackage 클래스로 trip_to라는 객체를 만들어 detail() 메서드를 호출한다.
여기까지 작성하고 실행하면 다음과 같이 태국 패키지여행 상품에 대한 정보를 출력한다.
'''

import travel.thailand  #travel 패키지의 tahiland 모듈 가져오기

trip_to=travel.thailand.ThailandPackage()
trip_to.detail()

'''
import 문만 사용할 때는 대상이 모듈이나 패키지여야 하고 클래스나 함수는 가져올 수 없다.
그래서 다음과 같이 작성하면 오류가 발생한다.

import travel.thailand.TahilandPackage  #클래스 import 불가
trip_to=travel.thailand.ThailandPackage()
trip_to.detail()


그러나 from~import 문을 사용하면 함수부터 클래스, 모듈, 패키지까지 모두 import할 수 있다.
다음처럼 travel.thailand 모듈에서 ThailandPackage 클래스를 가져오도록 코드를 수정한다.
앞에서와 다르게 클래스를 import한 후 객체를 생성할 때는 travel.thailand. 부분은 제외하고 클래스명만으로 생성할 수 있다.
'''

#travel.thailand 모듈에서 TahilandPackage 클래스 가져오기
from travel.thailand import ThailandPackage

trip_to=ThailandPackage()   #from~import 문에서는 travel.thailand. 제외
trip_to.detail()


'''
베트남 패키지여행의 정보도 확인해보자.
travel 패키지에서 vietnam 모듈을 가져와보자.
다음과 같이 작성하면 패키지명 없이 모듈명(vietnam.)만으로 모듈 안에 있는 VietnamPackage 클래스에 접근할 수 있다.
'''

#travel 패키지에서 vietnam 모듈 가져오기
from travel import vietnam

trip_to=vietnam.VietnamPackage()    #travel. 생략
trip_to.detail()

'''
이처럼 패키지에서는 import 대상이 무엇이냐에 따라 접근하는 코드도 달라져야 한다는 점을 주의하자.
'''




#11.3 모듈 공개 설정하기:__all__


'''
from theater_module import *

taravle도 같은 방식으로 사용해보면 어떨까?
*를 사용해 travel 패키지의 모든 기능을 가져다 쓰겠다고 작성 후\
VietnamPackage 클래스의 객체를 만든다.
그리고 detail() 함수에 접근한다.

from travel import *

trip_to=vietnam.VietnamPackage()
trip_to.detail()

실행하면 'vietnam'이 정의되지 않았다며 오류가 발생한다.

패키지는 만든 사람이 공개 범위를 설정할 수 있다.
패키지에 포함된 모듈 중에서 import되길 원하는 것만 공개하고 나머지는 비공개로 둘 수 있다.

travel 패키지를 만들 때 함께 생성한 __init__.py 파일을 열어 다음과 같이 작성한다.
__all__이라는 변수에 리스트 형태로 모듈명을 넣으면 해당 모듈을 공개로 설정한다.
이때 all 앞뒤로 언더바 2개씩 적어야 한다.


#__init__.py

__all__=["vietnam"] #vietnam 모듈 공개


파일을 저장하고 코드를 다시 실행해보자.
이번엔 베트남 패키지여행 상품 정보가 잘 출력된다.
'''

from travel import *

trip_to=vietnam.VietnamPackage()    #베트남
trip_to.detail()

'''
태국 패키지여행 상품은 어떨까?
VietnamPackage 클래스의 객체 생성 부분을 주석 처리하고 다음 줄에 ThailandPackage 클래스의 객체를 만든다.

from travel import *

trip_to=thailand.ThailandPackage()
trip_to.detail()

실행하니 vietnam 모듈에서 발생한 오류가 모듈명만 바뀌어 똑같이 발생한다.
이는 __init__.py 파일의 __all__ 변수에는 현재 vietnam만 저장돼 있기 때문이다.
즉, vietnam 모듈만 공개돼서 thailand 모듈은 외부에서 사용할 수 없다.

오류를 해결해보자.
__init__.py 파일을 열고 __all__ 변수에 thailand 모듈을 추가한 후 저장하자.
이제 vietnam과 thailand 모듈 모두 공개로 설정한 상태이다.


#__init__.py

__all__=["vietnam", "thailand"] #vietnam, thailand 모듈 공개


코드를 다시 실행하면 이상 없이 접근해 코드가 제대로 동작한다.
'''

from travel import *

trip_to=thailand.ThailandPackage()  #태국
trip_to.detail()


'''
정확히 말하면 __all__은 from travel import *와 같이 *를 이용해 패키지 내 모든 모듈들을\
자겨다 쓰려고 하는 경우에 import할 대상을 정의하는 역할을 한다.
패키지 내에 __init__.py 파일이 없거나 __all__ 리스트 안에 아무런 모듈을 넣지 않더라도\
from travel import vietnam, thailand와 같이 작성하면 여전히 vietnam, thailand 모듈을 사용할 수 있다.
'''




#11.4 모듈 직접 실행하기


'''
travel 패키지의 thailand와 vietnam 모듈은 내용이 간단해서 파악하기 쉽지만,\
실제 프로그램에서 모듈을 만들면 규모나 복잡도가 다르다.
그래서 모듈의 기능이 올바르게 동작하는지를 확인하는 작업이 필요하다.

모듈을 직접 실행할지 아니면 별도 파일을 호출해서 실행할지는 다음과 같이 구분한다.
이때 __name__과 __main__은 앞뒤로 언더바 2개씩 들어간다.

형식
if __name__=="__main__":    #직접 실행하는 경우"
    pass
else:
    pass


__name__은 현재 모듈(작성한 파이썬 파일)의 이름을 값으로 가지는 내장 변수이다.
모듈이 직접 실행되는 경우 __name__의 값은 __main__으로 설정된다.
그래서 앞의 코드와 같이 작성하면 파일이 직접 실행될 때 if 문의 동작이 실행된다.

직접 실행되지 않고 외부에서 호출해 사용하면 __mian__이 아닌 해당 모듈의 이름을 값으로 가지게 된다.
그래서 값을 출력해 보면 __main__이 아닌 Thailand 같은 모듈명을 출력한다.

*내장 변수는 파이썬에서 어떻게 사용할지 역할이 이미 정의되어 있는 변수이다.


travel 패키지의 thailand.py 파일에서 ThailandPackage 클래스 정의 아래에 다음과 같이 코드를 추가한다.
__name__ 변수의 값이 __main__일 때, 즉 모듈을 직접 실행하는 경우에는\
if 문에서 출력문과 함께 ThailandPackage 클래스로 객체를 만들어 detail() 메서드를 호출한다.
그렇지 않을 때, 즉 모듈을 외부에서 호출하는 경우에는 else 문으로 처리해 호출 안내 문구만 간략히 출력한다.


#thailand.py

class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원")

if __name__=="__main__":    #모듈 직접 실행
    print("thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 출력돼요.")
    trip_to=ThailandPackage()
    trip_to.detail()
else:   #외부에서 모듈 호출
    print("외부에서 thailand 모듈 호출")


모듈을 직접 실행할 때부터 동작을 확인해보자.
thailand.py 파일을 열고 실행해서 결과를 보면 if 문의 조건에 해당하는 문장들이 실행되는 것을 볼 수 있다.

#결과

thailand 모듈 직접 실행
이 문장은 모듈을 직접 실행할 때만 출력돼요.
[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원


이번에는 작업 파일에서 thailand 모듈을 가져다 써보자.
'''

from travel import *

trip_to=thailand.ThailandPackage()
trip_to.detail()

'''
#결과

외부에서 thailand 모듈 호출
[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원

실행하면 thailand 모듈에 정의한 else 문의 print() 문이 실행되고 나서\
detail() 메서드가 실행된다.

여기서 배운 if __name__=="__main__": 구문을 잘 활용하면 모듈을 직접 실행할지\
외부에서 가져다 쓸지를 구분해 필요한 코드를 작성할 수 있다.
'''




#11.5 패키지와 모듈 위치 확인하기


'''
패키지나 모듈은 호출하려는 파일과 동일한 경로에 있거나\
파이썬 라이브러리(library)들이 모여 있는 폴더에 있어야 사용할 수 있다.
앞에서는 theather_module이나 travel 패키지가 이를 사용하는 파일(ch11.py)과 같은 위치에 있어서 문제가 없었다.

*라이브러리
    라이브러리는 재사용을 위해 개발한 코드 묶음으로 보면 된다.
    모듈 묶음이 패키지라면, 패키지 묶음은 라이브러리.
    사실 파이썬에서 라이브러리는 패키지와 혼용하는 용어라서 둘을 크게 구분하지 않아도 괜찮다.

모듈을 문제없이 사용하려면 모듈의 위치를 알아야 한다.
파이썬에서는 getfile() 함수로 모듈의 경로를 확인할 수 있다.

자주 언급한 random 모듈의 경로를 확인해보자.
getfile() 함수는 inspect라는 모듈에 속하므로 먼저 inspect 모듈을 import한다.
또한, random 모듈의 경로를 파악해야 하므로 random 모듈도 import한다.
그런 다음 getfile() 함수에 전달값으로 random을 넣은 후 실행하면 모듈의 경로를 반환한다.
'''

import inspect
import random

print(inspect.getfile(random))  #random 모듈 위치(경로)

'''
#결과

C:\Python38\lib\random.py

결과로  ranndom.py 파일의 경로가 표시된다.
1.1.1 파이썬 설치하기 에서 개발 환경을 설정할 때 지정한 파이썬 경로의 lib 폴더 안에 있는 것을 확인할 수 있다.
바로 이 폴더가 앞에서 말한 '파이썬 라이브러리들이 모여 있는 폴더'이다.

이번에는 직접 만든 travel 패키지의 thailand 모듈이 어느 경로에 위치하는지 확인해보자.
'''

import inspect
from travel import *

print(inspect.getfile(thailand))    #thailand 모듈 위치

'''
#결과

외부에서 thailand 모듈 호출
c:\Users\dhals_zn0ga5j\OneDrive\바탕 화면\PythonWorkspace\travel\thailand.py

실행해 보니 외부에서 thailand 모듈을 호출한다는 문구와 함께 경로가 표시된다.
이 책에는 pythonWorkspace 폴더의 travel 폴더 안에 thailand 모듈이 위치한다는 것을 알 수 있다.


*NameError 오류 발생 시
    실행했을 때 'NameError: name 'thailand' is not defined'라는 메시지가 나오면서\
    오류가 발생한다면 travel 패키지의 __init__.py 파일을 열고 __all__변수에\
    thailand 모듈이 다음처럼 잘 추가됐는지 확인한다.

    #__init__.py

    __all__=["vietnam", "thailand"]


패키지나 모듈은 '파이썬 라이브러리들이 모여 있는 폴더'에 모여 있으면 사용할 수 있다.
이를 확인하기 위해 travel 패키지를 lib 폴더로 복사해보자.
travel 패키지를 복사하기 위해 PythonWorkspace 폴더로 이동한다.

또는 VSCode의 탐색기에서 travel 폴더에 오른쪽 마우스를 클릭하고 메뉴에서\
Reveal in File Explore(파일 탐색기에 표시)를 선택한다.
그러면 PythonWorkspace 폴더가 바로 열리고 그 안에 있는 travel 폴더가 보인다.

윈도우 파일 탐색기에서 작업 폴더에 있는 travel 폴더를 복사해 random.py 파일이 존재하는 경로\
(여기서는 C:\Python38\lib)에 붙여 넣는다.

*윈도우 파일 탬색기에서는 lib 폴더명이 Lib으로 표시될 수도 있다.

그리고 작업 중인 폴더에 있는 travel 폴더는 임시로 폴더명을 travel_temp로 변경한다.
travel 폴더에서 마우스 오른쪽 버튼을 클릭해 나오는 메뉴에서 Rename(이름 바꾸기)을 선택하면 폴더명을 바꿀 수 있다.

폴더명을 바꾸고 나면 패키지명이 변경되므로 VSCode에서 코드에 있는 travel 부분을 travel_temp로\
일괄 수정해 주는 기능의 안내창이 뜬다.
여기서는 바꿀 필요가 없으므로 Skip Changes(변경 내용 건너뛰기) 버튼을 클릭한다.
OK 버튼을 클릭하면 바뀐 폴더명으로 코드가 변경되어 제대로 테스트할 수 없다.

이 상태에서 다시 ch11.py 파일을 실행하면 thailand 모듈의 경로가 바뀐 것을 볼 수 있다.


#ch11.py

import inspect
from travel import *

print(inspect.getfile(thailand))    #thailand 모듈 위치


#결과

외부에서 thailand 모듈 호출
C:\python38\lib\travel\thailand.py


이는 호출하려는 파일과 같은 경로가 아닌 파이썬 설치 경로의 lib 폴더에 있는 패키지에서\
모듈을 불러와 사용하고 있다는 뜻이다.
또한, 현재 파일이 아닌 새로운 파이썬 프로그램을 만들어 작성할 때도 travel 패키지를 가져다 쓸 수 있다는 의미이다.

확인이 끝나면 다음 실습을 위해 lib 폴더에 붙여 넣은 travel 폴더(C:\python38\lib\travel)는 삭제하고.\
VSCode에서 이름을 바꾼 travel_temp 폴더는 다시 travel로 원상 복귀한다.
'''




#11.6 패키지 설치하기



'''
파이썬의 강점 중 하나는 유용한 패키지가 아주 많다는 점이다.
그래서 파이썬으로 개발할 때 어떤 기능이 필요하다면 처음부터 무작정 개발하기보다\
이미 잘 만들어진 패키지가 있는지 확인해 보는 것이 좋다.

가령 무작위로 어떤 수를 뽑는 기능이 필요하다고 해보자.
처음부터 구현할 수도 있지만, 개발하는 과정에서 실수할 수도 있고 고려할 부분이 생각보다 많을 수도 있다.
이미 많은 사람이 사용하고 충분히 검증받은 random 모듈을 사용하면 된다.
그러면 원하는 기능이 있을 때 해당 패키지가 있는지 어떻게 알 수 있을까?

이번엔 필요한 파이썬 패키지를 찾는 방법을 알아보자.
웹 브라우저를 열고 주소창에 http://pypi.org를 입력하면 페이지가 열린다.
PyPI(The Python Package Index)는 파이썬 전용 패키지 저장소이다.

검색창 아래에 있는 browse project를 클릭해 프로젝트를 자세히 살펴보자.
왼쪽 항목에서 Topic을 클릭하면 개별 주제들이 보인다.
Communications, Database, Internet 등 다양한 주제가 있다.
이 중에서 원하는 주제를 선택하면 해당하는 프로젝트 목록이 오른쪽에 나타난다.

또는 상단 검색창에서 직접 패키지를 찾을 수도 있다.
원하는 검색어를 입력하면 관련 패키지가 화면에 나온다.
실습을 위해 웹 스크래핑 분야에서 아주 유명한 BeautifulSoup4라는 패키지를 찾아 설치해보자.
검색창에 beautifulsoup을 입력하면 beautifulsoup4 버전 정보를 표시하는 프로젝트를 클릭한다.

개별 프로젝트 화면은 보통 다음과 같이 구성된다.
왼쪽 위에 패키지를 설치하는 명령이 있고 본문에는 프로젝트에 대한 설명과 예제 코드를 제공한다.
다음으로 패키지를 설치해보자.
먼저 왼쪽 위에 있는 패키지 설치 명령을 복사한다.
명령 옆에 있는 버튼을 클릭하면 복사한다.

VSCode의 터미널에서 마우스 오른쪽 버튼을 클릭하거나 Ctrl+V를 눌러 복사한 명령을 붙여 넣는다.
그리고 enter를 누르면 패키지가 설치된다.

설치가 끝나면 프로젝트 페이지의 Quick start에 나온 예제 코드를 복사한다.

from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
>>> print(soup.prettify())

복사한 코드를 VSCode에서 작업 중인 파일에 붙여 넣는다.
이때 각 문장 앞에 있는 >>> 부분은 제외한다.


*일부 경고 메시지가 발생할 수 있지만, 무시해도 된다.
    경고 메시지는 BeautifulSoup4 동작에 관한 내용이다.
    이 절에서는 신규 패키지 설치와 사용법을 설명하고 있다.
    그래서 실습을 위해 해당 패키지를 설치했을 뿐 BeautifulSoup4가 어떤 패키지이고 예제 코드가 어떤 동작을 하는지는 몰라도 무관!
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

'''
#결과

<p>
    some
    <b>
        bad
        <i>
            HTML
        </i>
    </b>
</p>


실행해 보면 프로젝트 페이지의 예제 코드 아래에 있는 내용을 출력하는 것을 확인할 수 있다.
BeautifulSoup4 패키지를 설치할 때 사용한 pip 명령은 패키지 설치 외에도 다양한 명령을 수행할 수 있다.

*pip 명령 사용 방법

옵션                설명                사용법

install             패키지 설치         pip install[패키지명]
install --upgrade   패키지 업그레이드    pip install --upgrade[패키지명]
uninstall           패키지 삭제         pip uninstall[패키지명]
list                설치 패키지 목록     pip list
show                패키지 상세 정보     pip show
'''




#11.7 내장 함수 사용하기


'''
파이썬은 프로그램을 더 빠르고 편리하게 개발할 수 있도록 유용한 기능을 담은\
내장 함수와 외장 함수를 제공한다.
내장 함수는 별도로 import하지 않고도 사용할 수 있는 함수이다.
사용자에게 입력받을 때 사용하는 input() 함수도 내장 함수에 해당한다.

사용자에게 좋아하는 언어를 입력받아 문장을 출력하는 코드를 만들어보자.
'''

language=input("어떤 언어를 좋아하세요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))

'''
프로그램을 실행해 터미널에 '파이썬'을 입력하면 language라는 변수에 이 값을 저장했다가\
print() 문으로 가져와 출력한다.
이때 input() 함수를 사용하기 위해 별도로 해야 하는 일은 아무것도 없다.

input() 함수 외에도 내장 함수는 종류가 굉장히 많다.
그중 하나인 dir() 함수를 사용해보자.

dir() 함수는 어떤 객체를 전달값으로 넘기면 이 객체가 어떤 변수와 함수를 가지고 있는지 알려 준다.
만약 전달값으로 아무것도 넣지 않으면 현재 소스 코드 안에서 사용할 수 있는 모듈 또는 객체를 출력한다.
비교하기 위해 import하지 않았을 때와 random, pickle 모듈을 import했을 때 dir() 함수의 실행결과를 확인한다.
'''

print(dir())
import random   #random 모듈 가져다 쓰기
print(dir())
import pickle   #pickle 모듈 가져다 쓰기
print(dir())

'''
실행해 보면 처음에는 기본값만 출력되고 random 모듈을 import한 후에는 random 모듈을,\
pickle 모듈을 import한 후에는 pickle 모듈까지 출력한다.

이번에는 random 모듈을 직접 전달값으로 설정해보자.
'''

import random
print(dir(random))

'''
결과로 random 모듈 안에 있는 모든 것을 출력한다.
앞에서 이미 사용해 본 randint(), randrange(), sample(), shuffle() 등이 보인다.

이번에는 모듈이 아닌 리스트 자료구조를 하나 만들어서 확인해본다.
lst라는 이름의 리스트를 만들고 숫자 몇 개를 저장해 전달한다.
'''

lst=[1,2,3]
print(dir(lst))

'''
실행하면 리스트에서 사용할 수 있는 변수와 함수 목록이 나온다.
리스트 자료구조를 공부할 때 본 append(), clear(), count(), extend(), index(), reverse(), sort() 등이 있다.

이번에는 더 기본적인 문자열 변수 하나를 만들어서 확인해보자.
name이라는 변수에 문자열을 값으로 넣고 dir() 함수로 확인한다.
'''

name="jim"
print(dir(name))

'''
훨씬 더 다양한 내용이 출력된다.
name이라는 문자열 변수의 값을 대문자로 변경하는 upper(), 소문자로 변경하는 lower(),\
특정 문자를 찾는 find() 등 다양한 함수를 사용할 수 있음을 확인할 수 있다.
'''




#11.8 외장 함수 사용하기


'''
외장 함수는 파이썬을 설치할 때 함께 설치되어 11.5 패키지와 모듈 위치 확인하기에서\
다룬 lib 폴더에 담겨 있다.
하지만 외장 함수는 내장 함수와 다르게 반드시 import해야만 프로그램 안에서 사용할 수 있다.

파이썬에서 제공하는 모듈을 살펴보려면 구글에서 'list of python modules'로 검색하거나\
파이썬 공식 홈페이지의 모듈인덱스 페이지를 방문하면 된다.
내장 함수와 마찬가지로 파이썬에서 사용할 수 있는 모듈 목록이 알파벳순으로 정렬돼 있다.

목록에서 모듈 하나를 선택하면 사용 가능한 함수들과 예제 코드를 볼 수 있다.
예를 들어, random 모듈에서 사용 가능한 함수 정보를 확인하고 싶다면 상단 인덱스에서 r을 클릭한다.

모듈 상세 페이지에는 모듈 정보와 모듈 파일의 위치(Lib/random.py)가 표시된다.
아래로 갈수록 모듈에 속한 함수들과 예제 코드들을 확인할 수 있다.
모듈은 굉장히 유용해서 많이 알면 알수록 좋지만, 모두 외울 수는 없다.
한 번쯤 어떤 모듈이 있는지 모듈명 정도는 훑어보는 것을 추천한다.
'''


#11.8.1 폴더 또는 파일 목록 조회 모듈


'''
glob 모듈은 어떤 경로에 있는 폴더 또는 파일 목록을 조회할 때 사용한다.
윈도우의 명령 프롬프트에서 사용하는 dir 명령과 비슷하다.
glob 모듈에는 glob()이라는 함수가 있는데, 파일명 또는 비슷한 형태를 전달하면 해당하는 파일을 조회한다.

확장자가 py인 파일 목록을 출력해보자.
glob 모듈을 import해서 가져오고 glob() 함수에는 *.py를 넣어 전달한다.

*는 모든 것을 지칭할 때 사용하는 와일드 카드 문자이므로 *와 파이썬 파일 확장자인 py를 합치면\
확장자가 py인 모든 파일을 의미한다.
'''

import glob

print(glob.glob('*.py'))    #확장자가 py인 모든 파일 출력

'''
실행하면 현재 작업 폴더에 존재하는 .py로 끝나는 모든 파일을 출력한다.
'''



#11.8.2 운영체제의 기본 기능 모듈


'''
os는 운영체제에서 제공하는 기본 기능 정도로 생각하면 된다.
예를 들어, 폴더를 만들거나 삭제하는 기능이다.

os 모듈을 import하고 getcwd() 함수를 호출해보자.
getcwd() 함수는 os 모듈에 속한 함수로, 현재 파이썬 파일을 실행하는 경로 정보를 알려 준다.
여기서 cwd는 현재 작업 폴더(current working directory)를 의미한다.
'''

import os

print(os.getcwd(os))    #현재 작업 폴더 위치(경로)

'''
이번에는 폴더를 하나 만들어 보자.
2가지 함수를 사용하는데, 먼저 exists() 함수는 주어진 경로에 해당하는 폴더 또는 파일이 존재하는지를 알려 준다.
makedirs() 함수는 현재 위치에 폴더를 새로 생성한다.

folder라는 변수에 sample_dir이라는 문자열을 값으로 넣는다.
exists() 함수로 folder 변수와 같은 이름의 폴더가 존재하는지를 확인한다.
같은 이름의 폴더가 존재하지 않으면 makedirs() 함수로 새로운 폴더를 생성한다.


*path는 경로 정보를 처리하기 위해 os 모듈에서 import해서 사용하는 또 다른 모듈이다.
os 모듈에서 path 모듈, 즉 모듈에서 모듈을 호출할 때 is.path.exists()와 같이 점으로 연결해 코드를 작성한다.
'''

import os

folder="sample_dir"

if os.path.exists(folder):  #같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
else:   #폴더가 존재하지 않으면
    os.makedirs(folder) #폴더 생성
    print(folder, "폴더를 생성했습니다.")

'''
#결과

sample_dir 폴더를 생성했습니다.


코드를 실행하면 폴더를 생성했다는 메시지가 출력된다.
그리고 VSCode 탐색기를 보면 작업 폴더에 sample_dir이라는 폴더가 생성돼 있다.
앞의 코드를 다시 한번 실행하면 sample_dir 폴더가 존재하므로 출력 내용이 달라진다.

#결과

이미 존재하는 폴더입니다.


같은 이름의 폴더가 있으면 해당 폴더를 삭제하도록 코드를 조금 수정하자.
이때는 os 모듈의 rmdir() 함수를 사용한다.
if 문에서 rmdir() 함수를 호출하면서 folder 변수를 전달해 전달값과 같은 이름의 폴더를 삭제한다.

코드를 다시 실행하면 sample_dir 폴더가 삭제되며 관련 문구가 출력된다.
'''

import os

folder="sample_dir"

if os.path.exists(folder):  #같은 이름의 폴더가 존재하면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)    #폴더 삭제
    print(folder, "폴더를 삭제했습니다.")   #삭제 문구 출력
else:   #폴더가 존재하지 않으면
    os.makedirs(folder) #폴더 생성
    print(folder, "폴더를 생성했습니다.")

'''
#결과

이미 존재하는 폴더입니다.
sample_dir 폴더를 삭제했습니다.


os 모듈에는 listdir() 함수도 있다.
glob 모듈의 glob() 함수와 비슷하게 현재 작업 폴더 안에 있는 폴더와 파일 목록을 출력한다.
'''

import os

print(os.listdir()) #현재 작업 폴더 안의 폴더와 파일 목록 출력




#11.8.3 시간 관련 모듈


'''
이번에는 시간 관련 함수를 제공하는 time 모듈을 사용한다.
time 모듈을 import하고 나서 현재 시간 정보를 반환하는 localtime() 함수를 호출한다.
'''

import time

print(time.localtime())

'''
실행결과에 무언가 나오기는 하는데 알아보기 힘들다.
이때 time 모듈에 있는 strftime() 함수는 사용자가 원하는 문자열 형태로 시간 정보를 출력한다.
이때 주로 사용하는 코드와 의미는 다음과 같다.


코드    의미

%Y      연(year)
%m      월(month)
%d      일(day)
%H      시(hour)
%M      분(minute)
%S      초(second)

가령 날짜와 시간 정보를 '2023-01-02 22:00:00'와 같이 출력하려면\
각 자리에 맞게 코드를 입력하고 코드 사이에 하이픈(-)과 콜론(:)을 적절한 위치에 넣는다.
이때 코드는 대소문자를 구분하므로 주의한다.
'''

import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))   #연-월-일 시:분:초

'''
time과 비슷한 datetime 모듈도 있다.
다음과 같이 작성하면 datetime 모듈을 사용해 오늘 날짜를 출력할 수 있다.
'''

import datetime

print("오늘 날짜는 ", datetime.date.today())

'''
datetime 모듈에는 timedelta() 함수도 있다.
두 날짜 및 시간 차이를 계산하거나 일정 시간이 경과한 후의 날짜 등을 구할 수 있다.

오늘로부터 100일 째 되는 날을 계산한다고 가정하자.
먼저 datetime.date.today()를 사용해 오늘 날짜를 가져와 today라는 변수에 저장한다.

그리고 timedelta() 함수를 호출하는데, 100일 뒤가 며칠인지 계산하기 위해 days라는 키워드 인자에 100을 넣는다.
이때 반환하는 값을 td 변수에 저장한다.
마지막으로 print() 문으로 today 변수와 td 변수의 값을 더해 출력한다.
'''

import datetime

today=datetime.date.today() #오늘 날짜 저장
td=datetime.timedelta(days=100) #100일째 날짜 저장
print("우리가 만난 지 100일은", today+td)   #오늘부터 100일 후 날짜

'''
파이썬으로 개발할 때 처음부터 끝까지 모든 기능을 직접 구현하려고 하지 말고,\
구글 검색으로 이미 누군가가 잘 만들어 놓은 유용한 라이브러리(패키지, 모듈)을 찾아보자.

우리에게 이미 필요한 라이브러리는 대부분 이미 존재하고, 지금 이 시간에도 새로운 라이브러리가 계속 만들어지고 있다.
모든 기능을 구현하는 것도 중요하지만, 필요한 라이브러리를 잘 찾아서 프로젝트에 적용하는 것도\
개발자의 덕목이자 개발 생산성을 향상시킬 수 있는 훌륭한 전략이다.
'''




#11.9 실습 문제: 나만의 모듈 만들기


'''
*문제: 프로젝트에 나만의 서명을 남기는 모듈을 만들어보자.

*조건
    모듈 파일명은 byme.py로 짓는다.
    실행했을 때 실행결과가 다음과 같이 나오도록 모듈을 작성한다.

*실행 결과

import byme

byme.sign()

이 프로그램은 나도코딩이 만들었습니다.
유튜브 : http://www.youtube.com/@nadiocoding
이메일 : nadocoding@gmain.com
'''

import byme

byme.sign()

'''
*해설

VSCode에서 byme.py라는 새로운 파일을 생성한다.
byme 모듈에는 조건에 주어진 대로 sign() 함수를 정의한다.

sign() 함수의 역할은 아주 단순하다.
실행결과에 나온 3줄을 출력만 하면 된다.
따라서 함수 안에 안내 문구를 출력하는 print() 문을 작성한다.

byme.py 파일을 저장하고 ch11.py 파일에 와서 조건에 제시한 코드를 작성한다.
byme 모듈은 작업 파일과 같은 경로에 있으므로 import만 하면 바로 사용할 수 있다.

조건에 나온 대로 byme 모듈을 import하고 sign() 함수를 호출한다.
실행하면 byme 모듈이 정상적으로 import돼 작성한 서명 문구를 출력하는 것을 확인할 수 있다.


#byme.py

def sign():
    print("이 프로그램은 나도코딩이 만들었습니다.")
    print("유튜브 : http://www.youtube.com/@nadiocoding")
    print("이메일 : nadocoding@gmain.com")
'''

