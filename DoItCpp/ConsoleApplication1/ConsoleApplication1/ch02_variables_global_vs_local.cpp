// ���� ����, ���� ���� �����Ͽ� �����ϱ�

#include <iostream>
using namespace std;

int value = 1;	// ���� ����

int main() {

	int value = -1;	// ���� ����

	cout << value << endl;	// ���� ���� ���(-1)
	cout << ::value << endl;	// ���� ���� ���(1)

	return 0;
}