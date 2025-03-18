// 매개변수를 레퍼런스 변수로 선언

#include <iostream>
using namespace std;

void swap(int &ref_a, int &ref_b)   // 매개변수를 레퍼런스 변수로 선언
{
    // 교환 전 a, b 값
    cout << "[swap func] before swap, ref_a: " << ref_a << " ref_b: " << ref_b << endl;

    int temp = ref_a;
    ref_a = ref_b;
    ref_b = temp;

    // 교환 후 a, b 값
    cout << "[swap func] after swap, ref_a: " << ref_a << " ref_b: " << ref_b << endl;
}

int main()
{
    int a = 5;
    int b = 10;

    // swap 함수 호출 전 a, b 값
    cout << "[main] before swap, a: " << a << " b: " << b << endl;

    swap(a, b);

    // swap 함수 호출 후 a, b 값
    cout << "[main] after swap, a: " << a << " b: " << b << endl;

    return 0;
}

/**
 * 실행 결과
 * 
 * [main] before swap, a: 5, b: 10
 * 
 * [swap func] before swap, ref_a: 5 ref_b: 10
 * [swap func] after swap, ref_a: 10 ref_b: 5
 * 
 * [main] after swap, a: 10 b: 5
 */

/**
 * swap 함수의 매개변수를 int &ref_a, int ref_b로 선언했으므로 main에서 swap(a, b) 함수를 호출하면
 * swap 함수에서는 레퍼런스 변수가 선언된다. main에서 넘긴 a, b 변수에 각각 별칭(또 다른 이름)이 부여된다고
 * 이해하면 된다. 즉, 실제 변수는 하나지만 이름이 2개가 되는 것이다. 
 * 
 * int &ref_a = a;      // 변수 a의 또 다른 이름 ref_a
 * int &ref_b = b;      // 변수 b의 또 다른 이름 ref_b
 * 
 * 그리고 swap 함수 내부에서 ref_a, ref_b의 값을 교환하면 어떻게 될까? swap 함수의 ref_a, ref_b는 실제로는 main 함수의 
 * a, b 변수와 같으므로 의도했던 대로 값이 교환된다. 이러한 호출 방식을 '참조에 의한 호출(call by reference)'이라고 한다. 
 * 참조에 의한 호출에서는 매개변수가 참조자가 되므로 피호출자(예에서는 main)의 변수를 그대로 이용한다. 
 */