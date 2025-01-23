#include <stdio.h>
#include <iostream>
#include <typeinfo>
using namespace std;

void main()
{
	/*
	push ebp
	mov ebp, esp
	sub esp, 10h					// (1)
	*/

	int a = 1;
	int& ra = a;
	/*
	mov  dword ptr [ebp-0Ch], 1		// (2)
	lea  eax, [ebp-0Ch]
	mov dword ptr [ebp-10h], eax	// (3) ra
	*/

	const int& rc = 2;
	/*
	mov  dword ptr [ebp-4], 2		// (4) Temp
	lea  ecx, [ebp-4]
	mov  dword ptr [ebp-8], ecx		// (5) rc
	*/
}