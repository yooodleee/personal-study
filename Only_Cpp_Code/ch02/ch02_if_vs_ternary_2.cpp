// 삼항 연산자 활용하기

#include <iostream>
using namespace std;

int main() {

	int a = 7;
	int b = 5;
	int result;

	result = a > b ? a : b;	 // a > b 결과에 따라서 result에 a값 또는 b값 저장

	cout << "result = " << result << endl;

	return 0;
}

// result = 7