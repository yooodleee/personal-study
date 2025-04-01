// 캐릭터 이동 오버로딩

/**
 * 함수와 연산자 오버로딩
 * 
 * 부모 클래스의 함수를 오버라이딩(overridining)한다는 것은 부모의 정의를 무시하거나 그에 앞서 
 * 자식 클래스에 정의된 함수를 우선시하겠다는 의미이다. 
 * 
 * 반면에 오버로딩(overloading)은 과부하 또는 과적이란 뜻이다. 점을 계속해서 쌓는다는 의밍이다. 
 * 이미 정의된 함수와 같은 이름을 사용하지만 매개변수 구성을 변경해 가면서 새로운 정의를 계속
 * 쌓는 의미로 이해할 수 있다. 
 * 
 * 만약 함수의 이름을 바꾸면 새로운 함수가 되며, 이름과 매개변수 구성은 그대로인데 반환 형식만 
 * 바꾼 함수는 오버로딩되지 않고 오류가 발행하므로 주의한다. 
 * 
 * 
 * 예컨대 몬스터에 이동 기능을 구현한다고 생각해 보자. 함수 이름과 매개 변수는 평범하게 
 * void move(int x, int y)로 설정했다. 개발하다 보니 특정 위치를 거쳐서 가야하는 요구사항이
 * 생겨 새로운 함수를 void move_follow_path(int x[], int y[], int spot_count)처럼 만들었다. 
 * 그런데 이런 식으로 함수가 늘면 이름도 복잡해지고 코드를 이해하기가 어려워질 수 있다. 
 * 
 * 이때는 void move(int x[], int y[], int spot_count)처럼 이름은 같지만 매개변수 구성이 다른
 * 함수를 정의할 수 있다. 이를 오버로딩이라고 한다. 오버로딩 함수도 많아지면 이해가 어려울 수 
 * 있지만, 함수 이름이 같고 매개변수 구성만 다르니 이동에 관련된 다른 옵션이 존재한다고 이해할
 * 수 있다. 또한 함수 오버로딩은 본문이나 호출하는 코드를 수정하지 않고 기능을 바꿔야 할 때 
 * 사용하기도 한다. 
 * 
 * 이동은 모든 캐릭터에 필요한 기능이니 character 클래스에 오버로딩 함수를 정의하고 호출해 본다. 
 */

#include <iostream>

using namespace std;



class character 
{
public:
    character() : location{ 0,0 } {};
    
    // x, y 좌표를 매개변수로 같은 함수
    void move(int x, int y) 
    {
        location[0] = x;
        location[1] = y;
        cout << location[0] << ", " << location[1] << "로 이동" << endl;
    };

    // x, y 배열과 배열 크기를 매개변수로 가지는 함수
    void move(int x[], int y[], int spot_count) 
    {
        for (int i = 0; i < spot_count; ++i) 
        {
            location[0] = x[i];
            location[1] = y[i];
            cout << i + 1 << "번째: " << location[0] << ", " << location[1] << "로 이동" << endl;
        }
    }

protected:
    int location[2];
};


int main(void) 
{
    character character_obj;
    int x_list[3] = { 10, 15, 20 };
    int y_list[3] = { 10, 15, 20 };

    // x, y 좌표를 매개변수로 가지는 함수 호출
    character_obj.move(10, 10);
    cout << endl;

    // x, y 배열과 배열 크기를 매개변수로 가지는 함수 호출
    character_obj.move(x_list, y_list, 3);
}


/**
 * 실행 결과
 * 
 * 10, 10로 이동
 * 
 * 1번째: 10, 10로 이동
 * 2번째: 15, 15로 이동
 * 3번째: 20, 20로 이동
 */