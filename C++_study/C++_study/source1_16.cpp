#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

void ToLower(std::string& str)
{
	bool bStarExtension = false;

	std::string::iterator it = str.begin();
	while (it != str.end())
	{
		// (1) 0�� ����� ó���ϱ� ���Ͽ� unsigned char�� ���
		unsigned char c = *it;

		if (bStarExtension)
		{
			bStarExtension = false;
		}
		else
		{
			// (2) 128�Ʒ��� ���ĺ� �� �⺻ �����̴�.
			if (c < 128 && !bStarExtension)
			{
				*it = tolower(c);
			}
			else
			{
				bStarExtension = true;
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