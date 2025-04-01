// 복사 생성자를 깊은 복사로 재정의

/**
 * 얕은 복사
 * 
 * 객체를 초기화할 때 똑같은 클래스로 생성한 객체를 대입하면 멤버 변수들이 그대로 복산된다. 
 * 이때 정적으로 할당된 멤버 변수는 변수가 생성되고 값이 복사된다. 반면에 동적으로 할당된
 * 멤버 변수는 메모리를 할당하지 않고 대입한 객체의 멤버 변수를 포인터로 참조한다. 이를 
 * 얕은 복사(shallow copy)라고 한다. 
 * 
 * 즉, 수수께끼를 저장하는 char *quiz는 동적으로 할당되므로 두 번째 객체는 첫 번째 객체에서
 * 할당한 메모리를 참조한다. 따라서 두 번째 객체에서 변경한 내용이 첫 번째 객체에도 그대로
 * 반영된다. 
 * 
 *                  (stack memory)                                                (haep memory)
 * first_monster                    second_monster                  =>            
 * first_monster.hp                 second_monster.hp               =>
 * first_monster.power              second_monster.power            =>
 * first_monster.quiz               second_monster.quiz             =>          first_monster.quiz
 * first_monster.monster_type       second_monster.monster_type     =>
 * first_monster.difficult_level    second_monster.difficult_level  =>
 * first_monter.location[2]         second_monster.location[2]      =>
 * 
 * 앞선 예시에서 오류가 발생했던 이유는 얕은 복사로 인해 똑같은 메모리 영역을 참조하고 있는데
 * 첫 번째 객체가 소멸(메모리 해제)한 후, 두 번째 객체에서 같은 메모리를 해제하려고 시도하기
 * 때문이다.
 */

/**
 * 깊은 복사
 * 
 * 이 문제를 해결하려면 동적으로 메모리가 할당된 멤버 변수의 값은 깊은 복사(deep copy)가 이뤄지도록
 * 해야 한다. 객체를 같은 클래스로 생성한 객체로 초기화하면 얕은 복사를 수행하는 기본 복사 생성자가
 * 호출된다. 얕은 복사가 아닌 깊은 복사가 되게 하려면 기본 복사 생성자를 오버라이딩해야 한다. 먼저
 * 복사 생성자의 형태를 알아보겠다. 
 * 
 * 복사 생성자 선언
 * 클래스_이름::클래스_이름(const 클래스_이름 &레퍼런스_변수);
 * 
 * 같은 클래스로 생성된 객체의 레퍼런스를 매개변수로 받아서 원하는 형태의 복사를 수행하는 것이다. 몬스터
 * B 클래스의 경우 monster_b::monster_b(const monster_b &ref)으로 선언할 수 있다. 복사 생성자를 
 * 오버라이딩한 후에 멤버 변수에 값을 저장하거나 동적 메모리를 할당하여 메모리의 위치가 아니라 메모리에
 * 저장된 값을 복사한다. 
 */

#include <iostream>
#include <string>
using namespace std;

class character {
public:
  character() : hp(100), power(100) {
  };

  void get_damage(int _damage) {};
protected:
  int hp;
  int power;
};

//Player 클래스
class player : public character {
public:
  player() {};
};

//기본 Monster 클래스
class monster {
public:
  void attack(player target_player) {};
  virtual void attack_special(player target_player);
};

void monster::attack_special(player target_player) {
  cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


//몬스터 A는 기본 Monster 클래스로부터 상속
class monster_b : public monster, character {
public:
  monster_b(player& attach_target)
    : monster_type("일반"),       // 직접 초기화
    location{ 0,0 },              // 유니폼 초기화
    unique_id(++total_count),     // 상수 변수 초기화
    target(attach_target) {       // 레버런스 변수 초기화
    difficult_level = 10;         // 복사초기화
    quiz = new char[1024];        // 동적 메모리 할당
  };

  ~monster_b() {
    delete[]quiz;
    total_count--;
  };

  monster_b(const monster_b& ref);

  //상속받은 함수 오버라이딩 
  virtual void attack_special(player target_player) override {
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
  };

  void set_quiz(const char* new_quiz) { strcpy_s(quiz, 1024, new_quiz); };
  void set_type(string type) { monster_type = type; };
  void set_difficult_level(int level) { difficult_level = level; };
  void set_location(int x, int y) { location[0] = x; location[1] = y; };
  char* get_quiz() { return quiz; };
  string get_type() { return monster_type; };
  int get_difficult_level() { return difficult_level; };
  int get_x_location() { return location[0]; };
  int get_y_location() { return location[1]; };

private:
  const int unique_id;
  player& target;
  static int total_count;
  char* quiz;
  string monster_type;
  int difficult_level;
  int location[2];
};

int monster_b::total_count = 0; // 정적 변수 초기화

monster_b::monster_b(const monster_b& ref) : unique_id(++total_count), target(ref.target) {
  quiz = new char[1024];
  strcpy_s(quiz, strlen(ref.quiz) + 1, ref.quiz);
  monster_type = ref.monster_type;
  difficult_level = ref.difficult_level;
  location[0] = ref.location[0];
  location[1] = ref.location[1];
}

int main() {
  player first_player;
  monster_b first_mon(first_player);
  first_mon.set_quiz("아침에 네발, 점심에는 두발, 저녁에는 두발인 것은?");
  first_mon.set_difficult_level(100);
  first_mon.set_type("수수께끼 몬스터");
  first_mon.set_location(30, 30);

  monster_b second_mon = first_mon;
  second_mon.set_quiz("문이 뒤집어 지면 무엇이 될까?");
  second_mon.set_location(45, 50);


  cout << "[" << first_mon.get_x_location() << " , " << first_mon.get_y_location()
    << "] 첫번째 몬스터(" << first_mon.get_type() << " - "
    << first_mon.get_difficult_level()
    << ")가 내는 수수께끼 : " << first_mon.get_quiz() << endl;
  cout << "[" << second_mon.get_x_location() << " , " << second_mon.get_y_location()
    << "] 두번째 몬스터(" << second_mon.get_type() << " - "
    << second_mon.get_difficult_level()
    << ")가 내는 수수께끼 : " << second_mon.get_quiz() << endl;

  return 0;
}