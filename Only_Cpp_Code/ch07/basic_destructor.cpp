// 소멸자 정의

/**
 * 소멸자
 * 
 * 소멸자(destructor)는 생성자와 반대 역할을 한다. 생성자에서 객체가 생성될 때 필요한 여러 가지 일을
 * 진행했다면, 소멸자에서는 객체가 소멸할 때 필요한 메모리 해제나 외부 환경을 객체 생성 이전 상태로
 * 변경하는 등의 일을 진행한다. 
 * 
 * 기본 소멸자
 * 
 * 소멸자를 선언하는 방법은 간단하다. 이름은 클래스 이름과 같게 작성하고 이름 앞에 ~ 를 추가한다. 다른
 * 함수와는 다르게 반환 형식이나 매개변수는 없다. 
 * 소멸자 선언 
 * => ~클래스_이름()
 * 
 * 소멸자는 객체가 소멸되는 시점에 자동으로 호출되낟. 소멸자는 생성자보다 간단하다. 주로 메모리나 정적 
 * 변숫값을 생성 전으로 되돌리는 작업이 많아서 매개변수가 필요하지 않다. 그리고 다중 상속일 때 생성자
 * 호출의 역순으로 소멸자가 호출된다. 
 */

#include <iostream>

using namespace std;



class character {
public:
    character() 
    {
        cout << "character 클래스 생성자" << endl;
    };

    ~character() {  // character의 소멸자 정의
        cout << "character 클래스 소멸자" << endl;
    }
};



class monster 
{
public:
    monster() 
    {
        cout << "monster 클래스 생성자" << endl;
    };

    ~monster() 
    {    // monster의 소멸자 정의
        cout << "monster 클래스 소멸자" << endl;
    }
};



class monster_a : public monster, character 
{
public:
    monster_a() 
    {
        cout << "monster_a 클래스 생성자" << endl;
    };

    ~monster_a() 
    {  // monster_a의 소멸자 정의
        cout << "monster_a 클래스 소멸자" << endl;
    }
};



int main() 
{
    monster_a forest_monster;
    return 0;
}

/**
 * 실행 결과
 * 
 * monster 클래스 생성자
 * character 클래스 생성자
 * monster_a 클래스 생성자
 * monster_a 클래스 생성자
 * character 클래스 생성자
 * monster 클래스 생성자
 */