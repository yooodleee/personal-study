// �پ��� ���� �λ縻 ����ϱ�

#include <iostream>
#include <io.h>
#include <fcntl.h>

using namespace std;

int main()
{
	wchar_t message_korean[] = L"�ݰ��� �����!";		// �ѱ���
	/*
	wchar_t message_chinese[] = L"~";	// �߱���
	wchar_t message_japanese[] = L"~";	// �Ϻ���
	wchar_t message_russian[] = L"~";	// ���þƾ�
	*/

	cout << "Hello World!" << endl;

	_setmode(_fileno(stdout), _O_U16TEXT);	// ������ �ܼ� â �����ڵ� ���

	wcout << message_korean << endl;
	/*
	wcout << message_chinese << endl;
	wcout << message_japanese << endl;
	wcout << message_russian << endl;
	*/

	return 0;
}