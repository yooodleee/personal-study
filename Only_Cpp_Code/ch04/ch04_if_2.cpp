// if�� Ȱ���� ���� �б�(�߰�ȣ ����)

#include <iostream>
using namespace std;


int main() {

	int input_number;

	cout << "���� �Է� : ";
	cin >> input_number;

	if (input_number > 0)
		cout << "�Է��� ���� ��� �Դϴ�." << endl;
	else if (input_number < 0)
		cout << "�Է��� ���� ���� �Դϴ�." << endl;
	else
		cout << "�Է��� ���� 0 �Դϴ�." << endl;

	return 0;
}

/*
���� �Է� : -1
�Է��� ���� ���� �Դϴ�.
*/