// 예외 처리 실패에 대응하기

#include <iostream>
#include <cstdlib>

using namespace std;


// 종료 처리 함수
void myterminate() {

	cout << "myterminate called" << endl;
	exit(-1);		// 프로그램을 비정상으로 종료
}

int main() {

	set_terminate(myterminate);		// 종료 처리 함수 지정
	throw 1;		// 예외 발생

	return 0;		// throw로 예외를 던졌으므로 실행되지 않음
}