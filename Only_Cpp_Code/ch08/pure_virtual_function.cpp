// 순수 가상 함수를 선언하고 자식 클래스에서 정의함

/**
 * 순수 가상 함수
 * 
 * 앞서 살펴본 가상 함수 코드를 보면 부모 클래스에도 함수를 정의했다. 
 * 그런데 부모 클래스에서는 가상 함수를 선언만 하고 자식 클래스에서 정의하도록 강제할 수도 있다. 이러한 함수를
 * 순수 가상 함수(pure virtual function)라고 한다. 부모 클래스에서는 동작하지 않지만 자식 클래스의 기능을 미리
 * 선언하고 싶을 때 사용한다. 
 * 
 * 순수 가상 함수 선언
 * 클래스에서 가상 함수를 선언만 하고 정의하지 않으면 오류가 발생하므로 순수 가상 함수를 선언하려면 다음처럼
 * 마지막 부분에 " = 0"을 추가해야 한다. 
 * virtual void attack_special(player target_player) = 0;
 * 
 * 순수 가상 함수로 선언한 후에는 이 클래스를 상속받는 자식 클래스에서 반드시 정의해야 한다. 만약 상속받은 클래스
 * 에서도 정의하지 않고 자식 클래스를 상속받는 또 다른 클래스에서 정의하게 사려면 자식 클래스에서 다시 순수 가상
 * 함수로 선언하면 된다. 
 * 
 * 순수 가상 함수 활용
 * 몬스터 코드를 조금 변형해 순수 가상 함수의 사용법을 알아보겠다. 몬스터들이 새벽이 되면 공격하는 기능을 추가해
 * 보겠다. 지금까지 만들어 온 monster_a, monster_b, monster_c에는 새벽 공격 기능을 멤버 함수나 가상 함수로 추가
 * 할 수 있겠지만, 앞으로 만들 새로운 몬스터 클래스에서는 실수로 빠뜨릴 수도 있다. 따라서 순수 가상 함수로 만들어 
 * 자식 클래스에서 정의하도록 하겠다. 
 * 
 * 몬스터 클래스의 계층 구조에서 최상위인 monster 클래스에 attack_at_dawn이라는 순수 가상 함수를 만들겠다. 즉, 
 * monster 클래스에서는 attack_at_dawn 가상 함수 선언만 하고 자식 클래스에서 강제로 정의하도록 하겠다. 
 */

#include <iostream>
#include <list>

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


class player : public character 
{
public:
    player() {};
};


class monster 
{
public:
    monster() {};
    void attack(player target_player) {};
    virtual void attack_special(player target_player);
    virtual void attack_at_dawn() = 0;  // 순수 가상 함수로 선언
};

void monster::attack_special(player target_player) 
{
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


class monster_a : public monster, character 
{
public:
    // 상속받은 함수 오버라이드 선언 
    virtual void attack_special(player target_player) override;
    virtual void attack_at_dawn() override;
};

void monster_a::attack_at_dawn() 
{
    cout << "동쪽에서 기습!" << endl;
}

void monster_a::attack_special(player target_player) 
{
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


class monster_b : public monster, character 
{
public:
    virtual void attack_special(player target_player) override;
    virtual void attack_at_dawn() override;
};

void monster_b::attack_special(player target_player) 
{
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}

void monster_b::attack_at_dawn() 
{
    cout << "적진에 조용히 침투하여 방화!" << endl;
}


class monster_c : public monster, character 
{
public:
    virtual void attack_special(player target_player) override;
    virtual void attack_at_dawn() override;
};

void monster_c::attack_special(player target_player) 
{
    cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
}

void monster_c::attack_at_dawn() {
    cout << "남쪽에서 적진을 향해 대포 발사!" << endl;
}


int main() 
{
    list<monster*> mon_list;

    monster_a first_monster;
    mon_list.push_back(&first_monster);

    monster_b second_monster;
    mon_list.push_back(&second_monster);

    monster_c third_monster;
    mon_list.push_back(&third_monster);

    for (auto item : mon_list) 
    {
        item->attack_at_dawn();
    }

    return 0;
}

/**
 * 실행 결과 
 * 동쪽에서 기습!
 * 적진에 조용히 침투하여 방화!
 * 남쪽에서 적진을 향해 대포 발사!
 */

/**
 * 모든 자식 클래스에서 순수 가상 함수를 오버라이딩했으므로 정상으로 실행된다. 코드에서 마지막 부분의 for 문을
 * 살펴보면 mon_list의 모든 객체를 부모 클래스인 monster* 형으로 업캐스팅했지만, 각 클래스에서 오버라이딩한 
 * 가상 함수가 실행된 것을 확인할 수 있습니다. 
 */

/**
 * monster 클래스에 선언한 attack_at_dawn()은 순수 가상 함수이므로 상속받은 자식 클래스에서 
 * 구현하지 않으면 컴파일 오류가 발생한다. 오류 메시지는 두 가지이다. 첫 번째는 순수 가상 함수를
 * 정의하지 않았다는 오류이고, 두 번째는 추상 클래스를 인스턴스화할 수 없다는 오류이다. 
 * 
 * 첫 번째 오류는 앞서 이야기한 것처럼 가상 함수 오버라이딩을 문법적으로 강제해서 발생한다 두 번째
 * 오류는 추상 클래스와 관련된 내용이다. 대게 첫 번째 오류를 해결하면 함께 해결된다. 
 * 
 * 이처럼 자식 클래스에서 오버라이딩을 강제하는 방법으로 순수 가상 함수를 사용할 수 있다. 이제 monster_a, 
 * monster_b, monster_c 클래스에서 attack_at_dawn 함수를 정의하고 결과를 확인해보자. 
 */