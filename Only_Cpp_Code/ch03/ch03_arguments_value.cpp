// 일반 변수를 매개변수로 활용하기 

/**
 * 함수의 매개변수 사용하기 
 * 
 * 함수의 매개변수(arguments)는 일반 변수뿐만 아니라 포인터와 배열도 활용할 수 있다. 
 * 먼저 매개변수를 일반 변수로 정의한 예를 살펴보도록 하자. 
 */

#include <iostream>
using namespace std;

void change_negative(int _val)
{
	if (_val > 0)
	{
		_val = -_val;
	}
}

int main() {

	int a = 3, b = -3;

	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	change_negative(a);		// a -> _val
	change_negative(b);		// b -> _val

	cout << "change_negative(a): " << a << endl;
	cout << "change_negative(b): " << b << endl;

	return 0;
}

/*

a = 3
b = -3
change_negative(a): 3
change_negative(b): -3

*/

/**
 * change_negative는 매개변수로 받은 _val이 양수이면 음수로 바꾸도록 만든 함수이다. 
 * 기대했던 결과는 a의 값 3이 -3으로 변경되는 것인데, 출력된 결과를 보면 원래 값 3이
 * 그대로 출력되었다. 그 이유는 매개변수인 _val이 change_negative 함수 내부에서만 
 * 효력이 있는 지역 변수이기 때문이다. 
 * 
 * main에서 change_negative 함수를 호출할 때 넣었던 a, b 변수는 _val 매개변수로 복사된다. 
 * 따라서 change_negative 함수에서는 _val 변수값만 음수로 만들 뿐, main의 a, b 변수에는
 * 아무런 영향이 없다. 
 */