#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	int max1 = 18446744073709551615;		// ��� �ִ�
	int max2 = 18446744073709551616;		// Compile Error
	int min1 = -18446744073709551615;		// ��� �ּڰ�
	int min2 = -18446744073709551616;		// Compile Error
}