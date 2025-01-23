#include <stdio.h>
#include <iostream>
#include <typeinfo>
using namespace std;

void main()
{
	const int& ra = 1;				// (1)
	int* pa = (int*)&ra;			// (2)
	*pa = 2;
	cout << ra << endl;
}

// 2