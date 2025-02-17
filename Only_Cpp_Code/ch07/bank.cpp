// bank 클래스 정의하기

#include <iostream>

using namespace std;


class bank {
private:
    int safe;   // 금고


public:
    bank();     // 기본 생성자
    void use_counter(int _in, int _out);    // 입출금 창구 함수

};

bank::bank() {
    safe = 1000;    // 은행 금고 초기 금액 설정
    cout << "최초 금고 : " << safe << endl;
    cout << endl;
}

void bank::use_counter(int _in, int _out) {
    safe += _in;    // 입금
    safe -= _out;   // 출금

    cout << "입금 : " << _in << endl;
    cout << "출금 : " << _out << endl;
    cout << "금고 : " << safe << endl;
    cout << endl;
}

int main() {
    bank my_bank;   // my_bank 인스턴스 생성(클래스가 메모리에 할당되어 생성된 변수=객체object)
    // bank 클래스의 멤버 함수인 use_counter를 호출할 수 있음.

    my_bank.use_counter(0, 20); // 출금 20
    my_bank.use_counter(50, 0); // 입금 50
    my_bank.use_counter(100, 50);   // 입금 100, 출금 50

    return 0;
}

/*
용어 정리

* 객체(object): 논리적 개념으로 클래스로 구현하고자 하는 구현 대상, 또는 인스턴스를 달리 부를 때 사용
* 클래스(class): 객체를 구현하기 위한 설계도
* 인스턴스(instance): 클래스 정의에 따라 메모리에 실체화된 객체의 형태태
*/