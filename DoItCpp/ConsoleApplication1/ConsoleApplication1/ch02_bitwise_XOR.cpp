// 비트 XOR 연산하기

#include <iostream>
#include <bitset>

using namespace std;

int main() {

	int a = 13;
	int b = 27;
	int c = a ^ b;	// 비트 XOR 연산

	cout << "a = " << bitset<8>(a) << " : " << a << endl;
	cout << "b = " << bitset<8>(b) << " : " << b << endl;
	cout << "c = " << bitset<8>(c) << " : " << c << endl;

	return 0;
}

/*
a = 00001101 : 13
b = 00011011 : 27
c = 00010110 : 22
*/