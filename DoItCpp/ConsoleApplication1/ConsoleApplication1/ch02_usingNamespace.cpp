// using namespace 이용하기

#include <iostream>	
using namespace std;	// 네임스페이스 사용 선언

int main()
{
	int i, j;

	cout << "Enter num_1: ";
	cin >> i;

	cout << "Enter num_2: ";
	cin >> j;

	cout << "num_1 + num_2 = " << i + j << endl;

	return 0;
}