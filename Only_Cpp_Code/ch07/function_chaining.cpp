// 멤버 함수 체이닝 적용

/**
 * 멤버 함수 체이닝을 구현할 때
 * 
 * 함수 체이닝(chanining)이란 여러 함수를 연이어 호출하는 방식을 말한다. 이는 멤버 함수가 객체를
 * 반환하고 해당 객체에서 다시 멤버 함수를 호출하는 방식으로 이뤄진다. 이러한 스타일은 코드를 
 * 간결하게 만들고 호출 순서를 직관적으로 표현할 수 있다. 
 * 
 * 멤버 함수 체이닝을 구현할 때에 반환 형식을 레퍼런스(예에서는 bank &)로 지정하고 return 문에 
 * this 포인터를 활용할 수 있다. 만약 반환 형식을 레퍼런스가 아닌 포인터(bank *)로 지정하면 
 * 체이닝 호출문은 func1().func2().func3()이 아닌 func1()->func2()->func3()처럼 작성해야 한다. 
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

    bank &deposit_interest(int interest);   // 이자 입금
    bank &withdraw_utility(int utility);    // 공과금 출금
    bank &withdraw_tax(int tax);            // 세금 출금

    string get_bank_name()
    {
        return bank_name;
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
    this->safe = 0;
    cout << bank_name << " 계좌가 초기화 되었습니다." << endl;
}

void bank::reset_account()
{
    this->safe = 0;
    cout << bank_name << " 계좌가 초기화 되었습니다." << endl;
}

bank &bank::deposit_interest(int interest)
{
    safe += interest;
    cout << bank_name << " 이자 지급: " << interest << endl;
}

bank &bank::withdraw_utility(int utility)
{
    safe -= utility;
    cout << bank_name << " 공과금 납부: " << utility << endl;
    return *this;
}

bank &bank::withdraw_tax(int tax)
{
    safe -= tax;
    cout << bank_name << " 세금 납부: " << tax << endl;
    return *this;
}

int main()
{
    bank rich_bank("부유한 은행"), global_bank("세계적 은행");
    rich_bank.use_counter(50, 10);
    cout << endl;

    global_bank.transfer_account(rich_bank.get_safe());
    rich_bank.reset_account();
    cout << endl;

    // 함수 체이닝 호출(함수가 차례로 호출됨)
    global_bank.deposit_interest(10).withdraw_utility(1).withdraw_tax(2);
    cout << endl;
    cout << global_bank.get_bank_name() << "잔액: " << global_bank.get_safe() << endl;

    return 0;
}

/**
 * 실행 결과
 * 
 * 부유한 은행 처리 - 입금: 50, 출금: 10
 * 
 * 세계적 은행으로 계좌 이동: 40
 * 부유한 은행 계좌가 초기화 되었습니다. 
 * 
 * 세계적 은행 이자 지급: 10
 * 세계적 은행 공과금 납부: 1
 * 세계적 은행 세금 납부: 2
 * 
 * 세계적 은행잔액: 47
 */