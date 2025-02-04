// ���� ������, ����/���� ���� ���ϱ�

#include <iostream>
using namespace std;

int main() {
	
	int a = 0;	// a ���� �� 0
	int b = 0;	// b ���� �� 0
	int a_prefix;
	int b_postfix;

	a_prefix = ++a;	// ���� ����(a���� 1��ŭ ������Ų �Ŀ� a_prefix�� ����)
	b_postfix = b++;	// ���� ����(b���� b_postfix�� ������ �Ŀ� b���� 1��ŭ ����)

	cout << "a = " << a << ", " << "a_prefix = " << a_prefix << endl;
	cout << "b = " << b << ", " << "b_postfix = " << b_postfix << endl;

	return 0;
}

/*
a = 1, a_prefix = 1
b = 1, b_postfix = 0
*/