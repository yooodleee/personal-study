// 객체를 대입하여 생성

/**
 * 객체를 대입하는 방법으로 main 함수의 소스 코드를 변경하고 실행해 본다. 
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

    monster_b second_mon = first_mon;                       // 변경된 코드
    second_mon.set_quiz("문이 뒤집어 지면 무엇이 될까?");
    second_mon.set_location(45, 50);
    
}

/**
 * 실행 결과
 * 
 * [30, 30] 첫 번째 몬스터 (수수꼐끼 몬스터 - 100)가 내는 수수께끼: 문이 뒤집어 지면 무엇이 될까?
 * [45, 50] 두 번째 몬스터 (수수꼐끼 몬스터 - 100)가 내는 수수께끼: 문이 뒤집어 지면 무엇이 될까?
 */

/**
 * second_mon 객체를 생성할 때 first_mon 객체를 대입한 후에 수수께끼와 위치를 재설정했다. 
 * 몬스터 타입과 난이도, 위치는 의도한 대로 출력되었지만, 수수께끼의 내용이 의도와 다르게
 * 출력되었다. 첫 번째 몬스터의 수수꼐끼 내용이 바뀐 것이다. 
 * 
 * 그리고 다음과 같은 오류도 발생한다(컴파일러에 따라서 오류가 발생하지 않을 수도 있다).
 * Debug Assesion Failed:
 * 
 * Program:
 * _sample_code\x64\Debug\monster_class_with_copy_constructor.exe
 * File: minkernel\crts\curt\src\appcrt\debug_heap.cpp
 * Line: 904
 * 
 * Expression: _CrtsValidHeapPointer(block)
 * 
 * For information on your program can cause an assertion
 * faliure. see the Visul C++ documentation on asserts.
 * 
 * (Press Retry to debug the application)
 * 
 * 이러한 현상은 수수께끼를 저장하는 char *quiz 변수가 동적으로 할당되기 때문에 발생한다. 
 * 반면에 위치를 저장하는 int location[2] 변수는 정적으로 할당되므로 이런 현상이 발생하지
 * 않는다. 
 */