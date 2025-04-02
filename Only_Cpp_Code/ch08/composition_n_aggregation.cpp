// 컴포지션과 어그리게이션

/**
 * 컴포지션과 어그리게이션, 두 가지 모두 클래스의 속성과 기능을 직접 구현하지 않고 이전에 정의된 것을
 * 재활용하는 방법이다. 다중 상속은 새 클래스에서 기존 클래스를 코드로 구현하지만, 컴포지션과 어그리게이션은
 * 멤버 객체로 참조하는 방법이다. 이 차이점을 염두에 두고 구체적인 내용을 살펴보겠다. 
 */

/**
 * 다중 상속 다시 보기
 * 
 * 다중 상속(multi inheritance)은 부모 클래스를 여러 개 상속받아 자식 클래스 정의하는 것을 말한다. 다양한
 * 부모 클래스를 상속받기 떄문에 많은 부분이 이미 정의되어 있다. 같은 개발 조직에서 부모 클래스를 개발할 때
 * 안정적이고 견고한 디자인 패턴을 적용해 두면, 이를 상속받아 사용하는 클래스에도 개발 방법론이나 구조를 
 * 흔들림 없이 빠르게 전파할 수 있다.  
 */

/**
 * #include <iostream> 
 * using namespace std;
 * 
 * 
 * // 캐릭터 클래스
 * class character
 * {
 * public: 
 *      character() : hp(100), power(100) {};
 * 
 * protected: 
 *      int hp;
 *      int power;
 * };
 * 
 * 
 * // 캐릭터를 상속받는 플레이어 클래스
 * class player : public character 
 * {
 * public:  
 *      player() {};
 * };
 * 
 * 
 * //  기본 몬스터 클래스
 * class monster
 * {
 * public: 
 *      monster() {};
 *      void get_damage(int _damage) {};
 *      void attack(player target_player) {};
 *      void attack_special(player target_player);
 * };
 * 
 * void monster::attack_special(player target_player)
 * {
 *      cout << "기본 공격 : 데미지 - 10 hp" << endl;
 * }
 * 
 * 
 * // 캐릭터와 기본 몬스터를 상속받는 몬스터 A
 * class monster_a : public monster, character
 * {
 * public: 
 *      void attack_player(player target_player);
 * };
 * 
 * void monster_a::attack_special(player target_player)
 * {
 *      cout << "인텡글 공격 : 데미지 - 15 hp" << endl;
 * }
 * 
 * class monster_b : public monster, character 
 * {
 * public:
 *      void attack_special(player target_player);
 * }
 * 
 * void monster_b::attack_special(player target_player)
 * {
 *      cout << "가상 공격 : 데미지 - 0 hp" << endl;
 * }
 * 
 * class monster_c : public monster, character
 * {
 * public: 
 *      void attack_special(player target_player);
 * }
 * 
 * void monster_c::attack_special(player target_player)
 * {
 *      cout << "강력 뇌전 공격 : 데미지 - 100 hp" << endl;
 * }
 * 
 * // ...(생략)... 
 */

/**
 * 다중 상속 문법은 단일 상속과 크게 다르지 않으므로 어렵지 않을 것이다. 상속받고자 하는 클래스들을 
 * 쉼표로 구분해서 나열하면 된다. 한 가지 주의할 점은 상속 접근 지정자를 명시하지 않으면 private으로
 * 지정된다는 것이다. 
 */

/**
 * 다중 상속 접근
 * 
 * 몬스터 A ~ C 는 기본 monster 클래스를 상속받는다. 몬스터가 가져야 할 기본 속성과 동작을 상속받아
 * 새로운 몬스터를 만들고 해당 몬스터에만 특화된 내용을 정의했다. 이런 관계를 'is-a'라고 한다. is-a
 * 관계에서 자식 클래스는 언제든지 부모 클래스를 대체할 수 있다. 
 * 
 * 그런데 몬스터가 다양한 지형에 특화된 기술을 가진다고 가정해 보자. '지형에 따른 특성'이라는 요소는
 * 모든 몬스터에 적용될 수 있고 캐릭터에 적용될 수 있다. 그러면 여러 지형에 적합한 속성을 클래스로
 * 만든 후 상속받도록 구현할 수 있다. 지형에 따른 속성 외에도 다양한 속성이 추가될 수도 있고 이를 모두
 * 상속으로 구현한다면 어떻게 될까? 다중 상속이 많아질수록 여러 가지 문제가 발생할 수 있다. 
 * 
 * 그중 클래스가 커지고 컴파일 시간이 늘어나는 문제점을 알아보자. 
 * 클래스가 다양한 역할을 수행하게 되는 거대 클래스(large class)는 개발자가 지양해야 할 문제이다. 
 * 클래스가 커지면 그만큼 속성과 기능이 많아지므로 상요하기가 어렵기 때문이다. 그리고 부모 클래스 중 
 * 일부가 변경되면 상속받은 모든 클래스를 다시 컴파일해야 하는데, 자식 클래스가 많거나 다양한 라이브러리에서
 * 사용된다면 변경 사항이 여러 곳에 영향을 주므로 바람직하지 않다. 
 * 
 * 예컨대, 부모 클래스 A, B, C를 상속받은 자식 클래스 E, D, F가 있고, 부모 클래스의 멤버 함수를 상속받아
 * 재정의했다고 가정해 보자. 부모 클래스 A, B, C의 멤버 함수가 변경되면 이를 재정의한 E, D, F도 수정해야
 * 하고 이 함수를 사용하는 클래스나 함수도 역시 수정해야 한다. 
 * 
 * 이처럼 상속이나 사용 관계로 서로 의존도가 높아지면 결합도(coupling)가 높다고 표현한다. 소스 코드는 
 * 결합도가 낮을수록 유지 / 보수가 수월해진다. 거대 클래스는 결합도를 높이는 주요 원인이 되므로 피해야
 * 한다. 
 * 
 * 컴파일 시간이 늘어나는 문제
 * C++는 컴파일 언어이므로 소스 코드가 변경되면 다시 컴파일해서 실행 파일을 만들어야 한다. 클래스 파일이
 * 수십 개라면 몇 분 안에 컴파일이 완료되겠지만, 오픈소스처럼 클래스 파일이 수만 개라면 몇 시간이 걸릴 
 * 수도 있다. 
 * 
 * 물론 변경된 소스 코드만 다시 컴파일하므로 변화의 범위가 적을 때는 반복 컴파일하면서 개발해도 큰 문제는
 * 없다. 하지만 상속 관계가 복잡하고 다중 상속이 복잡하게 엉켜 있으면 컴파일에 많은 시간이 소요되어 개발에
 * 큰 부담이 된다. 
 * 
 * 클래스가 커지더라도 잘 관리하면 문제가 없지 않을까?
 * 클래스가 커지면 관리가 어려워진다. 객체지향 개발의 조언 중에 "수정에는 닫혀 있고, 확장에는 열려 있어야 한다"라는
 * 말이 있다. 수정에 닫혀 있어야 한다는 것은 수정한 내용이 될 수 있으면 적은 범위에 영향을 미쳐야 한다는 것이다. 
 * 즉, 수정이 다른 클래스나 함수의 수정으로 이어지지 않아야 한다. 그리고 확장에 열려 있어야 한다는 것은 기능 확장이
 * 다른 부분에 수정을 유발하지 않으면서도 새로운 기능을 쉽게 추가할 수 있어야 한다는 의미이다. 
 */

/**
 * 다중 상속 대안
 * 
 * 그렇다면 클래스가 커지고 컴파일 시간이 늘어나는 문제점을 피할 수는 없을까? 여러 가지 방법 가운데 클래스 설계에서 
 * 고려할 수 있는 방법이 있다. 다중 상속으로 코드를 재사용하는 것이 아니라 재사용할 속성과 기능을 별도의 클래스로 
 * 분리하고 이 클래스를 멤버 변수로 포함하는 것이다. 이렇게 하면 분리된 클래스는 단일 속성과 기능을 가지므로 결합도는
 * 낮아지고 변경에 따른 영향이 다른 클래스로 전이되지 않는다. 
 * 
 * 이처럼 클래스를 분리하여 포함하는 방식에는 '컴포지션'과 '어그리게이션'이라는 두 가지가 있다. 컴포지션은 분리한
 * 클래스를 포함(part-of)하는 개념이고, 어그리게이션은 사용(has-a)하는 개념이다. 
 * 
 * 
 *                 (다중 상속)                                          (컴포지션, 어그리게이션)
 * ---------------------------------------------        ----------------------              -----------------
 * |            monster_a                      |        |      monster_a      |             |    monster     |
 * |     monster                 character     |        ----------------------              -----------------
 * | ----------------         ---------------  |        | monster_attribute,  |             |     attack,    |
 * | |   attack,    |         |   hp, power  | |        | character_attribute |             | attack_special |
 * | |attack_special|         ---------------- |        |                     |             ------------------
 * | ----------------                          |        |                     |
 * |                                           |        |  quiz, monster_type |
 * |    ---------------------------------      |        |   difficult_level,  |             ------------------
 * |    | quiz, monster_type, location  |      |        |       location      |             |    character   |
 * |    |       difficult_level         |      |        -----------------------             ------------------
 * |    --------------------------------       |                                            |    hp, power   |
 * ---------------------------------------------                                            ------------------
 * 
 * 
 * 변수처럼 객체에도 생명 주기(life cycle)가 있다. 객체가 생성되어 소멸하는 과정을 의미한다. 어떤 객체는 다른 객체가 
 * 생성될 때 함께 생성되거나 다른 객체에 의해서 생성될 수 있으며 소멸도 마찬가지다. 이때 두 객체는 '생명 주기가 같다'고
 * 표현한다.
 */

/**
 * 컴포지션
 * 
 * 컴포지션(composition)은 클래스가 가져야 할 특징을 다른 클래스로부터 상속받는 것이 아니라 멤버 변수로
 * 포함하는 개념이다. 조금 더 풀어서 설명하면 재사용할 속성과 기능을 별도의 클래스로 분리하고 이 클래스의
 * 객체를 멤버 변수로 포함하는 것이다. 
 * 
 * 컴포지션을 흔히 'part-of'라고 하는데, 별도로 분리한 클래스의 객체가 이를 멤버 변수로 포함한 클래스의 
 * 일부임을 나타낸다. 즉, 멤버 변수로 포함한 클래스에 종속된다. 따라서 분리한 클래스의 객체는 이를 멤버
 * 변수로 포함한 클래스에서 생명 주기를 직접 관리하므로 논리적으로도 완전히 포함 관계이며 두 클래스의 
 * 생명 주기는 같다. 
 * 
 * monster_a 클래스에서 monster와 character 클래스의 객체를 멤버 변수로 포함하는 컴포지션의 경우, 
 * monster와 character 클래스의 객체는 monster_a에 종속되고 이에 따라 객체가 생성되고 소멸하는 생명
 * 주기도 같아진다. 이처럼 상속을 사용하지 않고 컴포지션으로 포함하는 이유는 앞서 설명한 것처럼 클래스가 
 * 커지는 것을 막고, 변경에 따른 영향을 최소화하기 위함이다. 또한 자식 클래스가 부모 클래스를 완전히
 * 대체할 수 있는 다형성 구조에도 상속보다 컴포지션이 더 유리하다. 
 * 
 * 상속과 컴포지션의 차이점
 * 상속과 컴포지션은 메모리에서 생성되고 소멸되는 관점에서는 비슷하지만, 코드가 분리돼 있다는 점이 다르다. 
 * 즉, 분리된 클래스가 변경될 때 이 클래스의 객체를 멤버 변수로 포함하는 클래스는 변경하지 않아도 되며 이에
 * 따라 컴파일을 유도하지 않는다. 다라서 늦은 바인딩(late binding)이 가능하다는 점도 눈여겨볼 점이다. 늦은
 * 바인딩은 동적 바인딩이라고도 하며 호출 대상이 호출 시점에 결정되는 것을 말한다. 
 */

/**
 * 어그리게이션
 * 
 * 어그리게이션(aggregation)도 재사용할 속성과 기능을 별도의 클래스로 분리하고 이 클래스의 객체를 멤버 변수로
 * 포함하는 것은 컴포지션과 같다. 그러나 어그리게이션은 분리된 클래스의 객체를 포인터나 레퍼런스 변수로 포함한다.
 * 따라서 분리된 클래스와 이를 포함하는 클래스의 생명 주기가 다르다. 분리된 클래스를 사용하는 개념이므로 'has-a'
 * 관계가 성립하며, 'is-a' 관계인 상속과는 차이가 있다. 
 * 
 * 어그리게이션은 컴포지션과 달리 분리된 클래스가 이를 사용하는 클래스와 유연한 관계를 가진다. 리스코프 치환
 * 원칙에 따라 분리된 클래스를 직접 참조할 수도 있고, 해당 클래스를 상속받은 자식 클래스를 참조할 수도 있다. 
 * 
 * 다음 코드에서는 monster_a와 monster_b는 각각 컴포지션과 어그리게이션을 구현했다. 기존 실습에서는 character와 
 * monster 클래스를 다중 상속받았는데, 여기서는 두 클래스의 객체를 멤버 변수로 포함했다. monster_a에서는 일반 
 * 멤버 변수로 선언해 컴포지션을, monster_b에서는 레퍼런스 변수로 참조해 어그리게이션을 구현했다. 
 */

#include <iostream>

using namespace std;


// 캐릭터의 특성을 가지고 있는 캐릭터 클래스
class character 
{
public:
    character() : hp(100), power(100) {};
    int get_hp() 
    { 
        return hp; 
    };
    int get_power() 
    { 
        return power; 
    };


protected:
    int hp;
    int power;
};


// character 클래스를 상속받은 player 클래스
class player 
{
public:
    player() {};


private:
    character main_body;
};


// Monster 클래스
class monster 
{
public:
    monster() {};
    void get_damage(int _damage) {};
    virtual void attack(player target_player) 
    {
        cout << " 공격 : 데미지 - 10 hp" << endl;
    };
};


class monster_2nd_gen : public monster 
{
public:
    virtual void attack(player target_player) override 
    {
        cout << " 새로운 공격 : 데미지 - 30 hp" << endl;
    };
};


// 몬스터 A는 monster, character 클래스를 컴포지션으로 포함
class monster_a 
{
public:
    void attack(player target_player) 
    {
        main_role.attack(target_player);
    };


private:    
    character main_body;
    monster main_role;
};


// 몬스터 B는 monster, character 클래스를 어그리게이션으로 포함
class monster_b 
{
public: 
    // 레퍼런스 멤버 변수는 초기화 리스트로 초기화 진행
    monster_b(character& ref_character, monster& ref_monster)
        : main_body(ref_character)
        , main_role(ref_monster) {};

    void attack(player target_player) 
    {
        main_role.attack(target_player);
    };


private:
    character& main_body;
    monster& main_role;
};


int main() 
{
    // 어그리게이션에 포함할 객체 생성 - 몬스터 클래스의 생명 주기 다름
    character character_obj;
    monster monster_obj;
    monster_2nd_gen monster_new_obj;

    player player_1;

    // 컴포지션을 객체와 생명주기가 같아 객체에서 직접 생성
    monster_a forest_monster;

    // 어그리게이션을 위해 외부의 객체의 참조를 전달
    monster_b tutorial_monster(character_obj, monster_obj);
    monster_b urban_monster(character_obj, monster_new_obj);
    cout << "몬스터 A 공격" << endl;
    tutorial_monster.attack(player_1);

    cout << endl << "몬스터 B 공격" << endl;
    forest_monster.attack(player_1);
    urban_monster.attack(player_1);

    return 0;
}

/**
 * 실행 결과
 * 
 * 몬스터 A 공격
 * 공격 : 데미지 - 10 hp
 * 
 * 몬스터 B 공격
 * 공격 : 데미지 - 10 hp
 * 새로운 공격 : 데미지 - 30 hp
 */

/**
 * 어그리게이션으로 구현한 monster_b 클래스의 객체인 tutorial_monster와 urban_monster를 보면, 생성자에
 * 전달한 두 번째 인자가 서로 다르다. urban_monster 객체에는 montser 클래스를 상속받은 monster_2nd_gen 
 * 클래스의 객체를 대입했다. 그 결과로 montster_b 클래스의 코드는 같지만, tutorial_monster와 urban_monster
 * 객체의 공격은 서로 다른 결과를 출력한다. 즉, monster_b를 수정하지 않고(수정에는 닫혀 있고) 새로운 공격
 * 방식을 추가했다(확장에는 열려 있다). 
 * 
 * 컴포지션과 어그리게이션은 다양한 디자인 패턴에서 사용하는 방법이다. 
 */