// noexcept로 명시된 함수에서 예외 던지기

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

/*
(프로세스 30884)이(가) 3 코드(0x3)와 함께 종료되었습니다.
디버깅이 중지될 때 콘솔을 자동으로 닫으려면 [도구] -> [옵션] -> [디버깅] > [디버깅이 중지되면 자동으로 콘솔 닫기]를 사용하도록 설정합니다.
이 창을 닫으려면 아무 키나 누르세요...
*/