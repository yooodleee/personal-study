// switch�� Ȱ���� ���� �б�

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
		break;
	case2:
		cout << "�Է��� ���� 2 �Դϴ�." << endl;
		break;
	case3:
		cout << "�Է��� ���� 3 �Դϴ�." << endl;
		break;
	case4:
		cout << "�Է��� ���� 4 �Դϴ�." << endl;
		break;
	case5:
		cout << "�Է��� ���� 5 �Դϴ�." << endl;
		break;
	default:
		cout << "�Է��� ���� 1 ~ 5 ������ ���� ���� �����Դϴ�." << endl;
		break;
	}

	return 0;
}

/*
1 ~ 5 ������ ���� �Է� : 7
�Է��� ���� 1 ~ 5 ������ ���� ���� �����Դϴ�.
*/