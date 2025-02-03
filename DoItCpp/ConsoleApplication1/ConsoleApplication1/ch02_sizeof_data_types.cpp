// 정수형 크기 출력하기

#include <iostream>
using namespace std;

int main()
{
	cout << "short: " << sizeof(short) << "bytes" << endl;
	cout << "unsigned short: " << sizeof(unsigned short) << "bytes" << endl;
	cout << "int: " << sizeof(int) << "bytes" << endl;
	cout << "unsigned int: " << sizeof(unsigned int) << "bytes" << endl;

	// MS 전용
	cout << "__int8: " << sizeof(__int8) << "bytes" << endl;
	cout << "__int16: " << sizeof(__int16) << "bytes" << endl;
	cout << "__int32: " << sizeof(__int32) << "bytes" << endl;
	cout << "__int64: " << sizeof(__int64) << "bytes" << endl;

	cout << "long: " << sizeof(long) << "bytes" << endl;
	cout << "unsigned long: " << sizeof(unsigned long) << "bytes" << endl;
	cout << "long long: " << sizeof(long long) << "bytes" << endl;
	cout << "unsigned long long: " << sizeof(unsigned long long) << "bytes" << endl;

	return 0;
}

/*
short: 2bytes
unsigned short: 2bytes
int: 4bytes
unsigned int: 4bytes
__int8: 1bytes
__int16: 2bytes
__int32: 4bytes
__int64: 8bytes
long: 4bytes
unsigned long: 4bytes
long long: 8bytes
unsigned long long: 8bytes
*/

/*
1 byte == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)

# signed와 unsigned 정수 표현 범위 크기

1byte signed: -128 ~ 127
1byte unsigned: 0 ~ 255
2byte signed: 32,768 ~ 32,767
2byte unsigned: 0 ~ 65,535
4byte signed: -2,147,483,648 ~ 2,147,483,647
4byte unsigned: 0 ~ 4,294,967,295
8byte signed: -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
8byte unsigned: 0 ~ 18,446,744,073,709,551,615
*/