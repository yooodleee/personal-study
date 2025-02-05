// ������ ������ �Ű������� ����ϱ�

#include <iostream>
using namespace std;

void change_negative(int* _val)	// ������ ������ �Ű������� ���
{
	if (*_val > 0)
	{
		*_val = -(*_val);	// _val�� ����Ű�� ���� ����̸� ������ ����
	}
}

int main() {

	int a = 3, b = -3;

	cout << "a : " << a << endl;
	cout << "b : " << b << endl;

	change_negative(&a);	// a ������ �ּڰ��� ����
	change_negative(&b);	// b ������ �ּڰ��� ����

	cout << "change_negative(a) : " << a << endl;
	cout << "change_negative(b) : " << b << endl;

	return 0;
}

/*
a : 3
b : -3
change_negative(a) : -3
change_negative(b) : -3
*/