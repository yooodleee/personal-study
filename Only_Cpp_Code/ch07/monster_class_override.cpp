// 오버라이딩 함수 호출과 네임스페이스 활용

/**
 * 함수 재정의하기 => 오버라이딩(overriding)
 * 
 * 객체지향 프로그래밍에서 다형성을 구현하려면 함수의 오버라이딩을 이용해야 한다. 부모 클래스로부터 상속받은
 * 함수는 자식 클래스에서 부모 클래스에 정의된 내용을 그대로 사용한다. 하지만 다형성을 구현하려면 함수의 
 * 시그니처는 그대로 유지하면서 다르게 정의해야 한다. 
 * 
 * 시그니처는 그대로 유지하면서 부모 클래스에 정의된 함수를 자식 클래스에서 재정의하는 것을 오버라이딩이라고 한다. 
 * 
 * (부모)
 * monster::attack_special(A a)
 * 
 * (자식)
 * monster_a::attack_special(A a)
 * 
 * 몬스터 클래스를 다시 살펴보자. 몬스터 A, B, C는 attack_special(player)라는 함수를 각 클래스에서 재정의했다. 
 * 부모 클래스의 attack_special(player) 함수를 몬스터 A, B, C 클래스에서 오버라이딩한 것이다. 오버라이딩 함수는
 * 네임스페이스를 통해서 부모 클래스의 정의를 사용할 수 있다. 다음 코드를 실행하면 오버라이딩 함수는 자식 클래스에서
 * 재정의한 함수가 호출되며, 네임스페이스를 사용하면 해당 범위에 속한 함수가 호출된다. 
 */

#include <iostream>

using namespace std;


// 캐릭터 클래스
class character {
public:
    character() : hp(100), power(100) {};


protected:
    int hp;
    int power;

};


// 플레이어 클래스
class player : public character {
public:
    player();

};


// 기본 몬스터 클래스
class monster {
public:
    monster();
    void get_damage(int _damage);
    void attack(player target_player) {};
    void attack_special(player target_player) {};

};

void monster::attack_special(player target_player) {
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_a : public monster, character {
public:
    // 상속받은은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_a::attack_special(player target_special) {
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_b : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_b::attack_special(player target_special) {
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_c : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_c::attack_special(player target_special) {
    cout << "강력 뇌전 공격 : - 100 hp" << endl;
}


int main() {
    player player_1;

    monster_a forest_monster;
    monster_b tutorial_monster;
    monster_c boss_monster;

    cout << "오버라이딩 공격" << endl;
    forest_monster.attack_special(player_1);    // 오버라이딩 함수 호출
    tutorial_monster.attack_special(player_1);  // 오버라이딩 함수 호출
    boss_monster.attack_special(player_1);      // 오버라이딩 함수 호출

    cout << endl << "기본(monster 클래스) 공격" << endl;
    forest_monster.monster::attack_special(player_1);       // 네임스페이스에 속한 함수 호출
    tutorial_monster.monster::attack_special(player_1);     // 네임스페이스에 속한 함수 호출
    boss_monster.monster::attack_special(player_1);         // 네임스페이스에 속한 함수 호출

    return 0;
}

/**
 * 실행 결과 
 * 
 * 오버라이딩 공격
 * 인텡글 공격: 데미지 - 15 hp
 * 가상 공격: 데미지 - 0 hp
 * 강력 뇌전 공격: 데미지 - 100 hp
 * 
 * 기본(monster 클래스) 공격
 * 기본 공격: 데미지 - 10 hp
 * 기본 공격: 데미지 - 10 hp
 * 기본 공격: 데미지 - 10 hp
 */

/**
 * 그런데 만약 자식 클래스를 부모 클래스의 레퍼런스로 접근하면 어떤 함수가 호출될까? 
 * 결론은 부모 클래스에 정의된 함수가 호출된다. 
 */