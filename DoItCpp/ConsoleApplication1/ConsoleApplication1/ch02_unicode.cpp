// 다양한 언어로 인사말 출력하기

#include <iostream>
#include <io.h>
#include <fcntl.h>

using namespace std;

int main()
{
	wchar_t message_korean[] = L"반갑다 세계야!";		// 한국어
	/*
	wchar_t message_chinese[] = L"~";	// 중국어
	wchar_t message_japanese[] = L"~";	// 일본어
	wchar_t message_russian[] = L"~";	// 러시아어
	*/

	cout << "Hello World!" << endl;

	_setmode(_fileno(stdout), _O_U16TEXT);	// 윈도우 콘솔 창 유니코드 출력

	wcout << message_korean << endl;
	/*
	wcout << message_chinese << endl;
	wcout << message_japanese << endl;
	wcout << message_russian << endl;
	*/

	return 0;
}