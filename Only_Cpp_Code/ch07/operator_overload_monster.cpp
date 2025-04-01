// + 연산자 오버로딩(몬스터 C 합체)

/**
 * 연산자 오버로딩
 * 
 * 이번에는 연산자 오버로딩을 활용해서 몬스터 C끼리 서로 합체하면 레벨이 한 단계 상승하는 
 * 함수를 만든다고 생각해 보자. 두 몬스터 C를 합치는 함수는 어떻게 만들까? 함수 이름을 
 * 짓는 것부터 고민이다. 만약 단순히 '+' 연산자로 합칠 수 있다면 좋겠다. 
 * monster_c new_monster_c_obj = monster_c_obj1 + monster_c_obj2;
 * 
 * 코드도 간단해지고 이해하기도 매우 쉽지만, 이대로 작성하고 컴파일하면 오류가 발생한다. 
 * 
 * 숫자나 문자열에 사용하던 덧셈 연산자로는 객체를 더할 수 없다. 앞서 살펴본 복사 생성자처럼
 * 개발자가 직접 정의해 주어야 한다. 클래스에는 얇은 복사를 수행하는 대입 연산자가 기본으로
 * 정의되어 있으며, 필요할 때 복사 생성자를 오버라이딩해서 사용한다. 복사 생성자는 매개변수
 * 구성이 같으므로 이미 정의된 함수를 오버라이딩 한다. 
 * 
 * 비슷한 개념으로 몬스터 C끼리 합체하는 덧셈은 이미 정의된 더하기 연산에서 피연산자를 변경
 * 하는 것이다. 즉, int + int, string + string처럼 정의된 더하기 연산에서 int, string 대신에
 * monster_c 객체를 사용해야 한다. 따라서 같은 이름으로 함수 정의를 추가하는 오버로딩을 이용해서
 * 더하기 연산자 함수를 만들어야 한다. 이를 연산자 오버로딩(operator overloading)이라고 한다. 
 * 
 * 연산자 오버로딩에서 함수 이름은 operator 키워드에 새로 정의할 연산자 기호를 붙여서 선언하며, 
 * 일반적으로 이 연산에 참여할 피연산자를 매개변수로 구성한다. 
 * 연산자 오버로딩
 * 반환_형식 operator연산자_기호 (매개변수);
 * 
 * 몬스터 C 객체끼리 덧셈하는 연산자를 오버로딩해 보겠다. 
 */

#include <iostream>
#include <string>

using namespace std;



class character 
{
public:
    character() : hp(100), power(100), location{ 0,0 }, level(1) {};
    void move(int x, int y) {};
    void move(int x[], int y[], int spot_count) {};
    void get_damage(int _damage) {};
    int get_hp() { return hp; };
    int get_level() { return level; };

protected:
    int hp;
    int power;
    int location[2];
    int level;
};



class player : public character 
{
public:
    player() {};
};



// 기본 Monster 클래수
class monster 
{
public:
    void attack(player target_player) {};
    virtual void attack_special(player target_player);
};


void monster::attack_special(player target_player) 
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 몬스터 C는 기본 Monster 클래스로부터 상속
class monster_c : public monster, public character 
{
public:
    // 상속받은 함수 오버라이딩
    void attack_special(player target_player) override;
    monster_c operator+(monster_c& operand);
    void set_level(int level_value) { level = level_value; };
    void set_hp(int hp_value) { hp = hp_value; };
};


// 덧셈 연산자 오버로딩 구현
monster_c monster_c::operator+(monster_c& operand) 
{
    monster_c result_monster;
    result_monster.set_level(level + operand.get_level());
    return result_monster;
}


void monster_c::attack_special(player target_player) 
{
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}



int main() 
{

    monster_c monster_c_obj1, monster_c_obj2;
    monster_c_obj2.set_level(2);
    monster_c new_monster_c_obj = monster_c_obj1 + monster_c_obj2;

    cout << "합체전 몬스터 C #1 Level[" << monster_c_obj1.get_level()
         << "], 몬스터 C #2 Level[" << monster_c_obj2.get_level()
         << "]" << endl;
    
    cout << "합체 후 몬스터 C Level[" << new_monster_c_obj.get_level() << "]" << endl;


    return 0;
}

/**
 * 실행 결과
 * 
 * 합체 전 몬스터 C #1 Level[1], 몬스터 C #2 Level[2]
 * 합체 후 몬스터 C Level[3]
 */

/**
 * 객체끼리 덧셈하는 monster_c_obj1 + monster_c_obj2 코드에서 더하기 연산을 수행하는 주체는
 * monster_c_obj1이고 피연산자는 monster_c_obj2이다. 
 * 따라서 해당 코드를 monster_c_obj1.operator + (monster_c_obj2)처럼 작성해도 똑같이 동작한다. 
 * 하지만 더하기 연산자만 사용하는 편이 더 쉽다. 
 * 
 * 함수의 이름은 operator+이고 매개변수로는 monster_c 객체의 레퍼런스를 입력 받는다. 만약
 * 매개변수의 데이터 형식을 바꿔 정의하면 다른 클래스의 객체를 받을 수 있다. 즉, monster_c와 
 * 다른 클래스의 객체를 덧셈할 수 있다. 
 */