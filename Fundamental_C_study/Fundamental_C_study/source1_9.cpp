#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	float f = 33554432 + 3;
	cout << f << endl;				// 33554436 ���

	long long ll = 33554432 + 3;	// 33554435 ���
	cout << f << endl;
}

//3.35544e+07
//3.35544e+07