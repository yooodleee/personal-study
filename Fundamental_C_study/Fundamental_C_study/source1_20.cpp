#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <ctime>
#include <time.h>
using namespace std;

void main()
{
	time_t ct;						
	time(&ct);						// (1) ���� �ð� ���
	tm* pT = localtime(&ct);		// (2) tm ����

	pT->tm_mday += 50;				// (3) ���� ��¥�κ��� 50�� ��
	mktime(pT);						// (4) pT ����
	cout << pT->tm_year + 1900 << "��" << endl;
	cout << pT->tm_mon + 1 << "��" << endl;
	cout << pT->tm_mday << "��" << endl;
}