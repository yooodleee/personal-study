#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	int max1 = 18446744073709551615;		// 鼻熱 譆渤高
	int max2 = 18446744073709551616;		// Compile Error
	int min1 = -18446744073709551615;		// 鼻熱 譆歐高
	int min2 = -18446744073709551616;		// Compile Error
}