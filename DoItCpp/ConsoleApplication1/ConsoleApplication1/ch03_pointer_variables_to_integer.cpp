// ������ ������ ����Ű�� ���� ���ȭ

#include <iostream>
using namespace std;


int main() {

	int a = 0;
	const int* ptr = &a;	// *ptr�� ���ȭ

	a = 1;	// ������ ���
	*ptr = 2;	// ������ ���� �߻�

	return 0;
}

/*
�ɰ���	�ڵ�	����	������Ʈ	����	��	��ǥ�� ����(Suppression) ����	���� ����
����(Ȱ��)	E0137	���� ������ �� �ִ� lvalue���� �մϴ�.	
*/