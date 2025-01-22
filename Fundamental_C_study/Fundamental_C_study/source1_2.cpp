#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	char c = 1;

	c = c << 7;					// (1)
	cout << (int)c << endl;

	c = c >> 7;					// (2)
	cout << (int)c << endl;
}