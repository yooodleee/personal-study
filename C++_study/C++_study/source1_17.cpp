#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

void Func(const char* str)
{
	cout << "const char*" << endl;
}

void Func(char* str)
{
	cout << "char*" << endl;
}

void Func(void* str)
{
	cout << "void*" << endl;
}

void Func(string str)
{
	cout << "string" << endl;
}

void main()
{
	Func("Hello World!");
}