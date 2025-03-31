// 생성자 직접 호출하기

/**
 * 생성자에서 다른 생성자를 어떻게 호출할까? C++ 11 부터는 초기화 목록에서 다른 생성자를 
 * 호출할 수 있게 변경되었다. 초기화 목록은 추후에 다루기로 하고 먼저 수정한 코드를 살펴보자. 
 * 다른 생성자를 호출하는 코드를 생성자의 초기화 목록으로 옮겼다. 이렇게 하면 의도한 대로 
 * 생성자가 호출된다. 
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


class monster_a : public monster, character {
public:
    monster_a() : monster_a(10, 10) {   // 초기화 목록으로 다른 생성자 호출
        cout << "monster_a 클래스 생성자" << endl;
    };

    monster_a(int x, int y) : location{x, y} {
        cout << "monster_a 클래스 생성자 (매개변수 추가)" << endl;
    };

    void show_location() {
        cout << "위치(" << location[0] << " , " << location[1] << ")" << endl;
    };

private:
    int location[2];
};


int main() {
    monster_a forest_monster;
    forest_monster.show_location();

    return 0;
}

/**
 * 실행 결과
 * 
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자 (매개변수 추가)
 * monster_a 클래스 생성자
 * 위치 (10, 10)
 */

