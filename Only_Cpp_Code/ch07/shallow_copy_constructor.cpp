// 객체를 대입하여 생성

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


class monster_b : public monster, character {
public:
    monster_b(player &attack_target)
        : monster_type("일반")
        , location{0, 0}
        , unique_id(++total_count)
        ,target(attack_target) {
        difficult_level = 10;
        quiz = new char[1024];
    };

    ~monster_b() {      // 객체가 소멸할 때 자동으로 호출되는 소멸자
        delete[]quiz;
        total_count--;
    };

    void set_quiz(const char *new_quiz) {
        strcpy_s(quiz, 1024, new_quiz);
    };
    void set_type(string type) {
        monster_type = type;
    };
    void set_difficult_level(int level) {
        difficult_level = level;
    };
    void set_location(int x, int y) {
        location[0] = x, location[1] = y;
    };
    char *get_quiz() {
        return quiz;
    };
    string get_type() {
        return monster_type;
    };
    int get_difficult_level() {
        return difficult_level;
    };
    int get_x_location() {
        return location[0];
    };
    int get_y_location() {
        return location[1];
    };


private:
    string monster_type;
    int location[2];
    static int total_count;
    const int unique_id;
    player &target;
    int difficult_level;
    char *quiz;
};


int monster_b::total_count = 0;     // 정적 변수 초기화


int main() {
    player first_player;
    monster_b first_mon(first_player);
    
    first_mon.set_quiz("아침에 네 발, 점심에는 두 발, 저녁에는 두 발인 것은?");
    first_mon.set_difficult_level(100);
    first_mon.set_type("수수께끼 몬스터");
    first_mon.set_location(30, 30);

    monster_b second_mon = first_mon;
    second_mon.set_quiz("문이 뒤집어 지면 무엇이 될까?");
    second_mon.set_location(45, 50);
    
}