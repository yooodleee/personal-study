#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <ctime>
#include <time.h>
using namespace std;

void main()
{
	time_t ct;						
	time(&ct);						// (1) 현재 시간 얻기
	tm* pT = localtime(&ct);		// (2) tm 설정

	pT->tm_mday += 50;				// (3) 현재 날짜로부터 50일 뒤
	mktime(pT);						// (4) pT 갱신
	cout << pT->tm_year + 1900 << "년" << endl;
	cout << pT->tm_mon + 1 << "월" << endl;
	cout << pT->tm_mday << "일" << endl;
}