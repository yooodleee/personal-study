// �Ͻ��� �� ��ȯ

#include <iostream>
using namespace std;

int main() {
	float float_value = 1.5f;	// ���� �����ʹ� �ε� �Ҽ��� �� 1.5

	double double_value = float_value;	// ���� �°�: ������ ���� ����
	int int_value = float_value;		// ���� ��ȯ: ������ ���� �߻�

	cout << "float_value: " << float_value << endl;
	cout << "double_value: " << double_value << endl;
	cout << "int_value: " << int_value << endl;

	return 0;
}

/*
float_value: 1.5
double_value: 1.5
int_value: 1
*/