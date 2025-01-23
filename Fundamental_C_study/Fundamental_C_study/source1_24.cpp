#include <stdio.h>
#include <iostream>
#include <typeinfo>
using namespace std;

int GetValue()
{
	int a = 1;
	return a;
}

int& getReference()
{
	int a = 2;
	return a;
}

void Func(int& arg)					// (A)
{
	cout << "Lvalue" << endl;
}

void Func(int&& arg)				// (B)
{
	cout << "Rvalue" << endl;
}

void main()
{
	Func(1);					// (1) RValue Reference

	int a = 1;
	Func(a);					// (2) LValue Reference

	Func(GetValue());			// (3) Rvalue Reference
	Func(getReference());		// (40 LValue Reference
}

//Rvalue
//Lvalue
//Rvalue
//Lvalue