// ���� ������ ����� ����

#include <iostream>
using namespace std;

void print() {
	// �Լ� ������ ���� ����
	int value = 10;
	cout << "print �Լ� ���ο����� ���� ���� value: " << value << endl;
}

int main() {
	// main �Լ� ������ ���� ����
	int value = 5;
	cout << "main �Լ� ���ο����� ���� �м� value: " << value << endl;

	
	// print �Լ� ȣ��
	print();
	// print �Լ� ȣ�� �Ŀ��� main �Լ��� value�� ������ ���� ����
	cout << "�ٽ� main �Լ� ���ο����� ���� ���� value: " << value << endl;

	return 0;
}

/*
main �Լ� ���ο����� ���� �м� value: 5
print �Լ� ���ο����� ���� ���� value: 10
�ٽ� main �Լ� ���ο����� ���� ���� value: 5
*/