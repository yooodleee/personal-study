#include <stdio.h>
#include <iostream>
using namespace std;

void ToLower(std::string& str)
{
	bool bStartExtension = false;

	std::string::iterator it = str.begin();
	while (it != str.end())
	{
		// (1) 0�� ����� ó���ϱ� ���� unsigned char�� ���
		unsigned char c = *it;

		if (bStartExtension)
		{
			bStartExtension = false;
		}
		else
		{
			// (2) 128�Ʒ��� ���ĺ� �� �⺻�����̴�.
			if (c < 128 && !bStartExtension)
			{
				*it = tolower(c);
			}
			else
			{
				bStartExtension = true;
			}
		}

		it++;
	}
}

void main()
{
	using namespace std;

	string str = "ABC�����ْDDEF";
	ToLower(str);
	cout << str.c_str() << endl;
}

// abc�����ْDdef