// ���ܰ� ���޵Ǵ� ���� Ȯ���ϱ�

#include <iostream>
using namespace std;


void func_throw() {

	cout << "func_throw()" << endl;
	cout << "throw -1" << endl;

	throw - 1;	// ���� ���� ���� ������
	cout << "after throw - 1" << endl;
}

int main() {

	try {
		func_throw();
	}

	catch (int exec) {		// ���� ���� ���� �ޱ�

		cout << "catch " << exec << endl;
	}

	return 0;
}

/*
func_throw()
throw -1
catch -1
*/