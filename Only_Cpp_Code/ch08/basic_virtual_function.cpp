// 가상 함수 선언으로 인한 호출 변화

/**
 * 가상 함수와 동적 바인딩
 * 
 * 가상 함수는 객체지향 프로그래밍에서 다형성을 구현하는 데 필요하다. 다형성은 한 클래스가
 * 다양한 방식의 속성과 기능을 가질 수 있는 특성을 말한다. 가상 함수는 부모를 상속받은 자식
 * 클래스에 의해서 동작한다. 
 * 
 * 가상 함수란?
 * C++에서 다형성을 구현할 때 멤버 함수 가운데 자식 클래스에서 오버라이딩(재정의)해야 하는 
 * 가상 함수(virtual function)로 선언해야 한다. 일반 멤버 함수도 자식 클래스에서 오버라이딩
 * 할 수 있지만, 가상 함수로 선언하는 이유는 부모 클래스로 업캐스팅(upcasting)되었을 때 호출
 * 되는 함수에 차이가 있기 때문이다. 
 * 
 * 일반 멤버 함수는 업캐스팅된 부모 클래스에 구현된 함수가 호출되지만, 가상 함수는 자식 클래스
 * 에서 오버라이딩한 함수가 호출된다. 이러한 특징 덕분에 가상 함수로 다형성을 구현할 수 있는
 * 것이다. 
 */

/**
 * 가상 함수 선언과 구현, 사용 방법
 * 가상 함수는 클래스의 멤버 함수를 선언할 때 앞부분에 virtual 키워드를 붙이면 된다. 
 * virtual 반환_형식 함수_이름(매개변수);
 * 
 * 자식 클래스에서 가상 함수를 오버라이딩할 때도 똑같은 선언문을 사용한다. 마지막에 override 
 * 키워드는 추가하지 않아도 되지만, 부모 클래스의 멤버 함수를 오버라이딩할 것을 알려 주는 역할을
 * 한다. 또한 가상 함수를 재정의할 때에 다른 함수 시그니처를 입력하는 실수도 방지한다. 
 * 
 * 가상 함수 오버라이딩 선언
 * virtual 반환_형식 함수_이름(매개변수) override;
 * 
 * 가상 함수
 * class monster
 * {
 * public: 
 *      void attack(player target_player) {};
 *      // (1) 가상 함수 선언
 *      virtual void attack_special(player target_player);
 * };
 * 
 * // (2) 가상 함수 정의
 * void monster::attack_special(player target_player) {...}
 * 
 * 
 * class monster_c : public monster 
 * {
 * public: 
 *      // (3) 가상 함수 오버라이드 선언
 *      virtual void attack_special(player target_player) override;
 * };
 * 
 * // (4) 가상 함수 오버라이딩(재정의)
 * void monster_c::attack_special(player target_player) {...}
 * 
 * 
 * (1) 가상 함수 선언: 가상 함수 선언은 virtual 키워드를 추가하는 것만 다르고 일반 함수 선언과 같다. 
 * (2) 가상 함수 정의: 가상 함수 정의는 일반 함수와 같다. 
 * (3) 가상 함수 오버라이드 선언: 자식 클래스에서 가상 함수 오버라이드를 선언할 때는 마지막에 override
 * 키워드를 추가한다. 
 * (4) 가상 함수 오버라이딩(재정의): 자식 클래스에 오버라이딩된 가상 함수 정의는 일반 오버라이딩 함수와 같다. 
 */

/**
 * 가상 함수로 다형성 구현
 * 가상 함수를 사용하는 가장 큰 목적은 다형성 구현 때문이다. 리스코프 치환 원칙에 따라 자식 클래스가 부모 클래스를
 * 대체하더라도(업캐스팅) 부모 클래스의 멤버 함수가 아닌 자식 클래스에 오버라이딩한 함수가 호출돼야 다형성이 구현
 * 된다. 가상 함수로 다형성을 구현하는 코드를 보면서 의미를 알아보도록 하자. 
 */

#include <iostream>

using namespace std;



class character 
{
public:
    character() : hp(100), power(100) {};


protected:
    int hp;
    int power;
};


// Player 클래스
class player : public character 
{
public:
    player() {};
};


// 기본 monster 클래스
class monster 
{
public: 
    monster() {};
    void attack(player target_player) {};
    virtual void attack_special(player target_player);  // 가상 함수 선언
};


void monster::attack_special(player target_player) 
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 몬스터 A는 기본 monster 클래스로부터 상속
class monster_a : public monster, character 
{
public:
    // 가상 함수 오버라이드 선언
    virtual void attack_special(player target_player) override;
};


// 가상 함수 오버라이딩
void monster_a::attack_special(player target_player) 
{
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


// 몬스터 B는 기본 Monster 클래스로부터 상속
class monster_b : public monster, character 
{
public:
    // 상속받은 함수 오버라이딩
    virtual void attack_special(player target_player) override;
};

void monster_b::attack_special(player target_player) 
{
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}


// 몬스터 C는 기본 Monster 클래스로부터 상속
class monster_c : public monster, character 
{
public:
    // 상속받은 함수 오버라이딩
    virtual void attack_special(player target_player) override;
};

void monster_c::attack_special(player target_player) 
{
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}


int main() 
{
    player player_1;

    monster_a forest_monster;

    monster& mon = forest_monster;  // upcasting
    monster_a& mon_a = forest_monster;

    cout << endl << "부모 클래스로 업캐스팅 후 공격" << endl;
    mon.attack_special(player_1);   // monster_a의 오버라이딩 함수 호출

    cout << endl << "자식 클래스로 공격" << endl;
    mon_a.attack_special(player_1);

    cout << endl << "범위 연산자로 공격" << endl;
    mon_a.monster::attack_special(player_1);

    return 0;
}

/**
 * 실행 결과
 * 
 * 부모 클래스로 업캐스팅 후 공격
 * 인텡글 공격 : 데미지 - 15 hp
 * 
 * 자식 클래스로 공격
 * 인텡글 공격 : 데미지 - 15 hp
 * 
 * 범위 연산자로 공격
 * 기본 공격 : 데미지 - 10 hp
 */