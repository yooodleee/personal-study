// ���� ó��

#include <iostream>
using namespace std;


int main() {
	try
	{
		int input;
		cout << "���� �� �ϳ��� �Է��ϼ��� : ";
		cin >> input;

		if (input > 0)	// �Է¹��� ���ڰ� ����̸�
		{
			cout << "throw 1" << endl;
			throw 1;	// ���� 1 �߻� (���� ���� ����)
			cout << "after throw 1" << endl;
		}

		if (input < 0)	// �Է¹��� ���ڰ� �����̐�
		{
			cout << "throw-1.0f" << endl;
			throw - 1.0f;	// ���� 1.0f �߻� (�ε��Ҽ��� ���� ����)
			cout << "after -1.0f" << endl;
		}

		if (input == 0)	// �Է¹��� ���ڰ� 0�̸�
		{
			cout << "throw Z" << endl;
			throw 'Z';	// ���� Z �߻� (���� ���� ����)
			cout << "after throw Z" << endl;
		}
	}
	catch (int a)	// ���� ���� ���� �ޱ�
	{
		cout << "catch" << a << endl;
	}
	catch (float b)	// �ε��Ҽ��� ���� ���� �ޱ�
	{
		cout << "catch" << b << endl;
	}
	catch (char c)	// ���� ���� ���� �ޱ�
	{
		cout << "catch" << c << endl;
	}

	return 0;
}

/*
���� �� �ϳ��� �Է��ϼ��� : -6
throw-1.0f
catch-1
*/

/*
���� �� �ϳ��� �Է��ϼ��� : 1
throw 1
catch1
*/

/*
���� �� �ϳ��� �Է��ϼ��� : 0
throw Z
catchZ
*/