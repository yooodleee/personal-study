#include <stdio.h>
#include <iostream>
using namespace std;

void main()
{
	long long ll = 1;					// 최댓값 설정
	ll = (ll << 63);
	ll = -ll;

	printf("(A) %d \r\n", ll);			// (A)
	printf("(B) %lld \r\n", ll);		// (B)
	printf("(C) %I64d \r\n", ll);		// (C)
}

//(A)0
//(B)-9223372036854775808
//(C)-9223372036854775808