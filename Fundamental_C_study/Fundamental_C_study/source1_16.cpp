#include <stdio.h>
#include <iostream>
using namespace std;

void ToLower(std::string& str)
{
	bool bStartExtension = false;

	std::string::iterator it = str.begin();
	while (it != str.end())
	{
		// (1) 0과 양수만 처리하기 위해 unsigned char를 사용
		unsigned char c = *it;

		if (bStartExtension)
		{
			bStartExtension = false;
		}
		else
		{
			// (2) 128아래는 알파벳 및 기본문자이다.
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

	string str = "ABC가나다묭DEF";
	ToLower(str);
	cout << str.c_str() << endl;
}

// abc가나다묭def