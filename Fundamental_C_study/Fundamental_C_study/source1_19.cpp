#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <ctime>

void main()
{
	time_t ct;
	time(&ct);							// (1) ���� �ð� �б�
	tm* pT = localtime(&ct);			// (2) tm ����
}

// localtime: This function or variable may be unsafe
// Consider using localtime_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS