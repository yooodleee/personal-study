// private으로 선언된 멤버에 접근하기

/**
 * 만약, bank 클래스에서 private으로 선언된 멤버(예에서는 safe)를 main 함수에서
 * 바로 접근하게 되면 어떻게 될까?
 */

#include <iostream>

using namespace std;


class bank
{
private:
    int safe;   // 금고

public:
    bank();     // 기본 생성자
    void use_counter(int _in, int _out);    // 입출금 창구 함수

};

bank::bank()
{
    safe = 1000;    // 은행 금고 초기 금액 설정
    cout << "최초 금고: " << safe << endl;
    cout << endl;

}

void bank::use_counter(int _in, int _out)
{
    safe += _in;    // 입금
    safe -= _out;   // 출금

    cout << "입금: " << _in << endl;
    cout << "출금: " << _out << endl;
    cout << "금고: " << safe << endl;
    cout << endl;

}

int main()
{
    bank my_bank;
    my_bank.safe -= 100;    // private으로 지정된 금고에 직접 접근하여 인출 시도 
    return 0;
}

/**
 * 위 코드는 문법적 오류가 발생한다. 요류 메시지를 보면 bank 클래스의 safe 멤버 변수가 private
 * 접근 지정자로 선언되었다고 알려준다.
 */