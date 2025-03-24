// switch 문으로 분기하기

/**
 * 조건에 따른 분기가 여럿일 때도 if else 문으로 처리할 수 있겠지만, 갈래가 많으면 코드를
 * 읽기가 어려워진다. 이때 switch 문을 사용할 수 있다. switch 문은 여러 경우의 수 가운데
 * 하나를 선택해 실행할 때 사용한다. 
 * 
 * switch 문의 동작 방식
 * 
 * switch 문은 하나의 변수나 표현식을 결과에 따라 다양한 경우(case) 중 하나를 선택해 해당
 * 코드를 실행한다. switch 문을 이용하면 변숫값에 따라 다양한 동작을 수행하게 할 수 있다. 
 * 
 * switch (표현식)
 * {
 * case 상수1:
 * 		실행문1
 * 		break;
 * 
 * case 상수2: 
 * 		실행문2
 * 		break;
 * 
 * case 상수3:
 * 		실행문3
 * 		break;
 * 
 * case 상수4:
 * 		실행문4
 * 		break;
 * 
 * case 상수5:
 * 		실행문5
 * 		break;
 * 
 * default: 
 * 		실행문
 * 
 * }
 * switch 문 밖 
 * 
 * switch 문의 동작 방식은 간단하다. switch 문에서 표현식의 값을 평가하고 그 결과가 각 case의
 * 레이블과 같은지 확인한다. 이때 레이블(label)은 경우의 수를 나타내는 상수이다. 그리고 평가한
 * 값과 같은 레이블에 작성된 구문들을 실행한다. 만약 일치하는 레이블이 없으면 기본으로 default
 * 구문을 실행한다. case 문에서 break 키워드는 switch 문을 빠져나가는 역할을 한다. 
 */

#include <iostream>
using namespace std;


int main() {

	int input_number;

	cout << "1 ~ 5 정수 입력 : ";
	cin >> input_number;

	switch (input_number)
	{
		// 여러 case 가운데 하나로 분기합니다. 일치하는 case가 없다면 default로 분기합니다.
	case1:
		cout << "입력한 수는 1 입니다." << endl;
		break;
	case2:
		cout << "입력한 수는 2 입니다." << endl;
		break;
	case3:
		cout << "입력한 수는 3 입니다." << endl;
		break;
	case4:
		cout << "입력한 수는 4 입니다." << endl;
		break;
	case5:
		cout << "입력한 수는 5 입니다." << endl;
		break;
	default:
		cout << "입력한 수는 1 ~ 5 범위 밖입니다." << endl;
		break;
	}

	return 0;
}

/*
1 ~ 5 정수 입력: 1
입력한 수는 1 입니다. 
*/

/**
 * 1 ~ 5 정수 입력: 5
 * 입력한 수는 5 입니다. 
 */

/**
 * 1 ~ 5 정수 입력: 7
 * 입력한 수는 1 ~ 5 범위 밖입니다. 
 */