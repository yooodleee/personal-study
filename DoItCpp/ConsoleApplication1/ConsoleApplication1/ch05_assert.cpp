// assert�� �̿��� ���� ó��

#include <iostream>
#include <cassert>

using namespace std;


void print_number(int* _pt_int) {

	assert(_pt_int != NULL);	// ����� ��忡�� _pt_int�� ������ �˻�
	cout << *_pt_int << endl;
}

int main() {

	int a = 100;
	int* b = NULL;
	int* c = NULL;

	b = &a;
	print_number(b);

	// c�� NULL�� ���·� ���� ����
	print_number(c);


	return 0;
}

/*
100
Assertion failed: _pt_int != NULL
*/