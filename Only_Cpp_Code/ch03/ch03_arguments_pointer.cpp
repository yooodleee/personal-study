// 포인터 변수를 매개변수로 사용하기 

/**
 * 포인터를 매개변수로 사용하기 
 * 
 * arguments_value에서의 문제를 해결할 수 있는 방법 중 하나는 포인터 변수를 매개변수로 활용하는 것이다. 
 */

#include <iostream>
using namespace std;

void change_negative(int* _val)	// 포인터 변수를 매개변수로 사용 
{
	if (*_val > 0)
	{
		*_val = -(*_val);	// _val이 가리키는 값이 양수이면 음수로 변경 
	}
}

int main() {

	int a = 3, b = -3;

	cout << "a : " << a << endl;
	cout << "b : " << b << endl;

	change_negative(&a);	// a 변수의 주소값을 전달 
	change_negative(&b);	// b 변수의 주소값을 전달 

	cout << "change_negative(a) : " << a << endl;
	cout << "change_negative(b) : " << b << endl;

	return 0;
}

/*
a : 3
b : -3
change_negative(a) : -3
change_negative(b) : -3
*/

/**
 * 먼저 main에서 바뀐 부분은 change_negative(&a)와 change_negative(&b)이다. 
 * 두 코드에서 인자로 넘기는 a, b 변수 앞에 주소 연산자 &가 붙었다. 변수 이름 앞에 
 * 주소 연산자 &를 붙이면 해당 변수의 주소를 불러온다. 즉, a, b 변수에 저장된 3, -3이라는 
 * 값 대신에 a, b 변수의 주소를 전달한다. 
 * 
 * 이어서 change_negative 함수에서는 매개변수가 포인터 변수로 변경되었다. 포인터 변수는 
 * '메모리 주소를 저장하는 변수'이다. 즉, 함수가 호출될 때 주솟값을 전달했으므로 이를
 * 받으려면 포인터 변수로 선언해야 한다. 이제 change_negative 함수 내부에서는 포인터 변수
 * _val 앞에 역참조 연산자 *를 사용해 포인터 변수가 가리키는 데이터에 직접 접근할 수 있다. 
 * 따라서 실행 결과를 보면 main의 a, b 변수에 저장된 값이 모두 음수로 변경된 것을 확인할 수 있다. 
 */