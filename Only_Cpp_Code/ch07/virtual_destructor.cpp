// 리스코프 치환 원칙을 적용한 가상 소멸자

/**
 * 가상 소멸자는 아직 가상 함수를 배우지 않았으므로 이해가 어려울 수 있다. 여기서는 부모 
 * 클래스의 포인터로 생성된 자식 객체가 소멸할 때 자식 클래스의 소멸자가 호출되므로 보장
 * 한다는 것만 기억하면 된다. 이것이 다형성을 활용한 객체 소멸의 올바른 방법이다. 
 */

/**
 * 소멸자
 * 
 * 1) 소멸자: 
 *    클래스 이름과 동일하지만 앞에 ~ 연산자를 추가한 함수를 정의한다. 객체가 소멸되는 시점에 호출된다. 
 * 2) 자식 클래스 소멸자: 
 *    부모 클래스와 자식 클래스 모두 소멸자 정의 방법은 같다. 자식 클래스의 소멸자가 먼저 호출된 후에 
 *    부모 클래스의 소멸자가 호출된다. 
 * 3) 가상 함수로 선언된 소멸자: 
 *    자식 클래스가 부모 클래스를 대신할 경우 자식 클래스 소멸자가 호출되지 않으므로 가상 함수로 자식 
 *    클래스의 소멸자가 호출될 수 있도록 한다. 
 * 4) 가상 함수로 선언된 자식 클래스 소멸자: 
 *    가상 함수로 정의된 자식 클래스 소멸자
 * 
 * class monster
 * {
 * public: 
 *      monster() {...};
 *      // 소멸자
 *      ~monster() {...};
 * };
 * 
 * class monster_a : public monster 
 * {
 * public: 
 *      monster_a() {...};
 *      // 자식 클래스 소멸자
 *      ~monster_a() {...};
 * };
 * 
 * class monster 
 * {
 * public: 
 *      monster() {...};
 *      // 가상 함수로 선언된 소멸자
 *      virtual ~monster() {...};
 * };
 * 
 * class mosnter_a : public monster 
 * {
 * public: 
 *      monster_a() {...};
 *      // 가상 함수로 선언된 자식 클래스 소멸자
 *      virtual ~monster_a() {...};
 * };
 */

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