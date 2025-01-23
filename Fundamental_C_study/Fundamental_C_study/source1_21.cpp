#include <stdio.h>
#include <iostream>
#include <typeinfo>
using namespace std;

void main()
{
	int a = 1;
	int& ra = a;			// Reference
	ra = 2;
	cout << a << endl;

	int* pa = &a;				// Pointer
	*pa = 3;
	cout << a << endl;
}