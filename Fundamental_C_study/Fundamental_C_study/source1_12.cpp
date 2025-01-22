#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	unsigned int ui = 0xFFFFFFFF;

	float f;
	memcpy(&f, &ui, 4);			// (1) f is NaN
	cout << f << endl;

	float f2 = f + f;			// (2) f2 is NaN
	cout << f2 << endl;
}