// 리스코프 치환 원칙을 적용한 가상 소멸자

#include <iostream>

using namespace std;



class monster {
public:
    monster() {
        cout << "monster 클래스 생성자" << endl;
    };
    
    virtual ~monster() {    // 가상 소멸자 정의의
        cout << "monster 클래스 소멸자" << endl;
    };
};



class monster_a : public monster {
public:
    monster_a() {
        cout << "monster_a 클래스 생성자" << endl;
    };

    virtual ~monster_a() {  // 가상 소멸자 정의의
        cout << "monster_a 클래스 소멸자" << endl;
    };
};



int main() {
    monster *forest_monster = new monster_a();
    delete forest_monster;
    return 0;
}


/**
 * 소멸자
 * 
 * (1) 소멸자: 
 *      클래스 이름과 동일하지만 앞에 ~를 추가한 함수를 정의. 객체가 소멸되는 시점에 호출됨. 
 * 
 * (2) 자식 클래스 소멸자: 
 *      부모 클래스와 자식 클래스 모두 소멸자 정의 방법은 같다. 자식 클래스의 소멸자가
 *      먼저 호출된 후에 부모 클래스의 소멸자가 호출됨. 
 * 
 * (3) 가상 함수로 선언된 소멸자:
 *      자식 클래스가 부모 클래스를 대신할 경우 자식 클래스 소멸자가 호출되지 않으므로 
 *      가상 함수로 자식 클래스의 소멸자가 호출될 수 있도록 한다. 
 * 
 * (4) 가상 함수로 선언된 자식 클래스 소멸자: 
 *      가상 함수로 정의된 자식 클래스 소멸자자
 */