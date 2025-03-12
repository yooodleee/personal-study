// 시프트 연산하기기

#include <iostream>
#include <bitset>

using namespace std;

int main() {

	int a = 13;
	int b = a >> 1;	// 1bit 오른쪽으로 시프트
	int c = a << 1;	// 1bit 왼쪽으로 시프트
	int d = a >> -1;	// 시프트 수행 오류(warning C4293)
	int e = a << 32;	// 시프트 수행 오류(warning C4293)

	cout << "a = " << bitset<8>(a) << " : " << a << endl;
	cout << "b = " << bitset<8>(b) << " : " << b << endl;
	cout << "c = " << bitset<8>(c) << " : " << c << endl;
	cout << "d = " << bitset<8>(d) << " : " << d << endl;
	cout << "e = " << bitset<8>(e) << " : " << e << endl;

	return 0;
}

/*
a = 00001101 : 13
b = 00000110 : 6
c = 00011010 : 26
d = 00000000 : 0
e = 00001101 : 13
*/

/**
 * 경고 메시지
 * 
 * warning c4293: '>>': 시프트 횟수가 음수이거나 너무 큽니다. 정의되지 않은 동작입니다. 
 * warning c4293: '<<': 시프트 횟수가 음수이거나 너무 큽니다. 정의되지 않은 동작입니다. 
 */