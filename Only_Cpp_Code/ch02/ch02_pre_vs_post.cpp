// 증가 연산자, 전위/후위 연산 비교하기

#include <iostream>
using namespace std;

int main() {
	
	int a = 0;	// a 최초 값 0
	int b = 0;	// b 최초 값 0
	int a_prefix;
	int b_postfix;

	a_prefix = ++a;	// 전위 연산(a값을 1만큼 증가시킨 후에 a_prefix에 대입)
	b_postfix = b++;	// 후위 연산(b값을 b_postfix에 대입한 후에 b값을 1만큼 증가)

	cout << "a = " << a << ", " << "a_prefix = " << a_prefix << endl;
	cout << "b = " << b << ", " << "b_postfix = " << b_postfix << endl;

	return 0;
}

/*
a = 1, a_prefix = 1
b = 1, b_postfix = 0
*/