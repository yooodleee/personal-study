// new, delete�� �迭 ������ ���� �޸� �Ҵ��ϰ� �����ϱ�

#include <iostream>
using namespace std;

int main() {

	int* pt_int_array_value = new int[5];	// ���� �޸� �Ҵ�(�迭)

	for (int i = 0; i < 5; i++)
	{
		pt_int_array_value[i] = i;	// �Ҵ�� �迭 ������ 0~4���� ������� �ֱ�
	}

	for (int i = 0; i < 5; i++)
	{
		cout << pt_int_array_value[i] << endl;	// �迭 ���� ���
	}

	delete[] pt_int_array_value;	// ���� �޸� ����(�迭)

	return 0;
}