// 생성자 정의하기

#include <iostream>

using namespace std;


class character {
public:
    character() {
        cout << "character 클래스 생성자" << endl;
    };
};


int main() {
    character player;   // main에서 character 클래스로 player라는 객체를 생성할 때 character() 생성자가 자동으로 호출됨
    return 0;
}