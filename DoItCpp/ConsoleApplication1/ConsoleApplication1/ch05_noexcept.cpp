// noexcept�� ��õ� �Լ����� ���� ������

#include <iostream>
using namespace std;


void real_noexcept() noexcept	// ���ܸ� ������ ������ ���
{

	cout << "real_noexcept" << endl;
}

// noexcept�� ��õ� �Լ� �ȿ��� ���� �߻�
void fake_noexcept() noexcept {

	cout << "fake_noexcept" << endl;
	throw 1;	// ���� ���� ���� �߻�
}

int main() {

	real_noexcept();

	try {

		fake_noexcept();
	}
	catch (int exec) {

		cout << "catch" << exec << endl;
	}

	return 0;
}

/*
(���μ��� 30884)��(��) 3 �ڵ�(0x3)�� �Բ� ����Ǿ����ϴ�.
������� ������ �� �ܼ��� �ڵ����� �������� [����] -> [�ɼ�] -> [�����] > [������� �����Ǹ� �ڵ����� �ܼ� �ݱ�]�� ����ϵ��� �����մϴ�.
�� â�� �������� �ƹ� Ű�� ��������...
*/