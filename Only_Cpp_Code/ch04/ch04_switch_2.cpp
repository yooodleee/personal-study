// switch�� Ȱ���� ���� �б�(break ����)

#include <iostream>
using namespace std;


int main() {

	int input_number;

	cout << "1 ~ 5 ������ ���� �Է� : ";
	cin >> input_number;


	switch (input_number)
	{
	case1:
		cout << "�Է��� ���� 1 �Դϴ�." << endl;
	case2:
		cout << "�Է��� ���� 2 �Դϴ�." << endl;
	case3:
		cout << "�Է��� ���� 3 �Դϴ�." << endl;
	case4:
		cout << "�Է��� ���� 4 �Դϴ�." << endl;
	case5:
		cout << "�Է��� ���� 5 �Դϴ�." << endl;
	default:
		cout << "�Է��� ���� 1 ~ 5 ������ ���� ���Դϴ�." << endl;
	}

	return 0;
}