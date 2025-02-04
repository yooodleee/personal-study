// 비트 연산자로 1의 보수 구하기

#include <iostream>
using namespace std;

int main() {

	unsigned int value = 0x00000000;	// 0을 16진수(hex)로 표현한 값

	value = ~value;
	cout << hex << value << endl;

	return 0;
}

// ffffffff