#include <iostream>	// cout�� ����Ϸ��� <iostream>

using namespace std;

void main()
{
	int i = 1;
	i = (i << 31);
	cout << i << endl;	// (1) signed int �ּڰ�

	i = ~i;
	cout << i << endl;	// (2) signed int �ִ�

	unsigned ui = 0;
	cout << ui << endl;	// (3) unsigned int �ּڰ�

	ui = -1;
	cout << ui << endl;	// (4) unsigned int �ִ�

}