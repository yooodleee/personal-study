// 부동 소수점 출력하기

#include <iostream>
using namespace std;

int main()
{
	cout << 9.87654321f << endl;	// 값 끝에 f를 붙이면 float 부동 소수점
	cout << 987654.321f << endl;
	cout << 9876543.21f << endl;
	cout << 0.00000987654321f << endl;
	cout << 0.00000000000987654321f << endl;

	return 0;
}

/*
9.87654
987654
9.87654e+06
9.87654e-06
9.87654e-12
*/