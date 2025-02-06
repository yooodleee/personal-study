// switch를 활용한 조건 분기

#include <iostream>
using namespace std;


int main() {

	int input_number;

	cout << "1 ~ 5 사이의 정수 입력 : ";
	cin >> input_number;

	switch (input_number)
	{
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
		cout << "입력한 수는 1 ~ 5 사이의 범위 밖의 정수입니다." << endl;
		break;
	}

	return 0;
}

/*
1 ~ 5 사이의 정수 입력 : 7
입력한 수는 1 ~ 5 사이의 범위 밖의 정수입니다.
*/