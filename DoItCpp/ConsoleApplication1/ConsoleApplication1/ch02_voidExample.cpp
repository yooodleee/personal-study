#include <iostream>
using namespace std;

void printfunc()		// �Լ��� ���� ��ȯ���� ���� ��
{
	std::cout << "func" << std::endl;
}

int input_func(void)
{
	int input_value;

	int int_value;
	/*
	* ��� �ڷ����� ����ų �� �ִ� ���׸� �����ͷ� ����� ��
	* 
	float float_value;
	void* ptr_value;
	
	ptr_value = &int_value;
	ptr_value = &float_value;
	*/

	std::cin >> input_value;
	
	return input_value;
}