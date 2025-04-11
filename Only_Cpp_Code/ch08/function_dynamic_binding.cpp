// 함수의 동적 바인딩

/**
 * 가상 함수는 자식 클래스가 부모 클래스로 변환되더라도 자식 클래스의 오버라이딩 함수를 사용한다. 
 * 이렇게 동작하는 이유는 가상 함수가 '가상 함수 테이블'을 통해 동적으로 바인딩되기 때문이다. 여기서는 
 * 동적 바인딩과 가상 함수 테이블이 무엇인지 알아보겠다. 
 */

/**
 * 바인딩
 * 
 * 프로그램을 실행하면 함수 호출이나 변수 참조가 해당 코드와 연결되는데, 이 과정을 바인딩(binding)이라
 * 한다. 바인딩은 정적 바인딩(static binding)과 동적 바인딩(dynamic binding) 두 가지 종류가 있으며,
 * 각각 '이른 바인딩(early binding)', 늦은 바인딩(late binding)'이라고도 한다. 
 * 
 * 정적 바인딩은 컴파일 시점에 동작한다. 즉, 정적으로 바인딩되는 대상은 컴파일할 때 결정되어 프로그램이
 * 실행되는 동안 그대로 유지된다. C++ 언어는 auto 변수 외에는 형식 추론을 하지 않으므로 일반 변수와 함수,
 * 클래스, 정적 멤버 함수, 템플릿 등 대부분을 정적으로 바인딩한다. 
 * 
 * 다음은 함수 호출에서 정적 바인딩을 나타낸 것이다.
 * 
 * [stack memory]
 * 메모리 주소: 0xAE1F4C
 * --------------------------------------------------------
 * | void print_out_array(string pre, int(&array)[10])    |
 * |{                                                     |
 * |    cout << pre;                                      |
 * |                                                      |
 * |    for (int i = 0; i < 10; ++i)                      |
 * |    {                                                 |
 * |        cout << array[i] << " , ";                    |
 * |    }                                                 |
 * |    cout << endl;                                     |
 * |}                                                     |
 * --------------------------------------------------------
 * 
 * 메모리 주소: 0xAB104A
 * --------------------------------------------------------
 * | int main(void)                                       |
 * |{                                                     |
 * |    int array[10] = {7, 8, 2, 5, 3, 9, 0, 4, 1, 6};   |
 * |                                                      |
 * |    sort(array, array + 10);                          |
 * |    print_out_array("정렬 후: ", array);              |
 * |                                                      |
 * |    return 0;                                         |
 * |}                                                     |
 * --------------------------------------------------------'
 * 
 * 정적 바인딩에서 고정되는 것
 * 정적 바인딩이라고 해서 항상 같은 메모리 주소가 저장되는 것이 아니라, 바인딩 대상이 컴파일 시점에
 * 결정되는 것이다. 실제 참조할 메모리 주소는 프로그램을 실행할 때마다 달라진다. 따라서 정적 바인딩은
 * 실제 메모리 주소를 고정하는 것이 아니라, 바인딩 대상이 있는 위치를 고정하는 것으로 이해하면 된다. 
 */

/**
 * 함수의 동적 바인딩
 * 
 * 정적 바인딩이 컴파일 시점에 대상을 미리 정해놓은 것이라면, 동적 바인딩은 대상이 실행 시점에 결정되며
 * 변경될 수 있다. C++에서는 가상 함수 그리고 자식 클래스로 치환된 부모 클래스의 포인터가 동적으로 바인딩
 * 된다. 
 * 
 * 정적으로 바인딩된 대상은 고정되므로 만약 고정된 대상을 변경하려면 소스 코드를 수정하고 다시 컴파일해야 
 * 한다. 반면에 동적으로 바인딩된 대상은 프로그램이 실행되는 동안에 수시로 변경될 수 있다. 
 * 
 * 몬스터의 특수 공격을 가상 함수로 구현한 코드를 보면서 동적 바인딩을 살펴보도록 하자. 
 */
#include <iostream>

using namespace std;



class character 
{
public:
    character() : hp(100), power(100) {};
    void get_damage(int _damage) {};


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


// 기본 Monster 클래스
class monster 
{
public:
    monster() {};
    virtual void attack_special(player target_player);
};

void monster::attack_special(player target_player) 
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


class monster_a : public monster, character 
{
public:
    virtual void attack_special(player target_player) override;
};

void monster_a::attack_special(player target_player) 
{
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


int main() 
{
    player player_1;

    monster mother_monster;
    monster_a forest_monster;

    mother_monster.attack_special(player_1);

    monster* mon = &forest_monster;
    cout << endl << "부모 클래스로 업캐스팅 후 공격" << endl;
    mon->attack_special(player_1);

    mon = &mother_monster;
    cout << endl << "부모 클래스로 공격" << endl;
    mon->attack_special(player_1);

    return 0;
}

/**
 * 기본 공격 : 데미지 - 10 hp
 * 
 * 부모 클래스로 업캐스팅된 후 공격
 * 인텡글 공격 : 데미지 - 15 hp
 * 
 * 부모 클래스로 공격
 * 기본 공격 : 데미지 - 10 hp
 */

/**
 * 코드에서 부모 클래스의 객체인 mother_monster로 멤버 함수를 직접 호출할 때는 정적으로 바인딩된 함수가
 * 호출되며, 클래스 포인터 mon으로 호출할 때는 동적으로 바인딩된 함수가 호출된다. 정적 / 동적ㅇ느로 바인딩된
 * 함수가 호출하는 부분을 컴파일하면 내부적으로 다음과 같은 어셈블리어 코드가 만들어진다. 
 * 
 * mother_monster.attack_special(player_1);
 * => call      monster::attack_special (0xAE1F4C)
 * 
 * monster *mon = &forest_monster;
 * => lea       rax, [forest_monster]
 * => mo        aword ptr [mon], rax
 * 
 * mon->attack_special(player_1);
 * => call      aword ptr[rax]
 * 
 * 이를 해석하면 monster::attack_special 함수를 주어진 메모리 주소(0xAE1F4C)에서 호출한다. forest_monster 변수의
 * 주소를 rax 레지스터(어셈플리어, 레지스터 등은 컴퓨터 구조나 운영체제에 따라 다르다)에 불러오고, 그 주솟값을 
 * mon이라는 메모리 주소에 64비트 데이터로 복사한다(mov). 그리고 rax 레지스터에 저장된 주소로 이동하여 해당 주소에
 * 위치한 함수를 호출한다. 
 * 
 * 즉, 코드에서 부모 클래스의 객체인 mother_monster로 멤버 함수를 직접 호출할 때는 정적으로 바인딩된 함수가 호출되므로
 * 함수의 주소(0xAE1F4C)로 바로 이동하지만, 클래스 포인터 mon으로 호출할 때는 클래스의 객체로 이동한 후 객체에서 해당
 * 함수의 주소로 이동한다. 따라서 mon이 가리키는 객체의 attack_special 함수 호출문에 동적으로 바인딩된 주소를 찾아서
 * 호출한다. 
 * 
 * 동적 바인딩을 처음 공부한다면 프로그램이 실행되는 동안에 동적으로 바인딩된 함수는 호출 대상이 바뀔 수 있다는 것만
 * 기억하면 된다. 즉, 바인딩 대상이 계속 변경될 수 있어서 동적 바인딩이라고 한다. 
 */