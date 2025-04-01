// 자신을 가리키는 this 포인터

/**
 * this는 객체 내부에서 객체 자신을 가리키는 키워드이다. 객체 자신을 가리키는 키워드가
 * 왜 필요한지 금방 이해가 되지 않을 수도 있다. 
 * 
 * 객체가 메모리에 할당되는 구조
 * 
 * this 포인터를 이해하려면 먼저 객체의 메모리가 어떻게 할당되는지 알아야 한다. 객체도 
 * 하나의 변수이므로 객체가 생성되면 클래스 크기만큼의 메모리가 할당된다. 할당받는 
 * 메모리양은 클래스를 표현하기 위한 메모리, 멤버 변수를 저장하기 위한 메모리 등이 있다. 
 * 
 * 그런데 멤버 함수는 해당 클래스의 모든 객체가 같은 코드를 공통으로 사용하므로 멤버 함수를
 * 저장할 메모리를 객체마다 할당한다면 낭비일 것이다. 따라서 멤버 함수는 메모리에 한 번만
 * 적재하고 같은 클래스의 객체를 추가하더라도 똑같은 함수를 참조한다. 
 * 
 * 메모리 할당은 정적인지 동적인지에 따라 스택이나 힙 등 메모리 위치가 달라지지만 여기서는 
 * 이해하기 쉽게 정적 메모리 할당을 기준으로 설명하겠다. 
 * 
 * 은행 클래스를 구현한 코드와 이를 실행했을 때 메모리 상태를 그려 보겠다. 
 */

#include <iostream>
using namespace std;


class bank
{
private:
    int safe;       // 금고
    string bank_name;

public:
    bank(string name) : bank_name(name) { safe = 0; };  // 기본 생성자
    ~bank() {};
    void use_counter(int _in, int _out);                // 입출금 창구 함수
};

void bank::use_counter(int _in, int _out)
{
    safe += _in;
    safe -= _out;
    cout << bank_name << " 처리 - 입금: " << _in << ", 출금: " << _out << endl;
}

int main()
{
    bank rich_bank("부유한 은행"), global_bank("세계적 은행");
    rich_bank.use_counter(10, 10);
    global_bank.use_counter(20, 5);
    return 0;
}


/**
 * 실행 결과
 * 
 * 부유한 은행 처리 - 입금: 10, 출금: 10
 * 세계적 은행 처리 - 입금: 20, 출금: 5
 */

/**
 * bank 클래스로 생성한 rich_bank와 global_bank 객체는 각각 멤버 변수인 safe를 포함한 채로
 * 스택에 할당된다. 하지만 멤버 함수인 use_counter는 객체와는 별개로 한 번만 할당된다. 그리고
 * 함수가 호출되면 공통의 메모리 공간에 접근한다. 
 * 
 * 
 *      (stack memory)
 * --------------------------
 * |      rich_bank         |
 * --------------------------
 * |    rich_bank.size      |
 * --------------------------
 *                                  =>        bank::use_counter
 * --------------------------
 * |      global_bank       |
 * --------------------------
 * |    global_bank.safe    |
 * --------------------------
 */