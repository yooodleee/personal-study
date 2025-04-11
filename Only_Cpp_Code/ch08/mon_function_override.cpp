// 일반 함수를 활용한 오버라이딩 호출 변화

/**
 * 가상 함수를 사용하지 않고 오버라이딩했을 때의 동작도 살펴보도록 하자. 이전 코드와는 다르게 
 * 업캐스팅 후에 부모의 멤버 함수가 호출되는 것을 확인할 수 있다. 
 */

#include <iostream>

using namespace std;



class character 
{
public:
    character() : hp(100), power(100) {};


protected:
    int hp;
    int power;
};


// character 클래스를 상속받은 player 클래스
class player : public character 
{
public:
    player() {};
};



// 기본 Monster클래스
class monster 
{
public:
    monster() {};
    void get_damage(int _damage) {};
    void attack(player target_player) {};
    void attack_special(player target_player) {};
};

void monster::attack_special(player target_player) 
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 몬스터 A는 기본 Monster 클래스로부터 상속
class monster_a : public monster, character 
{
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_a::attack_special(player target_player) 
{
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


// 몬스터 B는 기본 Monster 클래스로부터 상속
class monster_b : public monster, character 
{
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_b::attack_special(player target_player) 
{
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}


// 몬스터 C는 기본 Monster 클래스로부터 상속
class monster_c : public monster, character 
{
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
};

void monster_c::attack_special(player target_player) 
{
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}



int main() 
{
    player player_1;

    monster_a forest_monster;

    monster& mon = forest_monster;          // 업캐스팅 발생
    monster_a& mon_a = forest_monster;

    cout << endl << "부모 클래스로 업캐스팅 후 공격" << endl;
    mon.attack_special(player_1);           // monster_a의 오버라이딩 함수 호출

    cout << endl << "자식 클래스로 공격" << endl;
    mon_a.attack_special(player_1);

    return 0;
}

/**
 * 실행 결과
 * 
 * 부모 클래스로 업캐스팅 후 공격
 * 기본 공격 : 데미지 - 10 hp
 * 
 * 자식 클래스로 공격
 * 인텡글 공격 : 데미지 - 15 hp
 */

