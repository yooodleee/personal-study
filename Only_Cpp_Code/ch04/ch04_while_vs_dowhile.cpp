// while, do ~ while ������

#include <iostream>
using namespace std;


int main() {

	int i = 0;
	
	while (i < 0) {	// ���ǽ��� �����̹Ƿ� �ݺ����� ���� ������� �ʴ´�.
		cout << "i is less than 0" << endl;
		i++;
	}

	int j = 0;

	do {
		cout << "j is less than 0" << endl;
		j++;
	} while (j < 0);	// ���ǽ��� ���������� �ݺ����� 1ȸ ����ȴ�.


	return 0;
}

// j is less than 0