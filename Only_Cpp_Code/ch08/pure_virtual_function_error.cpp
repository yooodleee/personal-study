// 순수 가상 함수만 선언하고 자식 클래스에서 정의하지 않음

/**
 * 가상 함수 테이블
 * 
 * 앞서 가상 함수로 구현한 몬스터 공격 코드에서 클래스 포인터 mom에 대입한 객체는 모두 가상 함수를 
 * 가지고 있으며, attack_special은 대입한 객체의 코드로 호출되었다. 이런 동작이 가능한 이유는 
 * 가상 함수를 포함하는 클래스는 가상 함수 테이블(virtual function table)을 이용하기 때문이다. 
 * 
 * 가상 함수가 있는 클래스로 객체를 생성하면 메모리에 _vfptr이라는 가상 함수 테이블을 가리키는 포인터가
 * 자동으로 생기고, 객체가 가상 함수를 호출할 때 _vfptr을 사용한다. 
 * 
 * 가상 함수 테이블은 클래스의 계층 구조에서 최상위 클래스에만 존재한다. 자식 클래스는 부모 클래스의 
 * 가상 함수 테이블을 상속받으며, 가상 함수를 오버라이딩할 때 해당 함수의 주소를 가상 함수 테이블에 등록
 * 한다. 
 * 
 * monster 클래스의 포인터로 선언한 mon에 monster_a 클래스의 객체를 대입(업캐스팅)했을 때와 monster
 * 클래스의 객체를 대입했을 때 가상 함수 테이블의 상태를 다음과 같이 표현해 보겠다. 
 * 
 *          ----------------------
 *          |       monster      |
 *          |   ---------------  |
 *          |   |  _vfptr[0]  |  |          -------------------------------
 *          |   ---------------  |          |   monster::attack_special() |
 *          |                    |          -------------------------------
 *          ----------------------          |   monster_a::attack_special()|
 *          |      monster_a     |          --------------------------------
 *          |   ---------------  |
 *          |   | _vfptr[0]   |  |
 *          |   ---------------  |
 *          ----------------------
 * 
 * monster 클래스에서 가상 함수 attack_special을 구현했으므로 컴파일러는 가상 함수 테이블을 만들어 해당 함수의
 * 주소를 등록하고, 이를 가리키는 _vfptr 포인터를 monster 클래스에 생성한다. 그리고 monster 클래스를 상속받은
 * monster_a는 monster의 _vfptr 포인터까지 상속받는다. monster_a 클래스에서 가상 함수 attack_special를 오버라이딩
 * 했으므로 함수의 주소를 가상 함수 테이블에 등록한다. 따라서 같은 함수를 호출하더라도 mon이 가리키는 객체에 따라
 * 호출되는 구현체는 다르다. 
 * 
 * 가상 함수 테이블은 배열이므로 가상 함수를 여러 개 구현하면 인덱스에 따라 이동한다. 현재는 가상 함수가 한 개이므로
 * [0]으로 접근하지만, 만약 monster와 monster_a 클래스에 attack_at_dawn이라는 가상 함수를 추가로 구현한다면 다음처럼
 * 표현할 수 있다. 
 * 
 *                              ---------------------
 *                              |      monster      |
 *                              |   --------------  |
 *                              |   | _vfptr[0]  |  |
 *                              |   --------------  |           --------------------------------
 *                              |   | _vfptr[1]  |  |           |   monster::attack_special()  |
 *                              |   --------------  |           --------------------------------
 *                              ---------------------           |   monster::attack_at_dawn()  |
 *                              |      monster_a    |           --------------------------------
 *                              |   --------------  |           |   monster_a::attack_special()|
 *                              |   | _vfptr[0]  |  |           --------------------------------
 *                              |   --------------  |           |  monster_a::attack_at_dawn() |
 *                              |   | _vfptr[1]  |  |           --------------------------------
 *                              |   --------------  |
 *                              ---------------------
 * 
 * monster 클래스의 포인터인 mon에 객체를 대입하면 해당 객체로 이동한 후 _vfptr이 가리키는 함수를 호출한다. 내부적으로는
 * 더 복잡하게 동작하지만 여기서는 가상 함수가 호출될 때 가상 함수 테이블이 사용된다는 사실만 기억하고 넘어가도 좋을 것
 * 같다. 
 */

#include <iostream>
#include <list>

using namespace std;



class character {
public:
    character() : hp(100), power(100) {};
    
    void get_damage(int _damage) {};


protected:
    int hp;
    int power;
};


class player : public character {
public:
    player() {};
};


class monster {
public:
    monster() {};
    void attack(player target_player) {};
    virtual void attack_special(player target_player);
    virtual void attack_at_down() = 0;  // 순수 가상 함수로 선언언
};

void monster::attack_special(player target_player) {
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}



class monster_a : public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_a::attack_special(player target_player) {
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


class monster_b : public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_b::attack_special(player target_player) {
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}


class monster_c : public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_c::attack_special(player target_player) {
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}


int main() {
    list<monster*> mon_list;

    monster_a first_monster;
    mon_list.push_back(&first_monster);

    monster_b second_monster;
    mon_list.push_back(&second_monster);

    monster_c third_monster;
    mon_list.push_back(&third_monster);

    for (auto item : mon_list) {
        item->attack_at_down();
    }

    return 0;
}