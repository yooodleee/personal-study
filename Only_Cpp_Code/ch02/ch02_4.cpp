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

