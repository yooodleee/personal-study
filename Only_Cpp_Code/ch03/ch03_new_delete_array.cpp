// new, delete로 동적 메모리 할당하고 해제하기 

/**
 * 동적 메모리 할당
 * 
 * 이번에는 new와 delete를 사용한 동적 메모리 할당을 알아보겠다.
 * 
 * 배열을 사용할 때도 이미 정해진 크기만큼의 고정 배열을 선언하고 사용했다. 
 * 
 * char char_array[10];
 * int int_array[500];
 * float float_array[1000];
 * 
 * 배열의 크기가 고정되다 보니 더 많은 요소가 필요할 때는 처리할 수 없고, 반대로 너무 큰 배열을 선언하면
 * 그만큼 메모리가 낭비되거나 프로그램이 강제로 종료될 수 있다. 메모리 낭비는 최소화하면서 배열의 크기를 
 * 지정할 수는 없다. 
 */

/**
 * 동적 메모리 할당과 해제하기
 * 
 * 이럴 때 동적 메모리 할당을 사용한다. 동적 메모리 할당(dynamic memory allocation)은 프로그램 실행 중에도
 * 필요한 크기의 메모리를 운영체제에 요청하여 사용할 수 있는 방법이다. 
 * 
 * C++ 언어에서 동적 메모리를 할당하려면 new 키워드를 사용한다. 
 * 
 * => 자료형 *변수_이름 = new 자료형;
 * 
 * new로 할당된 메모리는 필요 없는 시점에 delete 키워드로 반드시 직접 해제해야 한다. 
 * 
 * => delete 변수_이름;
 */

#include <iostream>
using namespace std;

int main() {

	int* pt_int_array_value = new int[5];	// 동적 메모리 할당(배열)

	for (int i = 0; i < 5; i++)
	{
		pt_int_array_value[i] = i;	// 할당된 배열 변수에 0 ~ 4까지 순서대로 넣기 
	}

	for (int i = 0; i < 5; i++)
	{
		cout << pt_int_array_value[i] << endl;	// 배열 변수 출력 
	}

	delete[] pt_int_array_value;	// 동적 메모리 해제(배열)

	return 0;
}