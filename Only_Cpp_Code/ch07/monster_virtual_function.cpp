// 가상 함수를 활용한 오버라이딩 함수 호출 변화

/**
 * 가상 함수를 활용한 함수 오버라이딩
 * 
 * 코드에서 forest_monster는 monster_a 클래스의 인스턴스이므로 부모 클래스인
 * monster를 참조하더라도 자신의 오버라이딩 함수가 호출돼야 한다. 즉, mon.attack_special
 * 함수를 호출해도 monster_a 클래스의 오버라이딩된 함수(인텡글 공격 데미지 출력)가 호출돼야 
 * 한다. 그래야지만 자식마다 다양한 특성을 지니는 다형성이 적용되었다고 할 수 있다. 
 * 
 * 이때는 가상 함수(virtual function)를 활용한다. 멤버 함수의 이름 앞에 virtual 이라는 
 * 키워드로 선언하면 가상 함수가 된다. 그리고 자식 클래스에서 가상 함수를 오버라이딩하면
 * 런타임 때에 올바른 버전의 함수가 호출된다. 
 * 
 * 즉, 부모 클래스를 참조하더라도 객체에서 가장 마지막에 오버라이딩된 함수를 호출한다. 
 * 그리고 상위 클래스에 정의된 함수를 호출해야 할 때는 네임스페이스를 활용하면 된다. 
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
    virtual void attack_special(player target_player) {};   // 가상 함수 선언언

};

void monster::attack_special(player target_player) {
    cout << "기본 공격 : 데미지 - 10 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_a : public monster, character {
public:
    // 가상 함수 오버라이드 선언 
    virtual void attack_special(player target_player) override;     
};

// 가상 함수 오버라이딩 
void monster_a::attack_special(player target_special) {
    cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_b : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    virtual void attack_special(player target_player) override;
};

void monster_b::attack_special(player target_special) {
    cout << "가상 공격 : 데미지 - 0 hp" << endl;
}


// 기본 몬스터 클래스 상속
class monster_c : public monster, character {
public:
    // 상속받은 함수 오버라이딩
    virtual void attack_special(player target_player) override;
};

void monster_c::attack_special(player target_special) {
    cout << "강력 뇌전 공격 : - 100 hp" << endl;
}


int main() {
    player player_1;
    monster_a forest_monster;

    monster &mon = forest_monster;      // 부모 클래스의 레퍼런스에 대입
    monster_a &mon_a = forest_monster;  // 자식 클래스의 레퍼런스에 대입

    cout << endl << "부모 클래스 레퍼런스로 공격" << endl;
    mon.attack_special(player_1);

    cout << endl << "자식 클래스 레퍼런스로 공격" << endl;
    mon_a.attack_special(player_1);

    cout << endl << "네임스페이스 활용 공격" << endl;
    mon_a.monster::attack_special(player_1);

    return 0;
}

/**
 * 실행 결과
 * 
 * 부모 클래스 레퍼런스로 공격
 * 인텡글 공격: 데미지 - 15 hp
 * 
 * 자식 클래스 레퍼런스로 공격
 * 인텡글 공격: 데미지 - 15 hp
 * 
 * 네임스페이스 활용 공격
 * 기본 공격: 데미지 - 10 hp
 */

/**
 * 오버라이딩과 오버로딩
 * 
 * 같은 시그니처로 자식 클래스에서 함수를 재정의하는 것을 오버라이딩이라고 한다. 그리고 함수 이름만
 * 같고 매개변수 구성이 다른 함수를 만드는 것을 오버로딩이라고 한다. 오버로딩은 추후에 다루도록 하겠다. 
 * 오버라이딩 함수는 네임스페이스로 원본 함수를 선택해서 호출하지만, 오버로딩 함수는 호출 인자에 따라서 
 * 알맞은 함수가 호출된다. 
 */