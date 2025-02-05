// 일반 변수를 매개변수로 활용하기

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

	change_negative(a);
	change_negative(b);

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