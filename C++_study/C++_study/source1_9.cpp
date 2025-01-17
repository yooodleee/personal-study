#include <iostream>
using namespace std;

void main()
{
	float f = 33554432 + 3;
	cout << f << endl;			// (1) 33554435 출력

	long long ll = 33554432 + 3;
	cout << ll << endl;			// (2) 33554435 출력
}