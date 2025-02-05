// static 변수를 이용한 아이디 생성 함수 만들기

#include <iostream>
using namespace std;


int getNewID() {

	static int ID = 0;
	return ++ID;
}

int main() {

	cout << "ID : " << getNewID() << endl;
	cout << "ID : " << getNewID() << endl;
	cout << "ID : " << getNewID() << endl;
	cout << "ID : " << getNewID() << endl;
	cout << "ID : " << getNewID() << endl;

	return 0;
}

/*
ID : 1
ID : 2
ID : 3
ID : 4
ID : 5
*/