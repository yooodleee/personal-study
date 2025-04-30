// 가상 소멸자

#include <iostream>

using namespace std;



class monster 
{
public:
    monster();
    // ~monster();
    virtual ~monster(); // 가상 소멸자 사용 

private:
    int* dummy;
};

monster::monster() 
{
    cout << "monster() 생성자 호출" << endl;
    dummy = new int;
}

monster::~monster() {
    cout << "~monster() 소멸자 호출" << endl;
    delete dummy;
}


class monster_a : public monster 
{
public:
    monster_a();
    // ~monster_a();
    virtual ~monster_a();

private:
    int* dummy_a;
};

monster_a::monster_a() 
{
    cout << "monster_a() 생성자 호출" << endl;
    dummy_a = new int;
}

monster_a::~monster_a() 
{
    cout << "~monster_a() 소멸자 호출" << endl;
    delete dummy_a;
}


int main() 
{
    monster* mon = new monster_a();     // 부모 클래스로 업캐스팅
    delete mon;
    
    return 0;
}