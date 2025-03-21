// 구조체를 매개변수로 사용하기

#include <iostream>
using namespace std;


struct Person
{
	std::string name;	// 이름
	int age;			// 나이
	float height;		// 키
	float weight;		// 몸무게
};


void check_age(Person* _adult, int _count)
{
	for (int i = 0; i < _count; i++)
	{
		if (_adult[i].age >= 25)
		{
			cout << "name : " << _adult[i].name << endl;
			cout << "age : " << _adult[i].age << endl;
			cout << "height : " << _adult[i].height << endl;
			cout << "weight : " << _adult[i].weight << endl;
		}
	}
}


int main() {

	Person adult[3] =
	{
		{"Brain", 24, 180, 70},
		{"Jessica", 22, 165, 55},
		{"James", 30, 170, 65},
	};
	check_age(adult, 3);	// 구조체 배열의 시작 주소 전달(adult)


	return 0;
}

/*
name : James
age : 30
height : 170
weight : 65
*/