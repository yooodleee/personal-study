// 소멸자 정의

#include <iostream>

using namespace std;



class character {
public:
    character() {
        cout << "character 클래스 생성자" << endl;
    };

    ~character() {  // character의 소멸자 정의
        cout << "character 클래스 소멸자" << endl;
    }
};



class monster {
public:
    monster() {
        cout << "monster 클래스 생성자" << endl;
    };

    ~monster() {    // monster의 소멸자 정의
        cout << "monster 클래스 소멸자" << endl;
    }
};



class monster_a : public monster, character {
public:
    monster_a() {
        cout << "monster_a 클래스 생성자" << endl;
    };

    ~monster_a() {  // monster_a의 소멸자 정의
        cout << "monster_a 클래스 소멸자" << endl;
    }
};



int main() {
    monster_a forest_monster;
    return 0;
}