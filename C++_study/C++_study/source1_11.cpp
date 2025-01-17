#include <iostream>
using namespace std;

void main()
{
	unsigned int ui = 0x7F80000;

	float f;
	memcpy(&f, &ui, 4);			// (1) f is infinity
	cout << f << endl;

	float f2 = f + f;			// (2) f2 is infinity
	cout << f2 << endl;
}