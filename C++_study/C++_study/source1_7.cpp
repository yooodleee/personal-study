#include <iostream>
using namespace std;

void main()
{
	float f[10];
	f[0] = 8388608.0;
	f[1] = 8388608.1;
	f[2] = 8388608.2;
	f[3] = 8388608.3;
	f[4] = 8388608.4;
	f[5] = 8388608.5;
	f[6] = 8388608.6;
	f[7] = 8388608.7;
	f[8] = 8388608.8;
	f[9] = 8388608.9;

	cout.precision(32);				// (1)
	for (int i = 0; i < 10 i++)
	{
		cout << f[i] << endl;
	}
}