// if 조건문으로 분기하기 

/**
 * 삼항 연산자 표현식(ternary operator expression)
 * 
 * 유일하게 피연산자가 3개이다. 
 * 조건식 ? 참일_때_표현식 : 거짓일_때_표현식 
 * 
 * 삼항 연산자는 if ~ else 문처럼 동작하므로 먼저 조건식의 결과에 따라 분기하는 간단한 예를 보겠다. 
 * 다음에서 변수 a는 7, b는 5로 초기화했으므로 result 변수에는 a 값이 저장된다. 
 */

#include <iostream>
using namespace std;

int main() {

	int a = 7;
	int b = 5;
	int result;

	if (a > b)
		return a;	// a > b가 true이면, result에 a 값 저장
	else
		return b;	// a > b가 false이면, result에 b 값 저장 

	cout << "result = " << result << endl;

	return 0;
}