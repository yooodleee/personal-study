#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

void main()
{
	string str = "ABC가나다묭EDF";
	transform(str.begin(), str.end(), str.begin(), tolower);
	cout << str.c_str() << endl;
}

//abc가나다뭗edf