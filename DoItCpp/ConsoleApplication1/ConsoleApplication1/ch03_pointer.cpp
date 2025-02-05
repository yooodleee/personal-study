// ������ �����ڷ� ������ ����

#include <iostream>
using namespace std;

int main() {

	char char_value = 'A';
	int int_value = 123;
	double double_value = 123.456;

	char* char_pointer_value = &char_value;
	int* int_pointer_value = &int_value;
	double* double_pointer_value = &double_value;

	// �Ϲ� ������ ������ ���
	cout << "char_value: " << char_value << endl;
	cout << "int_value: " << int_value << endl;
	cout << "double_value: " << double_value << endl;
	cout << endl;

	// ������ �����ڷ� ������ ������ ����Ű�� ������ ���
	cout << "char_pointer_value: " << char_pointer_value << endl;
	cout << "int_pointer_value: " << int_pointer_value << endl;
	cout << "double_pointer_value: " << double_pointer_value << endl;
	cout << endl;

	// ������ �����ڷ� ���� ������ ���� ����
	*char_pointer_value = 'Z';
	*int_pointer_value = 321;
	*double_pointer_value = 654.321;

	// �Ϲ� ������ ������ ���(������Ʈ Ȯ��)
	cout << "char_value: " << char_value << endl;
	cout << "int_value: " << int_value << endl;
	cout << "double_value : " << double_value << endl;

	return 0;
}

/*
char_value: A
int_value: 123
double_value: 123.456

char_pointer_value: A������������������������������?
int_pointer_value: 0000001EAA19FC04
double_pointer_value: 0000001EAA19FC28

char_value: Z
int_value: 321
double_value : 654.321
*/