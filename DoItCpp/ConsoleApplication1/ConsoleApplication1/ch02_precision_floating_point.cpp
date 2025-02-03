// 부동 소수점의 최대 유효 자릿수만큼 출력하기

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	float float_value = 9.87654321f;
	double double_value = 9.87654321987654321;
	long double long_double_value = 9.87654321987654321l;

	cout << "float: " << sizeof(float) << " bytes" << endl;
	cout << "float_value: " << setprecision(numeric_limits<float>::digits10 + 1) << float_value << endl << endl;	// 유효 자릿수만큼 정밀도 조정

	cout << "double: " << sizeof(double) << " bytes" << endl;
	cout << "double_value: " << setprecision(numeric_limits<double>::digits10 + 1) << double_value << endl << endl;

	cout << "long double: " << sizeof(long double) << " bytes" << endl;
	cout << "long_double_value: " << setprecision(numeric_limits<long double>::digits10 + 1) << long_double_value << endl << endl;

	return 0;
}

/*
float: 4 bytes
float_value: 9.876543

double: 8 bytes
double_value: 9.876543219876543

long double: 8 bytes
long_double_value: 9.876543219876543
*/