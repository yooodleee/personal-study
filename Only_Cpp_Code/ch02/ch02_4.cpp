// 02-4. 키워드와 리터럴


/*
이제 C++ 언어에서 변수를 정의하고 데이터를 올바르게 저장하는 방법을 알았을 것이다. 
이 절에서는 변수에 넣는 데이터 그 자체를 다룬다. 그리고 C++ 언어에서 제공하는 각종 키워드에는 무엇이 있는지도 소개한다. 
*/


/*
미리 정의된 키워드

키워드(keyword)란 프로그래밍 언어에서 특별한 의미로 미리 정의해 둔 식별자다. 
C++ 언어의 대표적인 키워드를 나열하면 다음과 같다. C++ 20 기준으로 97개 단어가 키워드로 등록되어 있다.

<C++ 키워드>
    break, catch, char, class, const, continue, delelte, do, double, dynamic_cast
    else, explicit, export, extern, FALSE, float, for, friend, if, inline, ,int, long
    mutable, namespace, new, operator, private, protected, public, return, short, signed
    sizeof, static, struct, switch, template, this, throw, TRUE, try, typeof, unsigned
    using, void, wchar_t, while, .... 


char, int, float 등 각종 데이터 형식을 비롯해 using, return 등 눈에 익은 키워드들이 보일 것이다. 
변수, 함수, 클래스 등 식별자를 정의할 때 미리 정의된 키워드와 똑같은 이름으로 만들 수 없다. 
식별자를 만들 때는 다음 규칙에 따라야 한다. 이 규칙을 어긴다면 컴파일러에서 오류가 발생한다. 
    * 키워드는 식별자로 사용할 수 없다. 
    * 식별자는 대소 문자, 숫자, 문자로만 구성할 수 있다. 
    * 식별자는 대소 문자 또는 밑줄(_)로만 시작해야 한다(숫자로 시작할 수 없음). 
    * 대문자와 소문자를 구별한다(nvalue, NVALUE, nValue 각각 다르게 취급). 
*/



/*
값 그 자체를 나타내는 리터럴

리터럴(literal)이란 코드에 직접 표현된 변하지 않는 값 그 자체를 의미한다. 
예를 보면서 설명을 이어가겠다. 

int value = 5;
double value = 0.5;
char value = 'A';

코드에서 5, 0.5, 'A'가 모두 리터럴이다. 
리터럴도 데이터 형식을 가진다. 
기본적인 리터럴 형식은 다음과 같다. 
참고로 부동 소수점 리터럴의 기본 데이터 형식은 float가 아니라 double이다. 

<리터럴 형식> 
    1. 문자: char --> 'A'
    2. 정수: int --> 0, 1, 2, -1, -2
    3. 부동 소수점: double --> 0.5, 0.1, -0.1
    4. 문자열: char[] --> "Hello", "안녕하세요"
    5. 불리언: bool --> true, false

기본 리터럴 외에도 다음처럼 별도의 접미사를 붙여 지정할 수 있는 리터럴도 있다. 

float value = 0.5;
unsigned int value = 5u;
long value = 5L;

<리터럴 접미사>
    1. unsigned int: u, U
    2. long: l, L
    3. unsigned long: ul, uL, Ul, UL, lu, Lu, lU, LU
    4. long long: ll, LL
    5. unsigned long long: ull, uLL, Ull, ULL, llu, llU, LLu, LLU
    6. float: f, F
    7. long double: l, L


* 접미사를 안 쓰면 어떻게 될까?
    리터럴에서 접미사는 선택 사항으로 생략해도 컴파일은 된다. 
    이때 컴파일러는 해당 리터럴의 데이터 형식을 유추하여 임의로 지정한다. 
    다음 코드처럼 접미사 f를 생략하면, 컴파일러는 R-value인 0.5를 float가 아닌 double로 처리한다. 
    따라서 의도치 않게 정밀도 문제가 발생한다. 
    리터럴 접미사를 명시해 데이터 형식을 확실하게 지정하는 것이 좋다. 

    float value = 0.5;      // float가 아닌 double로 처리
*/


/*
문자열 표현 방식

잠시 C++ 언어에서 문자열 표현 방식을 알아보겠다. 
먼저 C 언어에서 문자열은 다음과 같이 선언한다. 

char *str = "Hello";
char str[] = "Hello";

이 코드는 내부적으로는 char 배열을 만들고, 해당 배열에 문자를 하나씩 저장합니다. 
그리고 배열의 맨 마지막에는 문자열의 끝을 알리는 널 문자(\0)를 저장한다. 

C++ 역시 C 언어를 계승했으므로 C의 문자열 선언 코드와 구조를 그대로 사용할 수 있다. 
하지만 C++ 언어에서는 문자열을 좀 더 편리하게 다룰 수 있도록 표준 라이브러리 형태인 string 클래스를 지원한다. 
이 클래스에는 문자열과 관련한 다양한 함수를 제공한다. 

    #include <iostream>
    // #include <string>    // iostream 헤더에 string도 포함됨

    using namespace std;

    int main()
    {
        string string_value("Hello");
        cout << string_value << endl;

        string_value = "World";
        cout << string_value << endl;

        return 0;
    }

    먼저 string 형식의 변수를 사용하려면 std::string에 대한 헤더를 #include <string>처럼
    포함해 줘야 한다. 그리고 string 형식의 변수에는 문자열 데이터를 자유롭게 넣을 수 있다. 
*/

