#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void main()
{
	string str = "ABC°¡³ª´Ù’DEDF";
	transform(str.begin(), str.end(), str.begin(), tolower);
	cout << str.c_str() << endl;

}