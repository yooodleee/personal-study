// 처리되지 않은 모든 예외 받기

/**
 * catch(...) 문으로 기타 예외 처리
 * 
 * 만약 어떤 데이터 형식의 예외를 throw로 던졌는데, 받아 주는 catch 문이 없다면 
 * 어떻게 될까? 다음을 살펴보자. 
 * 
 * 예외를 던졌지만 받아 주는 catch 문이 없다면?
 * 
 * #include <iostream>
 * using namespace std;
 * 
 * int main()
 * {
 * 		try
 * 		{
 * 			throw 1;		// 예외 1 발생(정수 형식의 예외)
 * 		}
 * 		catch (char c)		// 문자 형식 에외 받기 
 * 		{
 * 			cout << "catch " << c << endl;
 * 		}
 * 
 * 		return 0;
 * }
 */

/**
 * 정수 형식 예외를 throw로 던졌지만, 문자 형식 예외를 받는 catch만 있는 상태이다. 
 * 실행해 보면 런타임 오류가 발생하며 프로그램이 강제로 종료된다. 윈도우 운영체제의
 * VC++ 환경에서 테스트해 보면 'abort() has been called'라는 메시지를 볼 수 있다. 
 * 즉, 어떤 예외를 던졌다면 이를 받을 수 있는 구문이 있어야 한다는 의미이다. 
 * 
 * 하지만 모든 예외의 짝을 맞춰 예외 처리 코드를 작성하는 것은 쉽지 않다. if 조건문의
 * else나 switch의 default처럼 일부 예외는 뭉뚱그려서 한 번에 처리하고 싶을 때가 있다. 
 * C++ 언어의 예외 처리에서는 catch(...) 문으로 이러한 요구에 대응할 수 있다. 즉, 
 * catch(...) 문은 명시하지 않은 나머지 모든 예외를 받아서 처리할 때 사용한다. 
 */

#include <iostream>
using namespace std;


int main() {

	try {

		int input;
		cout << "정수 중 하나를 입력해보세요 : ";
		cin >> input;

		if (input > 0) {		// 입력받은 숫자가 양수이면 
			
			cout << "throw 1" << endl;
			throw 1;		// 예외 1 발생 (정수 형식 예외)
			cout << "after trhow 1" << endl;
		}

		if (input < 0) {		// 입력받은 숫자가 음수이면 

			cout << "trhow -1.0f" << endl;
			throw - 1.0f;	// 예외 1.0f 발생(부동 소수점 형식 예외)
			cout << "after throw -1.0f" << endl;
		}

		if (input == 0) {		// 입력받은 정수가 0이면 

			cout << "throw Z" << endl;
			throw 'Z';	// 예외 Z 발생 (문자 형식 예외)
		}
	}
	catch (int a) {		// 정수 형식 예외 받기 
		
		cout << "catch" << a << endl;
	}
	catch (...) {		// 처리되지 않은 나머지 예외 모두 받기 
		cout << "catch all" << endl;
	}

	return 0;
}

/**
 * 정수 중 하나를 입력해보세요: 1
 * throw 1
 * catch 1
 */

/**
 * 정수 중 하나를 입력해보세요: -1
 * throw -1.0f
 * catch all
 */

/**
 * 정수 중 하나를 입력해보세요: 0
 * throw Z
 * catch all
 */

/**
 * 결과를 보면 정수 형식을 제외한 나머지 예외는 모두 catch(...) 문에서 처리되어 'catch all'이라는 
 * 메시지를 확인할 수 있다. 그렇다면 모든 예외를 catch(...) 문으로 처리하면 간단할 것 같다. 하지만
 * 예외를 구별하지 않고 하나로 받는 것은 적절한 예외 처리라고 볼 수 없다. 예외는 종류마다 제대로 
 * 구분해서 처리해 줘야 더 완벽한 프로그램을 만들 수 있다. 
 */