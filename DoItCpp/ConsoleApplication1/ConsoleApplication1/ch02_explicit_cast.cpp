// �Ͻ��� �� ��ȯ�� ����� �� ��ȯ ��
#include <iostream>
using namespace std;

int main() {
	
	int int_a = 10;
	int int_b = 5;

	int int_avg = (int_a + int_b) / 2;
	float float_avg_1 = (int_a + int_b) / 2;	// �Ͻ����� ��ȯ: ������ ����
	float float_avg_2 = float(int_a + int_b) / 2;	// ����� ����ȯ

	cout << "int_avg: " << int_avg << endl;
	cout << "float_avg_a: " << float_avg_1 << endl;
	cout << "float_avg_b: " << float_avg_2 << endl;

	return 0;
}

/*
int_avg: 7
float_avg_a: 7
float_avg_b: 7.5
*/