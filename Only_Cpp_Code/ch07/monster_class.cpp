// 몬스터 클래스 정의하기

/**
 * 추상화와 캡슐화를 이용한 클래스 설계
 * 
 * 추상화와 캡슐화를 이용해 게임 속 몬스터를 클래스로 만들어 보면서 개념을 
 * 다시 한 번 정리해보자. 게임 속 몬스터가 다음과 같은 규칙으로 움직인다고 
 * 가정해보자. 
 * 
 * 1) 몬스터는 체력과 공격력이 있다. 
 * 2) 몬스터는 데미지를 입으면 체력을 소모한다. 
 * 3) 몬스터는 공격할 수 있다. 
 * 4) 몬스터는 특수 공격을 할 수 있다. 
 * 5) 몬스터의 종류에 따라 공격력과 특수 공격은 다양하다. 
 * 
 * 
 * (몬스터 추상화)
 * - 체력 | 공격력
 * - 공격을 받는다. 
 * - 공격한다. 
 * - 특수 공격을 한다. 
 * 
 * 은닉화까지 고려하여 캡슐화한 몬스터를 클래스 다이어그램으로 표현하면 다음과 같다. 
 * 
 *                      (monster)
 *          ----------------------------------
 *          | - hp: int                      |
 *          | - power: int                   |
 *          ----------------------------------
 *          | + get_damage(int) : void       |
 *          | + attack(Player) : void        |
 *          | + attack_special(Player) : void|
 *          ----------------------------------
 * 
 * 잎사 소개한 몬스터의 특징은 1 ~ 4번 항목까지 만족하는 기본 몬스터 클래스를 설계했다. 
 * 마지막 5번 항목인 '몬스터의 종류에 따라 다른 요소' 부분은 어떻게 설계해야 할까?
 * 상속성과 다형성을 이용해 다음처럼 클래스 다이어그램으로 표현할 수 있다. 해당 부분은
 * 다음에 다루기로 하고 여기서는 몬스터 클래스가 범용으로 정의되었지만 미리 살펴보자. 
 * 
 *                      (monster)
 *          ----------------------------------
 *          | - hp: int                      |
 *          | - power: int                   |
 *          ----------------------------------
 *          | + get_damage(int) : void       |
 *          | + attack(Player) : void        |
 *          | + attack_special(Player) : void|
 *          ----------------------------------
 * 
 *                    (monster_a)
 *          ---------------------------------
 *          | + attack_special(player): void|
 *          ---------------------------------
 * 
 *                    (monster_b)
 *          ---------------------------------
 *          | + attack_special(player): int |
 *          ---------------------------------
 * 
 *                   (monster_c)
 *          ---------------------------------
 *          | + attack_special(player): void|
 *          ---------------------------------
 * 
 * 이렇게 설계한 클래스 다이어그램을 바탕으로 몬스터 클래스를 코드로 구현해 보겠다. 
 * 아직 배우지 않은 문법들도 있지만 여기서는 맛보기로 훑어보자. 기본으로 활용하는 
 * 코드라서 앞으로도 자주 사용할 예정이다. 흐름을 파악해보길 바란다. 
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

    cout << "몬스터 총 공격" << endl;
    forest_monster.attack_special(player_1);
    tutorial_monster.attack_special(player_1);
    boss_monster.attack_special(player_1);

    return 0;
}

/**
 * 실행 결과
 * 
 * 몬스터 총 공격
 * 인텡글 공격: 데미지 -15 hp
 * 가상 공격: 데미지 - 0 hp
 * 강력 뇌전 공격: 데미지 - 100 hp
 */