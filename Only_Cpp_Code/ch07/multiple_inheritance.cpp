// 다중 상속

/**
 * 클래스를 만들다 보면 한 번에 여러 가지 속성과 기능을 상속받아야 할 때도 있다. 앞에서 
 * 예로 든 게임 속 캐릭터들은 체력과 힘을 속성으로 가지는데, 이는 몬스터와 플레이어 모두에
 * 공통된 속성이다. 하지만 몬스터에는 공격이라는 기능이 있다. 플레이어와 몬스터는 캐릭터라는
 * 특성은 공유하지만, 공격이라는 특성은 몬스터만이 가지고 있다. 
 * 
 * 이처럼 다른 종류의 클래스를 둘 이상 상속받는 것을 다중 상속(multiple inheritance)이라고 한다. 
 * 몬스터 소스 코드에서 다중 상속 부분을 살펴보면 쉽게 이해할 수 있다. 게임 플레이어는 캐릭터 
 * 클래스만 상속받지만, 몬스터 A, B, C는 캐릭터 클래스와 몬스터 클래스를 모두 상속받는다. 
 */

#include <iostream>

using namespace std;


class character {
public:
    character() : hp(100), power(100) {};


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
    void get_damage(int _damage) {};
    void attack(player target_player) {};
    void attack_special(player target_player) {};

};


// 다중 상속(monster_a는 monster, character를 상속받음)
class monster_a : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
    
};

/**
 * 다중 상속을 지정할 때 클래스 이름 앞에 접근 지정자를 생략하면 private으로 상속받는다. 
 * 따라서 코드에서 monster_a는 monster 클래스를 public으로 상속받지만, character 클래스는
 * private으로 상속받는다. 
 * 
 * 다중 상속을 클래스 다이어그램으로 표현하면 다음과 같다. 
 * 
 *              (character) -> monster_a
 *                 ------------------
 *                 | - hp: int      |
 *                 | - power: int   |
 *                 ------------------
 * 
 *                      (monster)
 *          ---------------------------------
 *          | + get_damage(int) : void      |
 *          | + attack(player) : void       |
 *          | + attack_special(player): void|
 *          ---------------------------------
 */