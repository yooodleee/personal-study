#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	printf("%.3f\r\n", 0.3255);			// (1) 0.326
	printf("%.3f\r\n", 0.4255);			// (2) 0.425
	printf("%.3f\r\n", 0.42550001);		// (3) 0.426
}