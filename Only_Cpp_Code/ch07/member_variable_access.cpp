// public 멤버 변수 접근

#include <iostream>
#include <array>

using namespace std;


class manage_data_structor {
public:
    manage_data_structor();
    int current_index;
    array<int, 10> data_queue;
};

manage_data_structor::manage_data_structor() :
    current_index(0), data_queue{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} {
}


int main(void) {
    int data;
    manage_data_structor data_structor;

    data_structor.current_index = -1;
    data = data_structor.data_queue[data_structor.current_index];

    cout << "Data [" << data_structor.current_index << "] : " << data << endl;

    return 0; 
}