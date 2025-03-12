// 비트 AND 연산(&)

/**
 * 이항 연산자 표현식(binary operator expression)
 * 
 * 피연산자 연산자 피연산자 처럼 연산에 참여하는 피연산자가 2개인 표현식이다. 
 * 대부분의 산술 연산자와 관계 연산자가 여기에 속한다. 
 * 
 * * 산술 연산자
 * 		- 대입: a = 10
 * 		- 더하기: a + b
 * 		- 빼기: a - b
 * 		- 곱하기: a * b
 * 		- 나누기: a / b
 * 		- 나머지: a % b
 * 
 * 	* 관계 연산자
 * 		- 같음(true/false): a == b
 * 		- 같지 않음(true/false): a != b
 * 		- 초과(true/false): a > b
 * 		- 이상(true/false): a >= b
 * 		- 미만(true/false): a < b
 * 		- 이하(true/false): a <= b
 * 
 * * 논리 연산자
 * 		- 논리 AND(true/false): 둘 디 true일 때만 true => a && b
 * 		- 논리 OR(true/false): 둘 중 하나만 true여도 true => a || b
 * 
 * * 비트 연산자
 * 		- AND: a & b
 * 		- OR: a | b
 * 		- XOR: a ^ b
 * 		- 오른쪽 시프트(shift): a >> b
 * 		- 왼쪽 시프트(shift): a << b
 */

#include <iostream>
#include <bitset>

using namespace std;

int main() {

	int a = 13;
	int b = 27;
	int c = a & b;	// 비트 AND 연산(둘 다 true여야 true 반환, 둘 다 1이어야 1 반환)

	cout << "a = " << bitset<8>(a) << " : " << a << endl;
	cout << "b = " << bitset<8>(b) << " : " << b << endl;
	cout << "c = " << bitset<8>(c) << " : " << c << endl;

	return 0;
}

/*
a = 00001101 : 13
b = 00011011 : 27
c = 00001001 : 9
*/