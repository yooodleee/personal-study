// 리스코프 치환 원칙 적용

/**
 * 소멸자
 * 
 * 클래스 상속을 알아볼 때 잠깐 언급했던 리스코프 치환 원칙에 따르면, 자식 클래스는 언제든지
 * 부모 클래스를 대신할 수 있어야 한다. 몬스터 A 클래스를 조금 수정해서 리스코프 치환 원칙을
 * 적용해본다. 
 */

#include <iostream>

using namespace std;



class monster 
{
public:
    monster() 
    {
        cout << "monster 클래스 생성자" << endl;
    };

    ~monster() 
    {
        cout << "monster 클래스 소멸자" << endl;
    };
};



class monster_a : public monster 
{
public:
    monster_a() 
    {
        cout << "monster_a 클래스 생성자" << endl;
    };

    ~monster_a() 
    {      // 이 소멸자가 호출되지 않음.
        cout << "monster_a 클래스 소멸자" << endl;
    };
};



int main() 
{
    monster *forest_monster = new monster_a();
    delete forest_monster;      // 메모리 해제
    return 0;
}


/**
 * 실행 결과
 * 
 * monster 클래스 생성자
 * monster_a 클래스 생성자
 * monster 클래스 소멸자
 */

/**
 * 부모인 monster 클래스의 포인터에 자식인 monster_a 객체를 생성해서 대입했다. 리스코프 치환 원칙에
 * 따라 프로그램은 정상으로 실행된다. 그런데 출력 결과를 보면 monster_a 클래스의 소멸자가 호출되지 
 * 않았다. 
 * 
 * 코드에서 자식 클래스가 부모 클래스를 대신하더라도 여전히 부모 클래스가 사용되므로 delete 메모리를
 * 해제하면 부모 클래스의 소멸자가 호출된다. 그리고 객체가 이미 소멸했으므로 자식 클래스의 소멸자는
 * 호출되지 않았다. 
 */