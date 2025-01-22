#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	int i = 1;
	i = (i << 31);
	cout << i << endl;		// (1) signed int ÃÖ¼Ú°ª

	i = ~i;
	cout << i << endl;		// (2) signed int ÃÖ´ñ°ª

	unsigned ui = 0;
	cout << ui << endl;		// (3) unsigned int ÃÖ¼Ú°ª

	ui = -1;
	cout << ui << endl;		// (4) unsigned int ÃÖ´ñ°ª
}