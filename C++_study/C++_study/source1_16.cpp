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
		// (1) 0과 양수만 처리하기 위하여 unsigned char를 사용
		unsigned char c = *it;

		if (bStarExtension)
		{
			bStarExtension = false;
		}
		else
		{
			// (2) 128아래는 알파벳 및 기본 문자이다.
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

	string str = "ABC가나다묭DEF";
	ToLower(str);
	cout << str.c_str() << endl;
}