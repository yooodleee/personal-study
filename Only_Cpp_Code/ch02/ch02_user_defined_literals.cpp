// ����� ���� ���ͷ��� �Ÿ� ���� ��ȯ�ϱ�

#include <iostream>
using namespace std;


const long double km_per_mile = 1.609344L;

long double operator"" _km(long double val)		// _km ����� ���ͷ� ����
{
	return val;	// �ƹ��� ��ȭ ���� �״�� ��ȯ
}

long double operator"" _mi(long double val)		// _mi ����� ���ͷ� ����
{
	return val * km_per_mile;	// ������ ų�ι��ͷ� ��ȯ�Ͽ� ��ȯ
}

int main() {
	long double distance_1 = 1.0_km;	// ų�κ��ʹ� �״�� ����
	long double distance_2 = 1.0_mi;	// ������ ų�ι��� ������ ��ȯ�ؼ� ����

	cout << distance_1 + distance_2 << "km" << endl;	// ų�ι��ͷ� ���

	return 0;
}

// 2.60934km