#include <iostream>
using namespace std;

void main()
{
	float f[10];
	f[0] = 33554432;
	f[1] = 33554433;
	f[2] = 33554434;
	f[3] = 33554435;
	f[4] = 33554436;
	f[5] = 33554437;
	f[6] = 33554438;
	f[7] = 33554439;
	f[8] = 33554440;
	f[9] = 33554441;

	cout.precision(32);			// (1)
	for (int i = 0; i < 10; i++)
	{
		cout << f[i] << endl;
	}
}