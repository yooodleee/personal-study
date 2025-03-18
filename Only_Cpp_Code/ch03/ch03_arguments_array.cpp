// 배열을 매개변수로 사용하기

/**
 * 배열을 함수의 매개변수로 사용하는 예를 살펴보자.
 * 배열을 사용하면 자료형이 같은 여러 개를 한 번에 전달할 수 있다. 
 */

#include <iostream>
using namespace std;

int average(int _array[], int _count) {

	int sum = 0;
	for (int i = 0; i < _count; i++)
	{
		sum += _array[i];
	}

	return (sum / _count);
}

int main() {

	int score[5] = { 90, 75, 80, 100, 65 };
	cout << "��� ���� : " << average(score, 5) << endl;

	return 0;
}

// 평균 점수 : 82

/**
 * average는 매개변수로 받은 배열 안에 저장된 점수들의 평균을 계산하는 함수이다. 
 * 이 함수의 매개변수인 _array[]는 점수 배열을, count는 배열에 점수가 몇 개 들어 있는지 알려주는 역할을 한다. 
 * 여기서 _array[] 대신 int *_array처럼 포인터 변수로 바꿔도 문제가 없다. 이것은 배열로 매개변수를 사용하면
 * 포인터와 마찬가지로 실제로는 주솟값을 전달 받는다는 의미이다. 예에서는 score 배열의 시작 주소를 전달받는다. 
 * 
 * 따라서 average 함수에서는 main 함수에 정의된 score 배열에 저장된 데이터에 직접 접근할 수 있다. 심지어 
 * 매개변수인 _array 배열의 데이터를 변경하면 main에 있는 score 배열의 데이터도 변경된다. 
 */