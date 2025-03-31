// 상속받은 클래스의 생성자

/**
 * 상속 클래스의 생성자 호출 순서
 * 
 * 상속성과 다형성을 배울 때 살펴본 몬스터 코드에서 monster_a 클래스는 monster와 character
 * 클래스를 다중 상속받는다. 이때 각 클래스의 생성자는 monster_a(), monster_b(), character()
 * 이다. 
 * 
 * 그럼 monster_a 클래스의 객체가 생성될 때 어떤 생성자가 호출될까? 정답은 세 클래스의 생성자
 * 모두 호출된다. 호출 순서는 상속받은 순서대로 부모의 생성자가 먼저 호출되고 나서 자식의 생성자가
 * 호출된다. 
 */

#include <iostream>

using namespace std;


class character {
public:
    character() {
        cout << "character 클래스 생성자" << endl;
    };
};


class monster {
public:
    monster() {
        cout << "monster 클래스 생성자" << endl;
    };
};


class monster_a : public monster, character {
public:
    monster_a() {
        cout << "monster_a 클래스 생성자" << endl;
    };
};


int main() {
    monster_a forest_monster;
    return 0;
}

/**
 * 실행 결과
 * 
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자
 */