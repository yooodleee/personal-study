#include <iostream>
using namespace std;

void main()
{
	long long ll = 1;	// 최댓값 설정
	ll = (ll << 63);
	ll = ~ll;

	printf(" (A) %d \r\n", ll);		// (A)
	printf(" (B) %lld \r\n", ll);	// (B)
	printf(" (C) %I64d \r\n", ll);	// (C)

}