// 다중 포인터 선언

#include <iostream>

int main() {

	int int_value = 123;

	int* int_pt_value = &int_value;
	int** int_pt_pt_value = &int_pt_value;
	int*** int_pt_pt_pt_value = &int_pt_pt_value;

	return 0;
}