// ���� ó�� ���п� �����ϱ�

#include <iostream>
#include <cstdlib>

using namespace std;


// ���� ó�� �Լ�
void myterminate() {

	cout << "myterminate called" << endl;
	exit(-1);		// ���α׷��� ���������� ����
}

int main() {

	set_terminate(myterminate);		// ���� ó�� �Լ� ����
	throw 1;		// ���� �߻�

	return 0;		// throw�� ���ܸ� �������Ƿ� ������� ����
}