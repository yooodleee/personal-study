// 구조체를 매개변수로 사용하기

/**
 * 구조체 만들기
 * 
 * 일반 변수, 포인터, 배열을 매개변수로 이용하는 방법을 알아보았다. 그런데 이 방법들은 모두 단일 자료형만
 * 취급할 뿐 여러 가지 형식의 데이터를 하나의 매개변수로 전달할 수는 없다. 이를 해결하는 방법의 하나로 
 * 구조체가 있다. 
 * 
 * 먼저 구조체가 무엇인지 알아보겠다. 
 * 예컨대, 어떤 사람의 정보를 코드로 표현한다면 다음처럼 구성할 수 있다. 만약 이런 정보를 함수로 전달하려면
 * 매개변수가 적어도 4개 필요하다. 게다가 관리해야 하는 사람이 많을 때는 최소 4개의 배열로 관리해야 한다. 
 * 
 * 사람의 정보를 나타내는 변수 선언
 * std::string name;	// 이름
 * int age;				// 나이
 * float height;		// 키
 * float weight;		// 몸무게
 * 
 * 이 데이터들을 묶어서 하나로 관리할 수 있다면 좋을 것 같다. 예컨대 '사람'이라는 이름으로 데이터를 그룹지어
 * 사용할 수 있다면 어떨까? 구조체를 이용하면 이처럼 여러 형식의 데이터들을 묶어서 관리할 수 있다. 
 * 다음은 struct 키워드를 이용해 Person이라는 이름으로 구조체를 선언한 예다. 
 * 
 * Person 구조체 선언
 * struct Person
 * {
 * 		std::string name;		// 이름
 * 		int age;				// 나이
 * 		float height;			// 키
 * 		float weight;			// 몸무게
 * };
 * 
 * 구조체는 하나 이상의 변수를 묶어 새로운 자료형으로 정의할 수 있다. 
 * Person 구조체는 자료형과 마찬가지로 형식만 정의된 형태이다. 해당 구조체 형식의 변수를 만들어야
 * 비로소 사용할 수 있다. 구조체 형식의 변수를 만드는 방법은 일반적인 변수 선언과 같다. 
 * 
 * 구조체 변수 선언
 * Person adult;
 * 
 * 이제 adult라는 이름으로 Person 형식의 변수가 생성되었다. adult 변수는 멤버 변수를 포함하는 전체 구조체를
 * 참조한다. 구조체 안의 개별적인 멤버에 접근하려면 멤버 선택 연산자(member selection operator)인 점(.)을
 * 이용해야 한다. 예컨대 이름 변수에 접근하려면 adult.name, 나이 변수에 접근하려면 adult.age처럼 . 연산자를
 * 사용해야 한다. 
 * 
 * 멤버 변수에 접근
 * Person adult;
 * adult.name = "Brain";
 * adult.age = 24;
 * adult.height = 180;
 * adult.weight = 70;
 * 
 * 구조체 형식으로 배열을 선언할 수도 있다. adult[인덱스]처럼 인덱스로 각각의 Person을 구분하고, 각 Person의
 * 정보가 담긴 멤버 변수는 .으로 접근할 수 있다. 
 * 
 * 구조체 배열 선언
 * Person adult[3];
 * 
 * adult[0].name = "Brain";
 * adult[0].age = 24;
 * adult[0].height = 180;
 * adult[0].weight = 70;
 * 
 * adult[1].name = "Jessica";
 * adult[1].age = 21;
 * adult[1].height = 165;
 * adult[1].weight = 55;
 * 
 * adult[2].name = "James";
 * adult[2].age = 25;
 * adult[2].height = 178;
 * adult[2].weight = 80;
 * 
 * 
 * 이제 구조체를 함수의 매개변수로 사용하는 예를 보겠다. 앞서 본 Person 구조체를 그대로 사용하되, 나이는 
 * 25세 이상인 사람의 정보만 화면에 출력하는 프로그램이다. 
 */

#include <iostream>
using namespace std;


struct Person
{
	std::string name;	// 이름
	int age;			// 나이
	float height;		// 키
	float weight;		// 몸무게게
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
	check_age(adult, 3);	// adult => 구조체 배열의 시작 주소 전달 


	return 0;
}

/*
name : James
age : 30
height : 170
weight : 65
*/

/**
 * 이처럼 구조체를 사용하면 관련 값을 하나의 객체로 그룹화하므로 코드를 더 읽기 쉽고 유지관리하기 
 * 좋게 만들 수 있다. 함수에 전달할 인자가 많을 때 특히 유용하다. 
 * 
 * 그런데 구조체를 함수에 전달하면 복사본이 전달되므로 구조체가 매우 크면 성능 문제가 발생할 수 있다. 
 * 이때는 복사본 대신 구조체에 대한 포인터(주소)를 전달하면 해결할 수 있다. 따라서 앞의 예에서는 check_age 함수의 
 * 첫 번째 매개변수를 Person *_adult처럼 구조체 포인터 변수를 선언하고, main에서 호출할 때는 구조체 배열의 이름인
 * adult를 전달했다. 즉, 구조체 배열의 시작 주소를 전달했다. 
 */