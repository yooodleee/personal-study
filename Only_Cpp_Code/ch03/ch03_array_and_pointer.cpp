// 배열과 포인터가 같은지 확인하기

#include <iostream>
using namespace std;

int main() {

	int array[5] = { 1, 2, 3, 4, 5 };
	int* pointer_array = array;

	cout << "array: " << array << endl;
	cout << "pointer_array: " << pointer_array << endl << endl;

	cout << "sizeof(array): " << sizeof(array) << endl;
	cout << "sizeof(pointer_array): " << sizeof(pointer_array) << endl;

	return 0;
}

/*
array: 00000067FC78F608
pointer_array: 00000067FC78F608

sizeof(array): 20
sizeof(pointer_array): 8
*/