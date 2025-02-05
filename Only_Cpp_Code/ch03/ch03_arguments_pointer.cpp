// 포인터 변수를 매개변수로 사용하기

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

	change_negative(&a);	// a 변수의 주솟값을 전달
	change_negative(&b);	// b 변수의 주솟값을 전달

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