// 포인터 변수가 가리키는 값을 상수화

#include <iostream>
using namespace std;


int main() {

	int a = 0;
	const int* ptr = &a;	// *ptr을 상수화

	a = 1;	// 컴파일 통과
	*ptr = 2;	// 컴파일 오류 발생

	return 0;
}

/*
심각도	코드	설명	프로젝트	파일	줄	비표시 오류(Suppression) 상태	세부 정보
오류(활성)	E0137	식이 수정할 수 있는 lvalue여야 합니다.	
*/