// 값을 전달받는 생성자

/**
 * 값을 전달받는 생성자
 * 
 * 객체를 생성할 때 특정 값을 전달할 수 있다. 예컨대 화면에서 몬스터 A가 나타날 위치를
 * 멤버 변수(location[2])로 만들고 객체를 생성할 때 해당 위치를 입력받는 생성자를 
 * 생각해 본다. 
 * 
 * 이때는 생성자에 매개변수를 추가하면 된다. 그러면 객체를 생성할 때 전달할 인자의 종류에
 * 따라 알맞은 생성자가 자동으로 호출된다. 만약 기본 생성자는 생략하고 매개변수가 있는 
 * 생성자만 작성했을 때는 객체를 생성할 때 반드시 인자를 전달해야 한다. 
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
    monster_a() {
        cout << "monster_a 클래스 생성자" << endl;
    };

    monster_a(int x, int y) : location{x, y} {  // 초기화 목록이라고 하며 매개변수로 전달받은 값으로 멤버 변수를 초기화
        cout << "monster_a 클래스 생성자 (매개변수 추가)" << endl;
    };

    void show_location() {
        cout << "위치(" << location[0] << ", " << location[1] << ")" << endl;
    };

private:
    int location[2];
};


int main() {
    monster_a forest_monster;   // 기본 생성자 호출
    forest_monster.show_location();
    monster_a wood_monster(10, 25);     // 매개변수가 있는 생성자 호출
    wood_monster.show_location();

    return 0;
}

/**
 * 실행 결과
 * 
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자
 * 위치(-858993460, -858993460)
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자 (매개변수 추가)
 * 위치 (10, 25)
 */

/**
 * 실행 결과를 보면 값을 전달하지 않고 생성한 forest_monster 객체는 매개변수가 없는
 * 기본 생성자가 호출된다. 이때는 location 배열이 초기화되지 않아 쓰레기 값(garbage value)이
 * 출력된다. 그런데 값을 전달하면서 생성한 wood_monster 객체는 매개변수가 있는 생성자가 호출된다. 
 * 이때는 location 배열이 객체를 생성할 때 전달한 값(예에서는 10과 25)으로 초기화되어 위치가 
 * 정상으로 출력된다. 
 * 
 * 요약하면 값을 전달하는 생성자를 사용하면 기본 생성자는 실행되지 않는다. 다른 매개변수를 
 * 가지는 생성자를 여럿 만들 수 있지만, 객체를 생성할 때 입력된 인자에 맞는 생성자만 호출된다. 
 */