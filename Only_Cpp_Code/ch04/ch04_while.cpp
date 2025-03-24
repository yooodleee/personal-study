// while 반복문

/**
 * 반복문으로 흐름 제어
 * 
 * 반복은 프로그램에서 자주 사용하는 개념이다. C++ 언어에서는 여러 반복문을 제공하지만,
 * 그중 가장 단순한 while과 do ~ while 문을 먼저 보겠다.abort
 * 
 * while 문으로 반복하기
 * 
 * while 문은 주어진 조건이 참인 동안에만 특정 코드 블록을 반복해서 실행한다. 조건이 참인지에
 * 따라 프로그램의 흐름이 결정된다. 간단한 코드를 직접 실행해 보면서 어떻게 동작한느지 알아보자. 
 */

#include <iostream>
using namespace std;


int main() {

	int count = 0;

	while (count < 5) {
		cout << "count : " << count << endl;
		count++;
	}

	return 0;
}

/*
count : 0
count : 1
count : 2
count : 3
count : 4
*/

/**
 * while 문은 조건식의 결과가 참이면 while 문 블록의 구문들이 실행되고, 거짓이면 실행되지 않는다. 
 * count의 초깃값은 0이며 while의 조건식 count < 5가 참인지 판별한다. 조건식이 참이면 반복문 내부의
 * count 값을 출력하는 구문이 실행되고 count는 1씩 증가한다. 
 * 
 * 이 과정을 반복하다가 count 값이 5가 되면 조건식 count < 5가 거짓이 되어 반복을 종료하고 while 문의
 * 블록을 빠져나온다. 반복문에서 조건이 항상 참이면 무한 반복한다. 따라서 반드시 중지 조건을 명시해야
 * 한다. 
 */