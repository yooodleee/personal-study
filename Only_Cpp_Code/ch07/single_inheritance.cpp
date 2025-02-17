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
class player : public character {
public:
    player() {};

};