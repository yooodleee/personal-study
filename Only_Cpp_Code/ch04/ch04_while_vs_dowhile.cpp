// while, do ~ while 차이점


#include <iostream>
using namespace std;


int main() {

	int i = 0;
	
	while (i < 0) {	// 조건식이 거짓이므로 반복문은 전혀 실행되지 않는다. 
		cout << "i is less than 0" << endl;
		i++;
	}

	int j = 0;

	do {
		cout << "j is less than 0" << endl;
		j++;
	} while (j < 0);	// 조건식이 거짓이지만 반복문은 1회 실행된다. 


	return 0;
}

// j is less than 0

/**
 * 예에서 while 문은 i < 0 조건이 처음부터 거짓이므로 반복문 내부의 코드가 실행되지 않는다. 
 * 반면에 do ~ while 문은 조건이 평가되기 전에 반복문 내부의 코드가 한 번 실행되어 
 * "j is less than 0"가 출력된다. 이처럼 조건을 평가하는 순서가 다른 특성을 이용하여 반복문을
 * 적절하게 구현할 수 있다. 
 */