// if를 활용한 조건 분기(중괄호 생략)

/**
 * if 문에 중괄호 생략
 * 
 * 만약 if나 else if, else의 본문에 실행할 구문이 오직 하나만 있다면, 블록을 지정하는 중괄호 {}를
 * 생략할 수 있다. 중괄호를 생략하면 다음과 같다. 
 */

#include <iostream>
using namespace std;


int main() {

	int input_number;

	cout << "정수 입력 : ";
	cin >> input_number;

	if (input_number > 0)
		cout << "입력한 수는 양수 입니다." << endl;
	else if (input_number < 0)
		cout << "입력한 수는 음수 입니다." << endl;
	else
		cout << "입력한 수는 0 입니다." << endl;

	return 0;
}

/*
그런데 이렇게 하면 코드의 줄 수는 줄겠지만, 분기별로 실행할 구문이 여러 개일 때 블록 지정을 빠뜨리는
실수를 할 수 있다. 따라서 될 수 있으면 블록을 확실하게 지정해주는 것이 좋다. 

if ~ else if ~ else 문

if (조건식) {
	// 조건식이 참일 때
}

if (조건식) {
	// 조건식이 참일 떄
} else {
	// 조건식이 거짓일 때
}

if (조건식 1) {
	// 조건식 1이 참일 때
} else if (조건식 2) {
	// 조건식 1이 거짓이고, 조건식 2가 참일 때
} else {
	// 조건식 1, 조건식 2가 모두 거짓일 때 
}
*/