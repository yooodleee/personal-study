// assert를 이용한 예외 처리

#include <iostream>
#include <cassert>

using namespace std;


void print_number(int* _pt_int) {

	assert(_pt_int != NULL);	// 디버그 모드에서 _pt_int가 널인지 검사
	cout << *_pt_int << endl;
}

int main() {

	int a = 100;
	int* b = NULL;
	int* c = NULL;

	b = &a;
	print_number(b);

	// c는 NULL인 상태로 인자 전달
	print_number(c);


	return 0;
}

/*
100
Assertion failed: _pt_int != NULL
*/