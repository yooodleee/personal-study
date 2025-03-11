
#include <iostream>
#include <list>
#include <random>
#include <cmath>

using namespace std;

const int forest_terrain_type = 0;
const int cyber_terrain_type = 1;
const int urban_terrain_type = 2;

const int monster_a_type = 0;
const int monster_b_type = 1;
const int monster_c_type = 2;

random_device rd;
mt19937 get(rd());
uniform_int_distribution<int> dis(0, 99);
uniform_int_distribution<int> select(0, 2);


class character {
public:
    character() : hp(100), power(100) {};
    int get_hp() { return hp; }
    int get_power() { return power; }

protected:
    int hp;
    int power;
};


// 인터페이스로 사용할 추상 클래스 IRoute
class IRoute {
public:
    virtual void find_route(int x, int y) = 0;
    virtual void set_location(int x, int y) = 0;
    virtual void get_location(bool x) = 0;
};


// 인터페이스로 사용할 추상 클래스 IAttack
class IAttack {
public:
    virtual bool attach_target(character* target_player) = 0;
    virtual void check_target(character& target_player) = 0;
    virtual void attack_special(character& target_player) = 0;
};


// character 클래스와 추상 클래스 IRoute를 상속 받은 player 클래스
class player : public character, public IRoute {
public:
    player() {};
    virtual void find_route(int x, int y) override;
    virtual void set_location(int x, int y) override;
    virtual int get_location(bool x) override;

private:
    int location_x;
    int location_y;
};

void player::find_route(int x, int y) {
}

void player::set_location(int x, int y) {
    location_x = x;
    location_y = y;
}

int player::get_location(bool x) {
    if (x) {
        return location_x;
    }

    return location_y;
}


// IRoute, IAttack 두 추상 클래스를 상속 받아 정의한 몬스터 클래스
class monster : public IRoute, public IAttack {
public:
    int get_monster_type() {
        return monster_type;
    }
    virtual void set_location(int x, int y) override {
        location_x = x;
        location_y = y;
    };
    virtual int get_location(bool x) override {
        return x ? location_x : location_y;
    };

protected:
    int calculate_distance(int x, int y);
    character* target_player = nullptr;
    int monster_type;
    character monster_body;

private:
    int location_x;
    int location_y;
};

int monster::calculate_distance(int x, int y) {
    return (int)sqrt(pow(x - get_location(true), 2) + pow(y - get_location(false), 2));
}


class terrain {
public:
    virtual void allocate_monster(monster* mon) = 0;
    virtual void bost_monster(monster* mon) = 0;
    void set_start_location(int x, int y) {
        start_location_x = x;
        start_location_y = y;
    };
    void set_end_location(int x, int y) {
        end_location_x = x;
        end_location_y = y;
    };

protected:
    int terrain_type;
    void update_monster_list(monster* mon);

private:
    int start_location_x;
    int start_location_y;
    int end_location_x;
    int end_location_y;
};


void terrain::update_monster_list(monster* mon) {
    mon_list.push_back(mon);
}


class forest_terrain : public terrain {
public:
    forest_terrain() {
        terrain_type = forest_terrain_type;
    };
    virtual void allocate_monster(monster* mon) override;
    virtual void bost_monster(monster* mon) override;
};

void forest_terrain::allocate_monster(monster* mon) {
    if (monster_a_type == mon->get_monster_type()) {
        update_monster_list(mon);
        cout << "Monster A를 숲에 배치 합니다." << endl;
    }
}

void forest_terrain::bost_monster(monster* mon) {
    if (monster_a_type == mon->get_monster_type())
    {
        cout << "몬스터 A가 숲에서는 힘이 더 강해집니다." << endl;
    }
}

class cyber_terrain : public terrain {
public:
    cyber_terrain()
    {
        terrain_type = cyber_terrain_type;
    };
    virtual void allocate_monster(monster* mon) override;
    virtual void bost_monster(monster* mon) override;
};

void cyber_terrain::allocate_monster(monster* mon)
{
    update_monster_list(mon);
    cout << "모든 종류의 Monster를 사이버 공간에 배치 합니다." << endl;
}

void cyber_terrain::bost_monster(monster* mon)
{
    cout << "모든 몬스터가 사이버 공간에서는 속도가 빨라 집니다." << endl;
}

class urban_terrain : public terrain {
public:
    urban_terrain()
    {
        terrain_type = urban_terrain_type;
    };
    virtual void allocate_monster(monster* mon) override;
    virtual void bost_monster(monster* mon) override;
};

void urban_terrain::allocate_monster(monster* mon)
{
    if (monster_a_type != mon->get_monster_type())
    {
        update_monster_list(mon);
        cout << "Monster B, C를 도심에 배치 합니다." << endl;
    }
}

void urban_terrain::bost_monster(monster* mon)
{
    if (monster_c_type == mon->get_monster_type())
    {
        update_monster_list(mon);
        cout << "Monster C는 도심에 힘이 강해 집니다." << endl;
    }
}

