// �湮�ϴ� �մ� ����ŭ �� �����

#include <iostream>
#include <string>


using namespace std;

int main() {

	int customer_num = 0;

	cout << "���� �湮 �մ�: ";
	cin >> customer_num;	// �մ� �� �Է�

	string* bread = new string[customer_num];	// �մ� ����ŭ string �迭 ����

	for (int i = 0; i < customer_num; i++)	// �Է¹��� �մ� ����ŭ �ݺ�
	{
		bread[i] = "��_" + to_string(i);		// '��_����' ���·� �迭�� ����
	}

	cout << endl << "--������ ��--" << endl;
	for (int i = 0; i < customer_num; i++)
	{
		cout << *(bread + i) << endl;	// ����� �� ���(������ ���� ����)
	}

	delete[] bread;	// string �迭 ����

	return 0;
}

/*
���� �湮 �մ�: 5

--������ ��--
��_0
��_1
��_2
��_3
��_4
*/