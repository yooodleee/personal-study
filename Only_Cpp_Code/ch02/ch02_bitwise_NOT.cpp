// bit 연산자로 1의 보수 구하기

/**
 * 비트 연산자(~)는 비트열을 반전하라는 뜻으로 각 자릿수의 비트값을 반대로 바꿔 1의 보수로 변환한다. 
 * 다음을 실행해보면, 16진수로 표현한 0이 모두 f로 반전되는 것을 확인할 수 있다. 
 * 만약, 0과 1로 이뤄진 2진수를 1의 보수로 반전하면, 0 -> 1, 1 -> 0으로 0000 0101 -> 1111 1010이 된다. 
 */

#include <iostream>
using namespace std;

int main() {

	unsigned int value = 0x00000000;	// 0을 16 진수(hex)로 표현한 값

	value = ~value;
	cout << hex << value << endl;

	return 0;
}

// ffffffff