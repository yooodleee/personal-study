// 배열 원소의 메모리 주소 확인하기기

#include <iostream>
using namespace std;

int main() {

	int lotto[45] = {
		1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
		16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
		31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45
	};

	cout << "lotto[0] Address: " << &lotto[0] << endl;
	cout << "lotto[1] Address: " << &lotto[1] << endl;
	cout << "lotto[2] Address: " << &lotto[2] << endl;
	cout << "lotto[3] Address: " << &lotto[3] << endl;
	cout << "lotto[4] Address: " << &lotto[4] << endl;
	cout << "lotto[5] Address: " << &lotto[5] << endl;

	return 0;
}

/*
실행 결과

lotto[0] Address: 00000095922FF590
lotto[1] Address: 00000095922FF594
lotto[2] Address: 00000095922FF598
lotto[3] Address: 00000095922FF59C
lotto[4] Address: 00000095922FF5A0
lotto[5] Address: 00000095922FF5A4

주소는 프로그램을 실행할 때마다 다르게 할당되므로 출력되는 값이 다를 수 있다. 
*/