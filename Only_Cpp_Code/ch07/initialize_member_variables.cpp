// 같은 클래스의 객체를 2개 생성

/**
 * 멤버 변수 초기화
 * 
 * 클래스는 멤버 변수를 여러 개 가질 수 있다. 어떤 멤버 변수는 객체가 생성되고
 * 나서 여러 동작 중에 값이 정해지기도 하고, 클래스가 생성될 때 값을 정해야 
 * 하기도 한다. 그리고 문법적으로 반드시 초기화해야 하는 변수도 있다. 
 * 
 * 객체가 생성될 때 초기화가 필요한 멤버 변수는 생성자를 이용해야 한다. 특별히 
 * 레퍼런스 멤버 변수와 상수 멤버 변수는 생성자에서 반드시 초기화해야 하며, 정적
 * 멤버 변수는 전역 범위에서 초기화해야 한다. 멤버 변수 종류별로 초기화 방법을 
 * 알아보도록 하자. 
 * 
 * 일반 멤버 변수 초기화
 * 
 * 일반 멤버 변수는 생성자에서 일반적인 대입 연산자로 초기화하는 방법과 생성자 
 * 선언 뒤쪽에 초기화 목록을 이용하는 방법이 있다. 초기화 목록을 이용할 때는 대입
 * 연산이 아닌 직접 초기화(direct initialization) 구문을 사용한다. 
 * 
 * 초기화 목록과 대입 연산을 이용한 초기화
 * monster_b() : monster_type("일반")
 * {
 *      // 초기화 목록을 이용(직접 초기화)
 *      difficult_level = 10;       // 대입 연산 이용(복사 초기화)
 * };
 * 
 * 대입 연산은 데이터가 복사되므로 복사 초기화(copy initialization)라고 한다. 대입
 * 연산은 메모리 공간이 추가로 필요하고 복사가 일어나므로 성능에 미세한 차이가 있다. 
 * 일반 변수는 큰 차이가 없지만 클래스 변수는 직접 초기화(초기화 목록 이용)와 복사
 * 초기화(본문에서 대입 연산) 사이에 차이가 존재한다. 
 * 
 * 레퍼런스 멤버 변수와 멤버 변수 초기화
 * 
 * 클래스의 멤버가 아니더라도 레퍼런스 변수와 상수 변수는 선언과 동시에 값이 정해저야 
 * 한다. 레퍼런스 변수에는 참조할 변수나 객체를 지정해야 하고, 상수 변수에는 값을 
 * 지정해야 한다. 따라서 클래스의 멤버로 선언한 레퍼런스 변수와 상수 변수는 객체를 
 * 생성할 때 자동으로 호출되는 생성자에서 초기화 목록이나 본문의 대입 연산을 통해 반드시
 * 초기화해야 한다. 상수 멤버 변수는 선언과 동시에 값을 지정해 주어도 된다. 
 * 
 * 정적 멤버 변수 초기화
 * 
 * 함수에서 정적 변수를 사용하면 선언과 동시에 값을 지정해야 한다. 함수는 메모리에 한 번
 * 할당되고 사용 범위가 함수로 한정되므로 선언과 동시에 값을 지정하면 된다. 
 * 
 * 하지만 클래스에 선언한 정적 멤버 변수는 조금 다르다. 왜냐하면 클래스 멤버 변수를 static
 * 으로 선언하면 해당 클래스로 생성하는 모든 객체에서 참조할 수 있기 때문이다. 객체가 언제
 * 어디서 생성될지 사전에 알 수 없으므로 프로그램이 구동되는 시점에 값이 지정되어야 한다. 
 * 즉, 클래스에 선언한 정적 변수는 전역 범위에서 초기화해야 한다. 
 * 
 * 예컨대 다음은 monster_b 클래스에 정적 변수로 선언한 total_count를 여러 곳에서 접근하는
 * 모습을 보여 준다. 
 * 
 * (stack memory)                                               (전역 메모리)
 * first_monster            second_monster          =>      
 * first_monster.hp         second_monster.hp       =>      monster_b::total_count
 * first_monster.power      second_monster.power 
 * 
 * 정적 멤버 변수는 전역 범위에서 초기화되므로 어떤 클래스에 속한 멤버인지 알 수 있도록 네임스페이스를
 * 추가해 준다. 
 * 클래스_이름::정적_멤버_변수 = 값;        // 클래스 범위 밖의 전역에서 초기화
 * 
 * 이처럼 정적 멤버 변수는 전역 범위 어디에서나 초기화할 수 있지만, 가독성을 위해 클래스가 선언된 소스
 * 파일의 최상단이나 클래스 선언부 밑에 작성하는 편이 좋다. 참고로 헤더 파일에는 정적 멤버 변수를 
 * 초기화하는 코드를 작성할 수 없다. 헤더 파일은 여러 곳에서 포함할 수 있어서 중복 초기화가 발생할 수 
 * 있기 때문이다. 
 * 
 * * 멤버 변수 초기화
 * class monster_b : public monster, character 
 * {
 * pulbic: 
 *      monster_b(player & attack_target)
 *          : monster_type("일반"),             // 직접 초기화
 *          location{0, 0},                     // 유니폼 초기화
 *          unique_id(++total_count),           // 상수 변수 초기화
 *          target(attack_target)               // 레퍼런스 초기화
 *          {
 *              difficult_lavel = 10;           // 복사 초기화
 *              quiz = new char[1024];          // 동적 메모리 할당
 *          };
 * 
 * private:
 *      string monster_type;                    // 멤버 변수 목록
 *      int location[2];
 *      static int total_count;
 *      const int unique_id;
 *      player &target;
 *      int difficult_level;    
 *      char *quiz;
 * };
 * 
 * int monster_b::total_count = 0;              // 정적 변수 초기화
 * 
 * 1) 유니폼 초기화: 배열 형태의 멤버 변수를 초기화, 생성자 정의부에도 똑같은 형태로 초기화할 수 있다. 
 *      많은 원소를 가진 배열 형태의 멤버 변수 초기화에 유용함. 
 * 2) 상수 멤버 변수 초기화: 
 *      상수 멤버 변수는 변경할 수 없으므로 객체 생성과 동시에 값이 정해져야 한다. 따라서 초기화 목록에서
 *      초기화해야 한다. 
 * 3) 레퍼런스 멤버 변수 초기화: 
 *      레퍼런스 멤버 변수는 변경할 수 없으므로 객체 생성 동시에 값이 정해져야 한다. 따라서 초기화 목록에서
 *      초기화해야 한다. 
 * 4) 복사 초기화: 
 *      정의부에서 멤버 변수에 값을 직접 대입한다. 
 * 5) 동적 메모리 할당: 
 *      포인터 변수의 메모리는 필요에 따라 생성자에서 초기화할 수 있다. 
 * 6) 멤버 변수 목록: 
 *      초기화할 멤버 변수 목록이다. 
 * 7) 정적 멤버 변수 초기화: 
 *      정적 멤버 변수는 프로그램 시작과 동시에 값이 지정돼야 하므로 전역 범위에서 초기화한다. 
 */

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

    monster_b second_mon(first_player);
    second_mon.set_quiz("문이 뒤집어 지면 무엇이 될까?");
    second_mon.set_location(45, 50);

    cout << "[" << first_mon.get_x_location() 
         << " , " << first_mon.get_y_location() 
         << "] 첫 번째 몬스터(" << first_mon.get_type()
         << " - " << first_mon.get_difficult_level()
         << ")가 내는 수수께끼 : " << first_mon.get_quiz() << endl;

    cout << "[" << second_mon.get_x_location()
         << " , " << second_mon.get_y_location()
         << "] 두 번째 몬스터(" << second_mon.get_type()
         << " - " << second_mon.get_difficult_level()
         << ")가 내는 수수께끼 : " << second_mon.get_quiz() << endl;

    return 0; 
}