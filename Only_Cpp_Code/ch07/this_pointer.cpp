// this 포인터

/**
 * simple_bank.cpp 에서 use_counter 함수는 _in과 _out 매개변수로 전달받은 값을 
 * 멤버 변수인 safe에서 가감한다. 그런데 무언가 이상하다. 멤버 변수와 멤버 함수는
 * 스택에서 위치가 다르므로 주소를 모르면 멤버 함수에서 멤버 변수의 값을 변경할 수
 * 없을 텐데 프로그램이 정상으로 동작한다. 
 * 
 * 결론부터 말하면 멤버 함수에서 멤버 변수에 접근할 방법이 필요한데, this 포인터가
 * 이 역할을 말한다. 앞선 코드에서 this 포인터를 사용하지 않았는데도, 프로그램이 
 * 정상으로 동작한 이유는 컴파일 과정에서 자동으로 처리되기 때문이다. 즉, this 포인터는
 * 멤버 함수 내에서 자동으로 생성되어 해당 함수가 속한 객체의 주소를 가리킨다. 
 * 
 * 앞에서 작성한 소스 코드를 컴파일하면 내부적으로 다음과 같은 코드로 변경되어 처리된다. 
 * 컴파일된 은행 클래스
 * ...(생략)... 
 * void bank::use_counter(bank *const this, int _in, int _out)
 * {
 *      this->safe += _in;
 *      this->safe -= _out;
 * }
 * 
 * int main()
 * {
 *      bank rich_bank, global_bank;
 *      rich_bank.use_couter(&rich_bank, 10, 10);
 *      global_bank.use_counter(&global_bank, 20, 5);
 * 
 *      return 0;
 * }
 * 
 * 멤버 함수를 호출하는 코드에서는 객체의 주소를 첫 번째 인자로 전달하고, 이에 맞춰 멤버
 * 함수에서는 this 포인터로 주소를 전달받아서 멤버 변수에 접근할 때 사용한다. 이렇게 하면
 * 멤버 함수가 스택에서 다른 위치에 할당되더라도 해당 객체의 멤버 변수에 접근할 수 있다. 
 * 
 * 이것은 C++ 언어에서 메모리를 효율적으로 사용하기 위한 방법으로, 개발자가 직접 작성하는
 * 코드는 아니다. 그러나 개발자가 작성하는 코드에서는 객체 자신을 가리키는 this 포인터를
 * 활용할 수도 있다. 
 * 
 * 지역 변수와 구별할 때
 * 앞서 본 은행 코드에서 다음처럼 다른 은행의 계좌를 옮기는 transfer_account 라는 함수를 
 * 추가하려고 한다. 
 * void transfer_account(int safe);
 * 
 * 그런데 다른 은행의 계좌를 나타내는 매개변수 이름이 safe로 멤버 변수 이름과 같아서 헷갈린다. 
 * 이럴 때는 멤버 변수를 this 포인터로 표현할 수 있다. 다음 코드에서 this->safe와 safe는 각각
 * 멤버 변수와 매개변수를 가리킨다. 
 */


#include <iostream>
#include <string>
using namespace std;


class bank
{
private:
    int safe;       // 금고
    string bank_name;

public:
    bank(string name) : bank_name(name)
    {
        safe = 0;   // 기본 생성자
    };
    ~bank() {};

    void use_counter(int _in, int _out);    // 입출금 창구 함수
    void transfer_account(int safe);        // 계좌 변경 함수
    void reset_account();                   // 계좌 초기화
    int get_safe()
    {
        return safe;                        // 금고 금액 반환
    };                                      
};

void bank::use_counter(int _in, int _out)
{
    safe += _in;
    safe -= _out;
    cout << bank_name << " 처리 - 입금: " << _in << ", 출금: " << _out << endl;
}

void bank::transfer_account(int safe)
{
    this->safe = safe;
    cout << bank_name << "으로 계좌 이동: " << safe << endl;
}

void bank::reset_account()
{
    this->safe = 0;
    cout << bank_name << "계좌가 초기화 되었습니다." << endl;
}

int main()
{
    bank rich_bank("부유한 은행"), global_bank("세계적 은행");
    rich_bank.use_counter(50, 10);

    global_bank.transfer_account(rich_bank.get_safe());
    rich_bank.reset_account();

    return 0;
}

/**
 * 실행 결과
 * 
 * 부유한 은행 처리 - 입금: 50, 출금: 10
 * 세계적 은행으로 계좌 이동: 40
 * 부유한 은행 계좌가 초기화 되었습니다. 
 */

/**
 * 멤버 변수나 매개변수 이름을 지을 때 될 수 있으면 겹치지 않도록 정의하는 것이 
 * 코드를 읽고 해석하기가 쉽다. 그러나 여러 개발자가 협업하거나 라이브러리의
 * 클래스들을 사용하다보면 이런 충돌을 만날 수 있다. 그때는 this 포인터를 활용할
 * 수 있다. 
 */