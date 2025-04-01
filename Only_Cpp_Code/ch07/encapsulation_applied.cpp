// private 멤버 변수 접근

/**
 * 객체 지향 원칙에 맞게 앞선 에시 코드를 수정해 보겠다. 배열과 배열의 인덱스를 private
 * 변수로 선언하고 이에 접근해 값을 설정하거나 가져오는 함수를 추가한다. 그리고 set_current_index
 * 함수에서는 배열의 현재 인덱스를 설정할 때 범위를 벗어났으면 정상 범위로 조정하여 문제가 발생하지
 * 않도록 한다. 
 */

#include <iostream>
#include <array>

using namespace std;


class manage_data_structor 
{
public:
    manage_data_structor();
    int get_current_index() 
    { 
        return current_index; 
    };
    void set_current_index
    (
        int new_index
    );
    int get_array_value() 
    { 
        return data_queue[current_index]; 
    };


private:
    int current_index;
    array<int, 10> data_queue;
};


manage_data_structor::manage_data_structor() :
    current_index(0), data_queue{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 } {}


void manage_data_structor::set_current_index(int new_index) 
{
    if (new_index < 0 || new_index >= 10)
        return;

    current_index = new_index;
}


int main(void) 
{
    int data, index;
    manage_data_structor data_structor;

    data_structor.set_current_index(-1);
    index = data_structor.get_current_index();
    data = data_structor.get_array_value();
    cout << "Data [" << index << "] : " << data << endl;

    return 0;
}

/**
 * 실행 결과
 * Data[0]: 0
 */

/**
 * 이처럼 클래스의 멤버 변수는 특별한 이유가 없다면 public으로 지정하지 말고 private이나 
 * protected으로 지정한 후 멤버 함수를 통해서 값을 설정하거나 얻어야 한다. 
 */