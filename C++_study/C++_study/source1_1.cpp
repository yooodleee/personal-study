#include <iostream>	// cout을 사용하려면 <iostream>

using namespace std;

void main()
{
	int i = 1;
	i = (i << 31);
	cout << i << endl;	// (1) signed int 최솟값

	i = ~i;
	cout << i << endl;	// (2) signed int 최댓값

	unsigned ui = 0;
	cout << ui << endl;	// (3) unsigned int 최솟값

	ui = -1;
	cout << ui << endl;	// (4) unsigned int 최댓값

}