// 사용자 정의 리터럴로 거리 단위 변환하기

/**
 * 리터럴을 나타내는 접미사를 함수 이름으로 만든다. 
 * 사용자 정의 리터럴 연산자 operator"" 사용용
 */
#include <iostream>
using namespace std;


const long double km_per_mile = 1.609344L;

long double operator"" _km(long double val)		// _km 사용자 리터럴 정의
{
	return val;	
}

long double operator"" _mi(long double val)		// _mi 사용자 리터럴 정의 
{
	return val * km_per_mile;	// 마일(mile)을 킬로미터로 반환하여 변환환
}

int main() {
	long double distance_1 = 1.0_km;	// 킬로미터는 그대로 저장
	long double distance_2 = 1.0_mi;	// 마일은 킬로미터 단위로 변환해서 저장

	cout << distance_1 + distance_2 << "km" << endl;	// 

	return 0;
}

// 2.60934km