// �Ű������� �Ϲ� ������ ����

#include <iostream>
using namespace std;


void swap(int a, int b)
{
	// swap �Լ� �� ��ȯ �� a, b ��
	cout << "[swap func] before swap, a: " << a << " b: " << b << endl;

	int temp = a;
	a = b;
	b = temp;

	// swap �Լ� �� ��ȯ �� a, b ��
	cout << "[swap func] after swap, a: " << a << " b: " << b << endl;
}


int main()
{
	int a = 15, b = 10;

	// swap �Լ� ȣ�� �� a, b ��
	cout << "[main] before swap, a: " << a << " b: " << b << endl << endl;

	swap(a, b);

	// swap �Լ� ȣ�� �� a, b ��
	cout << "[main] after swap, a: " << a << " b: " << b << endl;

	return 0;
}

/*
[main] before swap, a: 15 b: 10

[swap func] before swap, a: 15 b: 10
[swap func] after swap, a: 10 b: 15
[main] after swap, a: 15 b: 10
*/