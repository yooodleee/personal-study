// 다중 상속

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


// 다중 상속
class monster_a : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player);
    
};