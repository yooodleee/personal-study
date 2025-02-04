// if 조건문으로 분기하기

#include <iostream>
using namespace std;

int main() {

	int a = 7;
	int b = 5;
	int result;

	if (a > b)
		return a;	// a > b가 true -> result에 a값 저장
	else
		return b;	// a > b가 false -> result에 b값 저장

	cout << "result = " << result << endl;

	return 0;
}