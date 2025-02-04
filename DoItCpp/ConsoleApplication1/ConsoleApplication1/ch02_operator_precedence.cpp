// 연산자의 우선순위 확인하기

#include <iostream>
using namespace std;

int main() {

	int a = 5, b = 2, c = 8;

	int result_1 = a + b * c;	// 곱셈 먼저 연산(오른쪽으로 결합)
	cout << "Result_1 : " << result_1 << endl;

	int result_2 = (a + b) * c;	// 괄호로 우선순위 변경
	cout << "Result_2 : " << result_2 << endl;

	a += b * c;	// 곱셈 먼저 연산
	cout << "Result_3 : " << a << endl;

	bool condition = true;
	int result_4 = (condition && a > b) ? a : b;	// > 먼저 연산*왼쪽으로 결합)
	cout << "Result 4 : " << result_4 << endl;

	return 0;
}