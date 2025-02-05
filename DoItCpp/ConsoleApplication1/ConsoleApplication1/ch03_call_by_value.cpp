// 매개변수를 일반 변수로 선언

#include <iostream>
using namespace std;


void swap(int a, int b)
{
	// swap 함수 내 교환 전 a, b 값
	cout << "[swap func] before swap, a: " << a << " b: " << b << endl;

	int temp = a;
	a = b;
	b = temp;

	// swap 함수 내 교환 후 a, b 값
	cout << "[swap func] after swap, a: " << a << " b: " << b << endl;
}


int main()
{
	int a = 15, b = 10;

	// swap 함수 호출 전 a, b 값
	cout << "[main] before swap, a: " << a << " b: " << b << endl << endl;

	swap(a, b);

	// swap 함수 호출 후 a, b 값
	cout << "[main] after swap, a: " << a << " b: " << b << endl;

	return 0;
}

/*
[main] before swap, a: 15 b: 10

[swap func] before swap, a: 15 b: 10
[swap func] after swap, a: 10 b: 15
[main] after swap, a: 15 b: 10
*/