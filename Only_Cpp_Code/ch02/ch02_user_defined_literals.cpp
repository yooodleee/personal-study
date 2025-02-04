// 사용자 정의 리터럴로 거리 단위 변환하기

#include <iostream>
using namespace std;


const long double km_per_mile = 1.609344L;

long double operator"" _km(long double val)		// _km 사용자 리터럴 정의
{
	return val;	// 아무런 변화 없이 그대로 반환
}

long double operator"" _mi(long double val)		// _mi 사용자 리터럴 정의
{
	return val * km_per_mile;	// 마일을 킬로미터로 변환하여 반환
}

int main() {
	long double distance_1 = 1.0_km;	// 킬로비터는 그대로 저장
	long double distance_2 = 1.0_mi;	// 마일은 킬로미터 단위로 변환해서 저장

	cout << distance_1 + distance_2 << "km" << endl;	// 킬로미터로 출력

	return 0;
}

// 2.60934km