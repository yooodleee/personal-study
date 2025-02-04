#include <iostream>
using namespace std;

void printfunc()		// 함수가 값을 반환하지 않을 때
{
	std::cout << "func" << std::endl;
}

int input_func(void)
{
	int input_value;

	int int_value;
	/*
	* 모든 자료형을 가리킬 수 있는 제네릭 포인터로 사용할 때
	* 
	float float_value;
	void* ptr_value;
	
	ptr_value = &int_value;
	ptr_value = &float_value;
	*/

	std::cin >> input_value;
	
	return input_value;
}