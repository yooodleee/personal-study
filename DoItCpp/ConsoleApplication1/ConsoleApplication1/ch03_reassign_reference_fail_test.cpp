// ���۷��� ������ �Ұ�

#include <iostream>
using namespace std;


int main() {

	int value = 10;
	int& ref_value = value;

	int value2 = 20;
	ref_value = value2;		// ���۷��� ������, �ǵ��� �ٸ��� ����

	cout << "value: " << value << endl;
	cout << "ref_value: " << ref_value << endl;

	return 0;
}

/*
value: 20
ref_value: 20
*/