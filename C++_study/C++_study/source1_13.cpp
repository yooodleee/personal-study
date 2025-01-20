#include <stdio.h>
#include <iostream>
using namespace std;

bool HasFinalConsonant(wchar_t Letter)
{
	if (Letter >= 0xAC00 && Letter <= 0xD7A3)	// (1) 한글 완성형 확인
	{
		if ((Letter - 0xAC00) % 28 == 0)	// (2) 받침 없는 글자 확인
		{
			return true;
		}
	}

	return false;
}

void main()
{
	if (HasFinalConsonant(L'왕'))
	{
		cout << "왕 - 받침 없음" << endl;
	}

	if (HasFinalConsonant(L'주'))
	{
		cout << "주 - 받침 없음" << endl;
	}
}