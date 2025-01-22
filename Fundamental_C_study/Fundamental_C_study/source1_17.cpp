#include <stdio.h>
#include <iostream>
using namespace std;

void Func(const char* str)				// (1)
{
	cout << "const char" << endl;
}

void Func(char* str)					// (2)
{
	cout << "char*" << endl;
}

void Func(void* str)					// (3)
{
	cout << "void" << endl;
}

void Func(string str)					// (4)
{
	cout << "string" << endl;
}

void main()
{
	Func("Hello World!");
}