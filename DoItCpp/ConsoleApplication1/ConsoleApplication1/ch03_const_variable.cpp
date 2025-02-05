// const로 지정한 변수에 값 대입 시도

#include <iostream>
using namespace std;


int main() {

	const int a = 1;
	a = 2;	// 컴파일 오류 발생

	return 0;
}

/*
식이 수정할 수 있는 lvalue여야 합니다.
*/