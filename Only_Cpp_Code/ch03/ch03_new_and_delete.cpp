// new, delete로 동적 메모리 할당하고 해제하기 

#include <iostream>
using namespace std;

int main() {

	int* pt_int_value = new int;	// 동적 메모리 할당하기 

	*pt_int_value = 100;
	cout << *pt_int_value << endl;

	delete pt_int_value;	// 동적 메모리 해제하기 

	return 0;
}

// 100

/**
 * 정수를 저장할 메모리 주소를 동적 할당하고 해당 메모리의 주소를 pt_int_value가 가리키도록
 * 선언한 예다. 그리고 pt_int_value가 가리키는 메모리에 100을 저장하고 출력한 후 delete 명령으로
 * 메모리를 해제했다. 
 * 
 * 이 코드는 int 형 변수 하나만 동적으로 할당했다가 해제해 본 것이다. 변수 여러 개를 배열 형태로 
 * 메모리를 할당하고 해제하는 것도 크게 다르지 않다. 다만 배열의 크기를 추가해야 한다. 
 * 
 * 자료형 *변수_이름 = new 자료형[크기];
 * delete[] 변수_이름;
 */