// if ���ǹ����� �б��ϱ�

#include <iostream>
using namespace std;

int main() {

	int a = 7;
	int b = 5;
	int result;

	if (a > b)
		return a;	// a > b�� true -> result�� a�� ����
	else
		return b;	// a > b�� false -> result�� b�� ����

	cout << "result = " << result << endl;

	return 0;
}