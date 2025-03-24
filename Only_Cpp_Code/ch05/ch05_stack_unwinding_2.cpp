// 스택 풀기 동작 확인하기 

#include <iostream>
using namespace std;


void func_throw() {

	cout << endl;
	cout << "func_throw() 함수 내부" << endl;
	cout << "throw - 1" << endl;

	throw - 1;		// 정수 형식 예외 던지기 
	cout << "after throw - 1" << endl;
}

void func_2() {

	cout << endl;
	cout << "func_2() 함수 내부" << endl;
	cout << "func_throw() 호출" << endl;
	
	func_throw();
	cout << "after func_throw()" << endl;
}

void func_1() {
	
	cout << endl;
	cout << "func_1() 함수 내부" << endl;
	cout << "func_2() 호출" << endl;

	func_2();
	cout << "after func_2()" << endl;
}

int main() {

	cout << "main 내부" << endl;

	try {

		cout << "func_1() 호출" << endl;
		func_1();
	}

	catch (int exec) {		// 정수 형식 예외 받기 

		cout << endl;
		cout << "catch" << exec << endl;
	}

	return 0;
}

/*
main 내부
func_1() 호출 

func_1() 함수 내부
func_2() 호출

func_2() 함수 내부 
func_throw() 호출 

func_throw() 함수 내부 
throw - 1

catch-1
*/

/**
 * 이 예에서는 스택이 쌓이고 풀리는 과정을 확인하기 위해 연속으로 호출되는 함수를 여러 개 만들었다. 
 * 함수가 호출되는 순서는 다음과 같다. 
 * => main -> func_1() -> func_2() -> func_throw()
 * 
 * 함수가 호출되면 스택에 순서대로 쌓인다. 따라서 맨 마지막에 호출되는 함수가 가장 위쪽에 위치한다. 
 * func_throw 함수에서 발생한 throw - 1 예외는 func_throw 함수 내에서 처리되지 않아 이를 호출한
 * func2 함수로 전달된다. 예외를 전달받은 func2 함수에서도 처리되지 않으면 func2 함수를 호출한
 * func1 함수로 전달된다. 같은 이유로 func1 함수를 호출한 main 함수까지 예외가 전달되어 비로소 처리된다. 
 * 
 * 그리고 예외를 전달한 함수는 남은 코드를 실행하지 않고 바로 종료된다. 따라서 각 함수에서 마지막 코드인
 * 'after~~' 를 출력하는 구문은 모두 수행하지 않았다. 이처럼 예외를 전달하는 순서가 스택에 쌓인 역순이므로
 * 스택 풀기라고 한다. 
 */


/**
 * 예외 처리
 * 
 * => 예외가 발생할 수 있는 코드를 try 블록으로 감싼다. 
 * => 예외가 발생하면 프로그램의 제어는 즉시 try 블록 다음에 오는 catch 블록으로 넘어간다. 
 * => throw 키워드로 예외를 던진다. throw 다음에 지정하는 예외 형식은 모든 유형이 될 수 있다. 
 * => catch 블록에는 throw로 던진 에외 형식으로 매개변수를 선언한다. 이 매개변수로 오류 메시지 같은 예외 정보에
 * 	  접근한다. 
 * => 단일 try 블록에 catch 블록이 여러 개 있을 수 있으며, 각 블록은 서로 다른 유형의 예외를 처리하도록 정의한다. 
 * 
 * try {
 * 	// 예외가 발생할 수 있는 코드 영역
 *  throw execption_value;		// 예외를 강제로 발생시키는 코드
 * } catch (exception_type e) {
 * 	// 예외가 발생했을 때 실행되는 코드 블록
 * 	// e에는 발생한 예외의 정보가 담겨 있음 
 * 	// exception_type은 실제 예외 형식에 따라 정의 
 * }
 */