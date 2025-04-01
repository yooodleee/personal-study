// + 연산자 오버로딩(몬스터 C와 플레이어 합체)

/**
 * 다음 코드에서는 연산자 오버로딩으로 몬스터 C가 플레이어를 흡수해 체력을 보충하는 
 * 기능을 추가하겠다. 
 */

#include <iostream>
#include <string>
using namespace std;


class character
{
public:
    character() : hp(100), power(100), location{ 0, 0 }, level(1) {};

    void move(int x, int y) {};
    void move(int x[], int y[], int spot_count) {};
    void get_damage(int _damage) {};

    int get_hp()
    {
        return hp;
    };
    int get_level()
    {
        return level;
    };

protected:
    int hp;
    int power;
    int location[2];
    int level;
};


class player : public character
{
public:
    player() {};
};


// 기본 Monster 클래스
class monster
{
public:
    void attack(player target_player) {};
    virtual void attack_special(player target_player);
};

void monster::attack_special(player target_player)
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 몬스터 C는 Monster 클래스로부터 상속
class monster_c : public monster, public character
{
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player) override;

    monster_c operator+(monster_c &operand);
    monster_c operator+(player &operand);

    void set_level(int level_value) 
    {
        level = level_value;
    };
    void set_hp(int hp_value)
    {
        hp = hp_value;
    };
};


monster_c monster_c::operator+(monster_c &operand)
{
    monster_c result_monster;
    result_monster.set_level(level + operand.get_level());
    return result_monster;
}

monster_c monster_c::operator+(player &operand)
{
    monster_c result_monster;
    result_monster.set_hp(hp + operand.get_hp());
    return result_monster;
}

void monster_c::attack_special(player target_player)
{
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}


int main()
{
    monster_c monster_c_obj1, monster_c_obj2;
    monster_c_obj2.set_level(2);
    player player1;
    monster_c new_monster_c_obj = monster_c_obj1 + monster_c_obj2;

    cout << "Player 합체 전 몬스터 C HP[" << new_monster_c_obj.get_hp()
        << "]" << endl;
    
    new_monster_c_obj = new_monster_c_obj + player1;

    cout << "Player 합체 후 몬스타 C HP[" << new_monster_c_obj.get_hp()
        << "]" << endl;

    return 0;
}

/**
 * 실행 결과
 * 
 * Player 합체 전 몬스터 C HP[100]
 * Player 합체 후 몬스터 C HP[200]
 */

/**
 * 실행 결과를 보면 몬스터가 플레이어를 흡수해서 플레이어의 체력만큼 증가된 것을 
 * 알 수 있다. 물론, 체력을 나타내는 멤버 변수 hp를 public으로 공유해 덧셈할 수도 
 * 있다. 그러나 체력이 0이 되었을 때 몬스터 삭제, 최고 체력에 도달할 때 더 이상 
 * 증가하지 않게 하는 등 전처리와 후처리를 위해서 hp를 protected로 은닉화하고 
 * 멤버 함수나 연산자 오버로딩을 활용하는 방법이 객체지향 프로그래밍에 더 가깝다. 
 */

/**
 * 함수 오버로딩과 연산자 오버로딩은 같은 것인가?
 * 
 * 오버로딩 개념과 동작 과정은 두 가지 모두 같다. 다만 연산자는 'operator+'와 같은
 * 이름으로 선언하고 사용할 때는 '+'만 쓰는 특수한 함수이다. + 연산자를 사용할 수도 
 * 있고 operator+로 직접 호출해서 사용할 수도 있다. 
 */