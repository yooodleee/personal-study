// ó������ ���� ��� ���� �ޱ�

#include <iostream>
using namespace std;


int main() {

	try {

		int input;
		cout << "���� �� �ϳ��� �Է��غ����� : ";
		cin >> input;

		if (input > 0) {		// �Է¹��� ���ڰ� ����̸�
			
			cout << "throw 1" << endl;
			throw 1;		// ���� 1 �߻� (���� ���� ����)
			cout << "after trhow 1" << endl;
		}

		if (input < 0) {		// �Է¹��� ���ڰ� �����̸�

			cout << "trhow -1.0f" << endl;
			throw - 1.0f;	// ���� 1.0f �߻� (�ε� �Ҽ��� ���� ����)
			cout << "after throw -1.0f" << endl;
		}

		if (input == 0) {		// �Է¹��� ���ڰ� 0�̸�

			cout << "throw Z" << endl;
			throw 'Z';	// ���� Z �߻� (���� ���� ����)
		}
	}
	catch (int a) {		// ���� ���� ���� �ޱ�
		
		cout << "catch" << a << endl;
	}
	catch (...) {		// ó������ ���� ������ ���� ��� �ޱ�
		cout << "catch all" << endl;
	}

	return 0;
}

/*
���� �� �ϳ��� �Է��غ����� : 1
throw 1
catch1
*/

/*
���� �� �ϳ��� �Է��غ����� : -1
trhow -1.0f
catch all
*/

/*
���� �� �ϳ��� �Է��غ����� : 0
throw Z
catch all
*/