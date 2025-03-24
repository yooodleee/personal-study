// 반복문에서 break 활용

/**
 * 반복문에서 break 문 사용
 * 
 * switch 문을 빠져나올 때 break 키워드를 사용했다. 그런데 break 키워드는 반복문에서 빠져나오는
 * 용도로도 사용한다. break 문을 만나면 반복문을 빠져나와 다음에 오는 코드를 실행한다. 
 */

#include <iostream>
using namespace std;

int main()
{
    for (int count = 0; count < 10; count++)
    {
        cout << "count: " << count << endl;
        if (count == 5)
        {
            cout << "break로 반복문 탈출" << endl;
            break;
        }
    }
    cout << "반복문 종료" << endl;
    return 0;
}

/**
 * 실행 결과
 * 
 * count: 0
 * count: 1
 * count: 2
 * count: 3
 * count: 4
 * count: 5
 * break로 반복문 탈출
 * 반복문 종료 
 */

/**
 * 예에서 for 문은 반복할 때마다 현재 count의 값을 출력한다. for 문 내부의 if 문은 count가 5인지 확인하고,
 * 참이면 반복 중단에 대한 메시지를 출력한 다음 break 키워드로 반복문을 빠져나온다. 그리고 나서 for 문 바로
 * 다음에 있는 "Loop ended" 문장을 출력하고 프로그램은 종료한다. 
 * 
 * break 키워드는 while이나 do ~ while 문에서도 같은 방식으로 사용할 수 있으니 적절하게 사용해 본다. 
 */

/**
 * C++ 언어에서 반복문을 만들 때 주의할 점
 * 
 * 반복문을 작성할 때는 종료 조건에 신경써야 한다. 그렇지 않으면 무한 반복되어 프로그램이 충돌할 수 있다. 
 * 반복이 실행되는 횟수를 제어하는 변수가 제대로 초기화되었는지, 반복할 때마다 올바르게 업데이트되는지 
 * 살펴봐야 한다. 또한 반복문 내부에서 실행되는 코드도 신경 써야 한다. 반복이 의도한 대로 실행되고 있는지
 * 살펴봐야 하고, 실수로 외부의 변수를 수정하지 않도록 확인해야 한다. 
 */