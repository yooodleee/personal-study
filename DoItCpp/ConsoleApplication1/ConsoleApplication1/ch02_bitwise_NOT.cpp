// ��Ʈ �����ڷ� 1�� ���� ���ϱ�

#include <iostream>
using namespace std;

int main() {

	unsigned int value = 0x00000000;	// 0�� 16����(hex)�� ǥ���� ��

	value = ~value;
	cout << hex << value << endl;

	return 0;
}

// ffffffff