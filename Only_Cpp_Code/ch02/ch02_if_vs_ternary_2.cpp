// 삼항 연산자 활용하기 

/**
 * 같은 예를 if 문 대신, 삼항 연산자로 바꾸면 다음과 같다. 
 * 
 * 간단한 if ~ else 문은 삼항 연산자로 간략하게 쓸 수 있다. 
 */

#include <iostream>
using namespace std;

int main() {

	int a = 7;
	int b = 5;
	int result;

	result = a > b ? a : b;	 // a > b 결과에 따라 result에 a값 또는 b값 저장 

	cout << "result = " << result << endl;

	return 0;
}

/**
 * 삼항 연산자는 if 조건문보다 코드를 간략하게 작성할 수 있지만, 무분별하게 사용하면 오히려
 * 가독성이 떨어질 수 있다. 그리고 한 줄 단위로 디버깅할 때 더 불편하게 할 수도 있다. 
 * 따라서 삼항 연산자는 코드의 가독성을 해치지 않는 범위에서 적절하게 사용하는 것이 좋다. 
 */

// result = 7