// 증가 연산자, 전위/후위 연산 비교하기

/**
 * ++: 1만큼 증가
 * --: 1만큼 감소소
 */

#include <iostream>
using namespace std;

int main() {
	
	int a = 0;	// a 최초 값 = 0
	int b = 0;	// b 최초 값 = 0
	int a_prefix;
	int b_postfix;
 
	a_prefix = ++a;		// a 값을 1만큼 증가시킨 후에 a_prefix에 대입 (전위 증가 연산자)
	b_postfix = b++;	// b 값을 b_postfix에 대입한 후에 b 값을 1만큼 증가 (후위 증가 연산자)

	cout << "a = " << a << ", " << "a_prefix = " << a_prefix << endl;
	cout << "b = " << b << ", " << "b_postfix = " << b_postfix << endl;

	return 0;
}

/*
execution result

a = 1, a_prefix = 1
b = 1, b_postfix = 0
*/


/**
 * 같은 증가 연산인데도 전위이냐 후위이냐에 따라 다르게 나온다. 
 * 먼저 a 변수 앞에 붙은 전위 연산자는 a 변수가 다른 연산에 이용되기 전에 수행된다. 
 * 따라서 a 값은 처음 0에서 1이 된다. 이후 a_prefix 변수에 a 값 1 이 대입된다. 
 * 결국 a와 a_prefix의 값은 똑같이 1이 출력된다. 
 * 
 * 		a_prefix = ++a
 * 		i) a 1 증가
 * 		ii) a_prefix에 대입
 */

/**
 * 후위 연산자는 연산 순서가 다르다. 전위 연산자와 반대로 b_postfix 변수에 b 값인 0을 대입하는 연산이
 * 먼저 수행된다. 이후에 b가 증가해 1이 된다. 결국 b_postfix와 b는 서로 다른 값이 출력된다. 
 * 
 * 요약하면, 전위 연산자를 사용하면 표현식의 나머지 부분이 평가되기 전에 변수값이 증가한다. 
 * 하지만, 후위 연산자를 사용하면 표현식의 나머지 부분이 평가된 후에 변수값이 증가한다. 
 * 즉, 연산자의 위치에 따라 연산 순서가 달라진다. 
 */