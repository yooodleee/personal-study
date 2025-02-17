// 부모와 자식 클래스 레퍼런스로 참조했을 때 호출 변화

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

    monster &mon = forest_monster;      // 부모 클래스의 레퍼런스에 대입
    monster_a &mon_a = forest_monster;  // 자식 클래스의 레퍼런스에 대입

    cout << endl << "부모 클래스 레퍼런스로 공격" << endl;
    mon.attack_special(player_1);

    cout << endl << "자식 클래스 레퍼런스로 공격" << endl;
    mon_a.attack_special(player_1);

    return 0;
}