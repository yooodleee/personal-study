// 단일 상속

#include <iostream>

using namespace std;


class character {
public:
    character() : hp(100), power(100) {};


protected:
    int hp;
    int power;

};


// 단일 상속
class player : public character {   // 클래스를 상속받을 때 부모 클래스(character)를 하나만 지정하는 경우
public:
    player() {};

};