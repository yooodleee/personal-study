#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	////////////////////////////////////////////
	char c;							// signed type
	c = 0x02;						// [0000,0010]		2
	c = c >> 1;						// [0000,0001]		1
	cout << (int)c << endl;

	c = 0x82;						// [1000,0010]		-126
	c = c >> 1;						// [1100,0001]		-63
	cout << (int)c << endl;

	//////////////////////////////////////////
	unsigned char uc;				// unsigned type
	uc = 0x02;						// [0000,0010]		2
	uc = uc >> 1;					// [0000,0001]		1
	cout << (int)uc << endl;

	uc = 0x82;						// [1000,0010]		130
	uc = uc >> 1;					// [0100,0001]		65
	cout << (int)uc << endl;
}