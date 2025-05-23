// 생성자와 소멸자 호출 순서

#include <iostream>

using namespace std;


class monster {
public:
    monster();      // 생성자
    ~monster();     // 소멸자


private:
    int *dummy;
};

monster::monster() {
    cout << "monster() 생성자 호출" << endl;
    dummy = new int;
}

monster::~monster() {
    cout << "~monster() 소멸자 호출" << endl;
    delete dummy;   // 메모리 해제
}



class monster_a : public monster {
public:
    monster_a();
    ~monster_a();

private:
    int* dummy_a;
};

monster_a::monster_a() {
    cout << "monster_a() 생성자 호출" << endl;
    dummy_a = new int;
}

monster_a::~monster_a() {
    cout << "~monster_a() 소멸자 호출" << endl;
    delete dummy_a;
}


int main() {
    monster_a* mon = new monster_a();

    delete mon;
    return 0;
}

/**
 * monster() 생성자 호출
 * monster_a() 생성자 호출
 * ~monster_a() 소멸자 호출
 * ~monster() 소멸자 호출 
 */