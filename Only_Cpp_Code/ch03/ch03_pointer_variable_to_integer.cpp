// ������ ���� ��ü�� ���ȭ

#include <iostream>
using namespace std;


int main()
{
	int a = 0;
	int b = 1;
	int* const ptr = &a;	// ptr�� ���ȭ

	a = 1;	// ������ ���
	ptr = &b;	// ������ ���� �߻�

	return 0;
}

/*
�ɰ���	�ڵ�	����	������Ʈ	����	��	��ǥ�� ����(Suppression) ����	���� ����
����(Ȱ��)	E0137	���� ������ �� �ִ� lvalue���� �մϴ�.	
*/