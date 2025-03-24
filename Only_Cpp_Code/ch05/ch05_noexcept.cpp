// noexcept로 명시된 함수에서 예외 던지기 

/**
 * 예외 처리 생략과 실패 대응
 * 
 * 프로그래밍은 예측불허의 여정이다. 코드가 실행되는 동안 예외 상황은 피할 수 없고, 심지어 예외 처리
 * 메커니즘도 때로는 예외를 처리하지 못할 수도 있다. noexcept와 set_terminate를 활용해 예외 처리와 
 * 예외 처리 실패에 대응하고 프로그램의 안정상과 신뢰성을 높이는 방법에 대해 알아보자. 
 */

/**
 * 예외 처리 생략 => noexcept
 * 
 * 함수에서 문제가 발생할 때 만드시 예외를 발생시켜야 하는 것은 아니다. 때로는 예외를 발생시키는 것이 
 * 득보다 실이 더 클 때도 있다. 오류와 예외는 엄연히 다른 것이다. 값이나 실행 흐름을 충분히 예측할 수 
 * 있을 때는 if 문으로 처리하는 것이 성능 면에서 훨씬 이득이다. 
 * 
 * 함수가 예외를 던지지 않음을 나타낼 때는 다음처럼 noexcept 키워드로 명시할 수 있다. 이처럼 함수가 예외를
 * 던지지 않음을 명시하면 컴파일러가 코드를 최적화하고 빠르게 실행하는 데에 도움이 된다. 
 * => int func() noexcept
 * 
 * 또는 다음처럼 함수를 호출할 때 noexcept 키워드를 사용할 수 있다. 그러면 컴파일할 때 해당 함수가 예외를
 * 던지는지 확인해 true나 false로 알려준다. 
 * => bool does_not_throw = noexcept(my_function());
 * 
 * 참고로 함수에 noexcept 키워드를 붙였다고 해서 예외를 던지지 못하는 것은 아니다. noexcept가 명시된 함수에서 
 * 예외를 던지면 어떻게 되는지 다음 코드를 살펴보자. 
 */

#include <iostream>
using namespace std;


void real_noexcept() noexcept	// 예외를 던지지 않음을 명시 
{

	cout << "real_noexcept" << endl;
}

// noexcept로 명시된 함수 안에서 예외 발생 
void fake_noexcept() noexcept {

	cout << "fake_noexcept" << endl;
	throw 1;	// 정수 형식 예외 발생 
}

int main() {

	real_noexcept();

	try {

		fake_noexcept();
	}
	catch (int exec) {

		cout << "catch" << exec << endl;
	}

	return 0;
}

/**
 * warning C4297: 'fake_noexcept': 함수는 예외를 Throw하지 않도록 지정되었으나 예외를 Throw했습니다. 
 * message: 함수에서 __declspec(nothrow), throw(), noexcept(true) 또는 noexcept를 지정했습니다. 
 */

/**
 * 이 코드를 컴파일하면 경고는 발생하지만 어쨌든 실행 파일은 만들어진다. 컴파일러는 noexcept 키워드가
 * 붙은 함수는 예외를 던지지 않을 것으로 간주하고 그대로 컴파일한다. 하지만 실행해 보면 런타임 오류 메시지가
 * 발생하며 프로그램은 강제로 종료된다. 
 */