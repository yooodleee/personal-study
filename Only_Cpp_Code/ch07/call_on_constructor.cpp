// 생성자에서 다른 생성자 호출하기

/**
 * 생성자에서 다른 생성자 호출하기 
 * 
 * 생성자에서 다른 생성자를 호출해야 할 수 있다. 예컨대 앞의 코드에서 기본 생성자를 호출하면 
 * 위치를 10, 10으로 설정한다고 가정해보자. 기본 생성자에서 매개변수가 있는 생성자를 호출해본다. 
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
        monster_a(10, 10);  // 생성자에서 다른 생성자 호출
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
 * monster_a 클래스 생성자
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자 (매개변수 추가)
 * 위치 (-858993460, -858993460)
 */

/**
 * 위치가 10, 10으로 설정될 것이라고 예상했지만, 실행 결과를 보면 쓰레기 값이 출력된다. 
 * 그리고 객체는 forest_monster 하나만 생성했는데, 생성자는 부모 클래스는 물론 기본과 
 * 매개 변수가 있는 생성자가 모두 호출되었다. 
 * 
 * 이러한 현상은 객체를 생성해서 지역 변수에 저장하지 않았기 때문에 발생한다. 기본 생성자가
 * 호출되는 객체 생성 코드를 보면 monster_a forest_monster처럼 작성했다. 이 코드는 monster_a
 * 클래스의 객체를 생성해 forest_monster라는 지역 변수에 대입한다. 
 * 
 * 그런데 생성자에서 다른 생성자를 호출하는 코드를 보면 monster_a(10, 10)처럼 생성한 객체를 
 * 대입할 지역 변수 이름이 빠졌다. 즉, 이름이 없는 객체가 된다. 생성자에서 다른 생성자를 호출하는
 * 것이 의도였지만, 실제로는 기본 생성자 내부에서 이름이 없는 객체가 생성되었다가 소멸한다. 
 * 
 * 
 */