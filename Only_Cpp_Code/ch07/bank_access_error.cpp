// private으로 선언된 멤버에 접근하기

#include <iostream>

using namespace std;


class bank {
private:
    int safe;   // 금고
    // ... 생략 ...

};

int main() {
    bank my_bank;
    my_bank.safe -= 100;    // private으로 지정된 금고에 직접 접근하여 인출을 시도

    return 0;
}