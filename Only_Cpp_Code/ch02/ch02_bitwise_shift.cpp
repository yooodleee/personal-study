// ����Ʈ �����ϱ�

#include <iostream>
#include <bitset>

using namespace std;

int main() {

	int a = 13;
	int b = a >> 1;	// 1bit ���������� ����Ʈ
	int c = a << 1;	// 1bit �������� ����Ʈ
	int d = a >> -1;	// ����Ʈ ���� ����(warning C4293)
	int e = a << 32;	// ����Ʈ ���� ����(warning C4293)

	cout << "a = " << bitset<8>(a) << " : " << a << endl;
	cout << "b = " << bitset<8>(b) << " : " << b << endl;
	cout << "c = " << bitset<8>(c) << " : " << c << endl;
	cout << "d = " << bitset<8>(d) << " : " << d << endl;
	cout << "e = " << bitset<8>(e) << " : " << e << endl;

	return 0;
}

/*
a = 00001101 : 13
b = 00000110 : 6
c = 00011010 : 26
d = 00000000 : 0
e = 00001101 : 13
*/