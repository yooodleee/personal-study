#include <stdio.h> 
#include <iostream>
#include <cstring>		// CString 함수를 사용하기 위한 헤더파일
using namespace std;

void main()
{
	//////////////////////////////////
	CString str1 = "ABSCDEFG";
	cout << str1 << str1.GetLength() << endl;

	char* p1 = str1.GetBuffer();	// (1) 문자 배열을 얻는다.
	p1[3] = '\0';					// (2) 문자 배열을 수정한다.
	cout << str1 << str1.GetLength() << endl;	

	/////////////////////////////////
	string str2 = "ABCDEFG";
	cout << str2.c_str() << str2.size() << endl;

	char* p2 = (char*)str2.c_str();	// (1) 문자 배열을 얻는다.
	p2[3] = '\0';					// (2) 문자 배열을 수정한다.
	cout << str2.c_str() << str2.size() << endl;

}