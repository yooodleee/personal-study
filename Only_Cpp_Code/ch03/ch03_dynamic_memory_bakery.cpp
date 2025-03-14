// 방문하는 손님 수만큼 빵 만들기

/**
 * 포인터와 동적 메모리 할당
 * 
 * 포인터와 동적 메모리 할당을 연습하는 차원으로 방문하는 손님 수만큼 빵을 만들도록 한다. 
 * 매일 가게에 방문하는 손님 수만큼 빵을 만드는 것이 목표이다. 
 */

#include <iostream>
#include <string>


using namespace std;

int main() {

	int customer_num = 0;

	cout << "오늘 방문 손님: ";
	cin >> customer_num;	// 손님 수 입력

	string* bread = new string[customer_num];	// 손님 수 만큼 string 배열 생성 

	for (int i = 0; i < customer_num; i++)	// 입력 받은 손님 수만큼 반복 
	{
		bread[i] = "빵_" + to_string(i);		// '빵_숫자' 형태로 배열에 저장, to_string => 숫자를 문자열로 변환 
	}

	cout << endl << "--생산된 빵--" << endl;
	for (int i = 0; i < customer_num; i++)
	{
		cout << *(bread + i) << endl;	// 생산된 빵 출력 (포인터 연산 참고)
	}

	delete[] bread;	// string 배열 삭제(해제)

	return 0;
}

/**
 * 실행 결과 
 * 
 * 오늘 방문 손님 : 3 (enter)
 * 
 * --생산된 빵--
 * 빵_0
 * 빵_1
 * 빵_2
 */
