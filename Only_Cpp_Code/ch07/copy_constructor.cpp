// 복사 생성자를 깊은 복사로 재정의

#include <iostream>
#include <string>

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


class monster_b : public monster, character {
public:
    monster_b(player &attack_target)
        : monster_type("일반")
        , location{0, 0}
        , unique_id(++total_count)
        , target(attack_target) {
        difficult_level = 10;
        quiz = new char[1024];
    };

    ~monster_b() {
        delete[]quiz;
        total_count--;
    };

    monster_b(const monster_b &ref);    // 복사 생성자 선언

    // ...(생략)...

};


int monster_b::total_count = 0;     // 정적 변수 초기화


monster_b::monster_b(const monster_b &ref) : unique_id(++total_count), target(ref.target)
{
    // 복사 생성자 정의(깊은 복사)
    quiz = new char[1024];
    strcpy_s(quiz, strlen(ref.quiz) + 1, ref.quiz);
    monster_type = ref.monster_type;
    difficult_level = ref.difficult_level;
    location[0] = ref.location[0];
    location[1] = ref.location[1];
}

// ...(생략)...