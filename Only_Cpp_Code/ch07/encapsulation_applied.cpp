// private 멤버 변수 접근

#include <iostream>
#include <array>

using namespace std;


class manage_data_structor {
public:
    manage_data_structor();
    int get_current_index() { return current_index; };
    void set_current_index(int new_index);
    int get_array_value() { return data_queue[current_index]; };


private:
    int current_index;
    array<int, 10> data_queue;
};


manage_data_structor::manage_data_structor() :
    current_index(0), data_queue{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 } {}


void manage_data_structor::set_current_index(int new_index) {
    if (new_index < 0 || new_index >= 10)
        return;

    current_index = new_index;
}


int main(void) {
    int data, index;
    manage_data_structor data_structor;

    data_structor.set_current_index(-1);
    index = data_structor.get_current_index();
    data = data_structor.get_array_value();
    cout << "Data [" << index << "] : " << data << endl;

    return 0;
}