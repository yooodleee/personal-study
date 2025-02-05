// static 키워드로 지역 변수를 정적 변수로 만들기

#include <iostream>
using namespace std;


void func() {

	int a = 10;
	static int b = 10;

	a++;
	b++;

	cout << "a : " << a << " , b : " << b << endl;
}

int main()
{
	func();
	func();
	func();
	func();
	func();

	return 0;
}

/*
a : 11 , b : 11
a : 11 , b : 12
a : 11 , b : 13
a : 11 , b : 14
a : 11 , b : 15
*/