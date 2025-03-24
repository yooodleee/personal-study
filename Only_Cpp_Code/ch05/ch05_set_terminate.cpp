// 예외 처리 실패에 대응하기 

/**
 * 예외 처리 실패 대응 => set_terminate
 * 
 * throw 문으로 예외를 던졌는데 해당 예외를 받을 catch 문이 아예 없거나 있어도 형식이 맞지 않으면 
 * 프로그램은 강제로 종료된다. 이때 종료 처리 함수를 설정하는 set_terminate로 프로그램이 강제 종료
 * 되기 전에 특정 동작을 수행하도록 구성할 수 있다. 
 * => set_terminate(종료_처리_함수);
 * => 내부적으로 terminate라는 런타임 함수에서 프로그램을 강제로 종료시키는 abort 함수가 호출된다. 
 * 
 * set_terminate로 종료 처리 함수를 지정하여 예외 처리 실패에 대응하는 예를 보자. 
 */

#include <iostream>
#include <cstdlib>

using namespace std;


// 종료 처리 함수 
void myterminate() {

	cout << "myterminate called" << endl;
	exit(-1);		// 프로그램을 비정상 종료 
}

int main() {

	set_terminate(myterminate);		// 종료 처리 함수 지정
	throw 1;		// 예외 발생 

	return 0;		// throw로 예외를 던졌으므로 실행되지 않음
}

/**
 * mytermiate called
 */

/**
 * main 함수에서 throw 1 코드를 만나면 catch 문을 찾을 수 없어 오류가 발생하고 프로그램이
 * 강제로 종료된다. 그런데 강제로 종료되기 전에 set_terminate로 지정한 종료 처리 함수가
 * 호출된다. 
 * 
 * 종료 처리 함수로 지정한 myterminate에서는 프로그램을 강제로 종료하는 exit 함수를 사용했다. 
 * exit 함수는 <cstdlib> 헤더에 정의되어 있다. exit 함수에 상태 코드로 0을 전달하면 프로그램을
 * 정상으로, -1을 전달하면 비정상으로 종료한다. 이 상태 코드에 따라 내부에 정의된 각종 정리 작업을
 * 수행한다. 비슷한 함수로 abort가 있는데 이 함수는 어떤 정리 작업도 수행하지 않은 채 프로그램을
 * 비정상으로 즉시 종료한다. 
 */