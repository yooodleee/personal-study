#include <stdio.h> 
#include <iostream>
#include <cstring>		// CString �Լ��� ����ϱ� ���� �������
using namespace std;

void main()
{
	//////////////////////////////////
	CString str1 = "ABSCDEFG";
	cout << str1 << str1.GetLength() << endl;

	char* p1 = str1.GetBuffer();	// (1) ���� �迭�� ��´�.
	p1[3] = '\0';					// (2) ���� �迭�� �����Ѵ�.
	cout << str1 << str1.GetLength() << endl;	

	/////////////////////////////////
	string str2 = "ABCDEFG";
	cout << str2.c_str() << str2.size() << endl;

	char* p2 = (char*)str2.c_str();	// (1) ���� �迭�� ��´�.
	p2[3] = '\0';					// (2) ���� �迭�� �����Ѵ�.
	cout << str2.c_str() << str2.size() << endl;

}