#include <stdio.h>
#include <iostream>
using namespace std;

bool HasFinalConsonant(wchar_t Letter)
{
	if (Letter >= 0xAC00 && Letter <= 0xD7A3)	// (1) �ѱ� �ϼ��� Ȯ��
	{
		if ((Letter - 0xAC00) % 28 == 0)	// (2) ��ħ ���� ���� Ȯ��
		{
			return true;
		}
	}

	return false;
}

void main()
{
	if (HasFinalConsonant(L'��'))
	{
		cout << "�� - ��ħ ����" << endl;
	}

	if (HasFinalConsonant(L'��'))
	{
		cout << "�� - ��ħ ����" << endl;
	}
}