#include <iostream>
using namespace std;

void main()
{
	unsigned int ui = 0xC11B0000;

	float f;
	memcpy(&f, &ui, 4);
	cout << f << endl;
}