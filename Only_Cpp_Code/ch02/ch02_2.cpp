// 02-2. 데이터 형식


/*
프로그래밍에서 말하는 변수란 '값을 저장할 수 있는 공간'이다.
C++ 언어에서는 변수에 값을 저장하기 전에 정수, 부동 소수점, 문자 등 어떤 값을 저장할지 미리 정해주어야 한다.
이를 데이터 형식(data type)(자료형)이라고 한다.
데이터 형식은 프로그래밍에서 가장 기본적인 요소다.

파이썬 같은 인터프리터 언어는 변수의 형식을 자동으로 결정해 준다.
반면에 C, C++ 같은 컴파일 언어는 형식을 직접 지정해 주어야 한다.
형식이 엄격한 언어는 변수를 선언하고 사용할 때 어떤 형식으로 만들지 항상 고민해야 한다.
파이썬처럼 형식이 유연한 언어보다 훨씬 까다롭지만, 런타임 오류도 줄고 메모리를 효율적으로 이용할 수 있다는 장점이 있다.
*/

/*
C++의 데이터 형식 분류


C++ 언어의 데이터 형식은 크게 5가지로 분류할 수 있다.
각 분류에 속하는 주요 형식은 다음과 같다.
세부 형식은 이보다 많지만 자주 사용하는 것 위주로 정리했다.

C++ 데이터 형식

    1) 보이드
        - void: (none)
            void는 형식 없음을 의미함.

    2) 불리언
        - bool: (1)
            true, false 표현, C 언어에서도 지원(C99, stdboolh)

    3) 문자
        - char: (1)
            8비트 정수형으로 사용할 경우 일반적으로는 -128 ~ 127, 
            C++ 언어 표준에서는 적어도 -127 ~ 127 범위 지정
        - unsigned char: (1)
            0 ~ 255
        - signed char: (1)
            부호 비트를 가지도록 명시적 표현
        - char8_t: (1)
            C++20의 새 형식
        - char16_t: (2)
            UTF-16 문자 표현에 사용
        - char32_t: (4)
            UTF-32 문자 표현에 사용
        - wchar_t: (2)
            와이드 문자(wide character) 표현
        - __wchar_t: (2)
            마이크로소프트 전용

    4) 정수
        - short: (2)
            적어도 char보다는 크기가 큰 정수 형식
        - unsigned short: (2)
            양수만 저장
        - int: (4)
            일반적으로 가장 많이 사용하는 정수 형식
        - unsigned int: (4)
            양수만 저장
        - __int8, __int16, __int32, __int64: (1), (2), (4), (8)
            마이크로소프트 전용 정수 형식
            __int8은 char와 동일하게 취급
            __int16은 short, __int32는 int, __int64는 long long과 같은 데이터 형식으로 간주
        - long: (4)
            long의 경우 32비트 운영체제에서는 4byte(32bit),
            64비트 운영체제에서는 8byte(64bit)인데, 윈도우 64bit에서는 long도 4byte로 취급
        - unsigned long: (4)
            양수만 저장
        - long long: (8)
            int 형 연산에서 초과되는 범위를 다룰 때 사용
            적어도 8byte 이상의 크기를 보장(C++11 이후)
        - unsigned long long: (8)
            양수만 저장

    5) 부동 소수점
        - float: (4)
            C++ 언어에서 가장 작은 부동 소수점 형식
        - double: (8)
            float보다 큰 부동 소수점 형식
            소수를 구해야 하는 연산에서는 double이 소수점 아래 표현을
            더 많이 할 수 있으니 double을 추천
        - long double: (8)
            GCC, G++ 에서는 long double이 16byte
*/

/*
* __int8, __int16, __wchar_t는 어떤 형식인가?

데이터 형식 앞에 '__' 이 붙는 것은 마이크로소프트에서 제공하는 확장형이다.
C++ 표준은 아니며 마이크로포스트 비주얼 C++ 컴파일에서만 인식할 수 있다.
이러한 마이크로포스트 확장형은 특정 환경에서만 지원되며 호환성이 떨어질 수 있으므로 이를 대체하는 int8_t, wchar_t 같은
표준 C++ 자료형을 사용하는 것이 좋다.
*/

/*
형식이 없음을 나타내는 void

C++에서 void는 형식이 없음을 타나낸다.
따라서 void 형으로는 다음처럼 변수를 선언할 수 없다.

ex) void형 변수 선언(컴파일 오류)
    void value;

그럼 void 형은 언제 사용할까?
void 형은 3가지 상황에서 사용한다. 첫 번째는 함수가 값을 반환하지 않음을 표시할 때다.
다음 코드에서는 print_func 함수에는 값을 반환하는 return 문이 없다.
이처럼 반환값이 없는 함수를 선언할 때 void를 사용한다.

ex) 함수가 값을 반환하지 않을 때
    void prinf_func()
    {
        std::cout << "func" << std::endl;
    }

두 번째는 함수의 매개변수가 없음을 표시할 때이다.
물론 함수의 매개변수가 없으면 아무것도 입력하지 않은 채 () 처럼 빈 괄호로 두어도 된다.
하지만 다음 코드처럼 void로 표시하면 매개변수가 없음을 명시적으로 나타낼 수 있다.

ex) 매개변수가 없음을 표시할 때
    int input_func(void)
    {
        int input_value;
        std::cin >> input_value;
        
        return input_value;
    }

세 번째는 어떤 변수라도 가리킬 수 있는 제네릭 포인터(generic pointer)를 만들 때 사용할 수 있다.
제네릭 포인터에서 void는 단순히 '형태가 없음'을 의미하기 보다 '형태가 자유로움'을 의미한다고 이해하는 편이 좋다.

ex) 모든 자료형을 가리킬 수 있는 제네릭 포인터로 사용할 때
    int int_value;
    float float_value;
    void *ptr_value;
    
    ptr_value = &int_value;
    ptr_value = &float_value;

*/

/*
참, 거짓만 가지는 bool 형식

bool은 참(true: 1)과 거짓(false: 0)만 가질 수 있는 형식이다.
bool 형 변수에 true나 false 값을 초기화하거나 할당할 수 있지만, 실제로는 키워드가 아닌 정수로 저장된다.
true는 정수 1, false는 정수 0을 의미한다.
*/

/*
문자 형식

char는 C, C++ 언어에서 문자를 다룰 때 사용하는 대표적인 데이터 형식이다.
하지만 사실 char는 8bit(=1byte) 정수를 저장하는 역할을 할 뿐, 문자 전용 데이터 형식은 아니다.
char에 저장된 값은 아스키(ASCII) 코드로 변환하여 사용할 수 있다.

아스키 코드를 보면 문자를 출력할 수 있는 것은 32 ~ 126 번까지다.

문자를 표현하는 데 char를 사용하는 이유는 아스키 코드가 7bit 형태의 체계를 따르고 있어서다.
나머지 1bit는 통신 확인용 패리티(paritiy) 비트다.
즉, char가 아스키 문자를 저장할 떄는 0 ~ 127 사이의 값을 가진다.
만약 char를 8bit 정수 저장용으로 사용한다면 1bit를 부호로 사용하여 -128 ~ 127을 저장하지만, unsigned 키워드를 사용하면
부호 비트까지 활용하여 0 ~ 255까지 더 많은 양수를 저장할 수 있다.

wchar_t는 와이드 문자(wide character)를 저장하는 자료형이다.
비쥬얼 스튜디오에서는 wchar_t를 2byte로 정의하고, GCC 컴파일러는 4byte로 정의한다.
하지만 GCC에서도 컴파일할 때 -fshort-wchar 옵션을 적용하면 wchar_t를 2byte로 사용할 수 있다.

<char vs wchar_t>
    1) char:
        인코딩 방식:
            멀티바이트(MBCS)
        단일 문자 크기: 
            1byte 혹은 2byte(영문, 숫자 등의 아스키 코드는 1byte, 한글, 한자 등은 2byte로 표현)
        문자열: 
            유니코드를 제외한 문자열(ANSI, UTF-8)

    2) wchar_t:
        인코딩 방식:
            유니코드(UNICODE)
        단일 문자 크기:
            2byte(GCC에서는 기본 4byte)
        문자열:
            와이드 문자, UTF-16으로 인코딩된 문자열


UTF-16으로 인코딩된 문자열을 출력해 보면 유니코드가 어떻게 사용되는지 알 수 있다.
wchar_t 문자열을 입력할 때는 wcout을 이용해야 한다.
더물어 wchar_t에 유니코드 문자열을 넣으려면 L"문자열"처럼 지정해야 하는 것도 알아두어야 한다.
*/

/*
정수 형식

일반적으로 가장 많이 사용하는 데이터 형식을 꼽으라면 단연코 정수형이 그 주인공이다.
프로그래밍에서 정수형 데이터는 수학에서 정의하는 정수의 개념과 동일하다.
정수란, 양의 정수와 음의 정수, 그리고 0으로 이루어진 수의 체계이다.

그런데 정수형은 다른 데이터 형식과 달리 조금 특이하게 설정되어 있다.
정수형의 기준이 되는 int는 시스템의 자연스러운 크기를 따르도록 규정하고 있다.
자연스러운 크기란, 시스템에서 한 번에 처리할 수 있는 크기를 의미한다.
따라서 int는 컴퓨터 시스템에 따라 크기가 다르다.

예컨대 16bit 시스템에서 int는 16bit이고, 32bit 시스템에서는 32bit이다.
그런데 현재 컴퓨터 시장에서 거의 기본으로 출시되는 64bit 시스템에서 int는 64bit일 것 같지만, 실제론 32bit(=4byte)다.

* sizeof 연산자를 사용하면 현재 시스템에서 데이터 형식의 크기를 알 수 있다.

실행하는 시스템에 따라 크기는 다르게 나올 수 있다.
앞서 언급한 대로 C++ 언어 표준안은 정수형의 크기를 정확하게 명시하지 않지만, 최소한으로 정의된 것을 요약하면 다음과 같다.

1 byte == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)

정수형에서 signed, unsigned는 문자형에서 설명한 것과 같다.
부호가 있는(signed) 정수는 음수와 양수를 모두 저장할 수 있다.
signed 키워드를 이용해 부호 있는 정수를 명시적으로 선언할 수 있다.
반대로 부호가 없는 (unsigned) 정수는 양수만 가질 수 있다.
unsigned 키워드를 이용해 부호 없는 정수를 명시적으로 선언할 수 있다.

signed, unsigned 키워드에 따른 정수 표현 범위를 비교하면 다음과 같다.

<signed vs unsigned integer types>

    1 byte signed = -128 ~ 127
    1 byte unsigned = 0 ~ 255
    2 byte signed = 32,768 ~ 32,767
    2byte unsigned = 0 ~ 65,535
    4byte signed = -2,147,483,648 ~ 2,147,483,647
    4byte unsigned = 0 ~ 4,294,967,295
    8byte signed = -9,223,372,036,854,808 ~ 9,223,372,036,854,807
    8byte unsigned = 0 ~ 18,446,744,073,709,551,615
*/

/*
부동 소수점 형식

부동 소수점(floating point)이라는 말을 처음 듣는다면 조금 생소할 수 있다.
부동이란, "떠다니며 움직인다"는 의미다. 즉, 소수점이 고정되지 않고 움직인다는 뜻이다.
소수점이 움직인다는 것은 정수부와 소수부의 자릿수가 일정하지 않다는 의미다.
그렇지만 유효 숫자의 자릿수는 정해져 있다.
즉, 자료형의 크기가 정해져 있으므로 부동 소수점의 특정 자리까지만 저장할 수 있고 나머지는 유실된다.

부동 소수점의 정밀도(floating point precision)는 데이터 유실 없이 얼마나 많은 유효 자릿수를 나타낼 수 있는가를 의미한다.

* IEEE 754 부동 소수점 표준
    C++ 언어의 부동 소수점은 IEEE 754에서 정의한 형식으로 정의되어 있다.
    IEEE 754는 전기전자기술자협회(IEEE)에서 개발한 표준으로, 컴퓨터에서 부동 소수점을 표현하는 데 가장 널리 쓰인다.
    IEEE 754의 부동 소수점 표현은 크게 세 부분으로 구성된다.
    최상위 비트는 부호를 표시하는 데 사용하며, 지수(exponent)와 가수(fraction / mantissa) 부분으로 나뉜다.

    부동 소수점 방식은 컴퓨터에서 고정 소수점 방식보다 넓은 범위의 수를 나타낼 수 있어 계산에 많이 사용되지만,
    근삿값으로 표현되고 고정 소수점 방식보다 연산 속도가 느려 별도의 전용 연산 장치를 두는 경우가 많다.
    부동 소수점을 계산하는 데 최적화된 장치로 그래픽 카드가 있다.

C++ 언어에서 지원하는 부동 소수점 형식을 살펴보도록 한다.
부동 소수점을 표현할 때 숫자 뒤에 'f'를 붙이면 float 형, 'l'을 붙이면 long double 형, 아무것도 붙이지 않으면 double 형 값이 된다.

<부동 소수점의 크기에 따른 표현 범위아 유효 자릿수>
    1) 4 byte:
        표현 범위(+-1.18 x 10 ^ -38 ~ +-3.4 x 10^38)
        유효 자릿수(자리): 6 ~ 9, 일반적으로 7

    2) 8 byte:
        표현 범위(+-2.23 ~ 10 ^ -38 ~ +-1.80 x 10^308)
        유효 자릿수(자리): 15 ~ 18, 일반적으로 16

    3) 16 byte:
        표현 범위(+-3.36 x 10^-4932 ~ +- 1.18 x 10^4932)
        유효 자릿수(자리): 33 ~ 36


* 데이터 형식

1) 정수형(integer):
    정수를 표현하는 형식으로 int, short, long, long long 등이 있다.
    각 형식은 저장하는 비트 수에 따라 값의 범위가 다르다.

2) 부동 소수점(floating point):
    소수점이 있는 값을 표현하는 방식으로 float, double, long double 등이 있다.
    float보다 double 등이 높은 정밀도를 제공한다.

3) 문자(character):
    단일 문자를 표현하는 형식으로 char를 사용하며 작은 따옴표로 문자를 감싸 표현한다.

4) 불리언(boolean):
    참(true) 또는 거짓(false)을 표현하는 형식으로 bool을 사용하며, 조건문과 논리 연산에 주로 활용한다.

5) 보이드(void):
    함수가 어떤 값을 반환하지 않음을 나타내며, 주로 함수의 반환 타입으로 사용한다.

    void func_name() {...}
    int int_age = 25;
    bool is_passed = True;
    char ch_grade = 'A';
    float float_height = 175.3f;
    double double_height = 175.5;
    long double long_double_height = 175.5l;
*/