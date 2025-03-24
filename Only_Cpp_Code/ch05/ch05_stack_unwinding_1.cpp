// 예외가 전달되는 동작 확인하기

/**
 * 예외가 전달되는 순서
 * 
 * C++에서 예외 처리는 주로 try, catch, throw 문으로 구현한다. 이러한 구문들은 예외가 발생했을 
 * 때 프로그램의 제어 흐름을 변경하고 오류를 처리하는 데 사용한다. try 블록에서 예외가 발생하면 
 * 먼저 같은 영역(scope)에 있는 catch 문을 찾는다. 그런데 다음 코드처럼 예외를 던진 func_throw
 * 함수에 catch 문이 없으면 어떻게 될까?
 */

#include <iostream>
using namespace std;


void func_throw() {

	cout << "func_throw()" << endl;
	cout << "throw -1" << endl;

	throw - 1;	// 정수 형식 예외 던지기 
	cout << "after throw - 1" << endl;
}

int main() {

	try {
		func_throw();
	}

	catch (int exec) {		// 정수 형식 예외 받기 

		cout << "catch " << exec << endl;
	}

	return 0;
}

/*
func_throw()
throw -1
catch -1
*/

/**
 * 실행 결과를 보면 func_throw 함수에서 던진 예외가 이 함수를 호출한 main 영역의 
 * catch 문에서 정상으로 처리된 것을 확인할 수 있다. 즉, 예외 처리의 책임은 throw가 
 * 발생한 함수를 호출한 쪽으로 넘어간다. 이처럼 함수에서 예외가 처리되지 않아 함수를 
 * 호출한 쪽으로 전달되는 현상을 가리켜 스택 풀기(stack unwinding)라고 한다. 
 * 
 * 그리고 예외가 발생하면 해당 함수의 남은 코드들은 더 이상 수행되지 않고 종료된다. 
 * 따라서 func_throw 함수에서 'after throw - 1' 은 출력되지 않는다. 
 * 
 * 예외가 전달되는 과정을 단계별로 살펴보면 스택 풀기의 의미를 확실하게 이해할 수 있다. 
 */