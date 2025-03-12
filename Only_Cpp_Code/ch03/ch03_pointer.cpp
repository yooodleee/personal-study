// 역참조 연산자로 데이터 접근

/**
 * 포인터와 연산자
 * 
 * 포인터는 메모리 주소를 저장하는 변수를 의미한다. 
 * 포인터 변수도 일반 변수를 선언할 때처럼 int나 char와 같은 자료형을 지정한다. 
 * 다만 다음처럼 자료형과 변수 이름 사이에 *를 추가한다. 
 * 
 * 자료형 *(포인터_변수_이름)
 */

/**포인터 변수 선언과 주소 대입하기
 * 
 * 포인터 변수를 선언하는 코드를 살펴보자. 
 * 다음은 일반 변수 3개와 포인터 변수 3개를 선언하는데, 포인터 변수에는 일반 변수의 주소를 넣었다. 
 * 
 * #include <iostream> 
 * 
 * int main()
 * {
 * 		char char_value = 'A';
 * 		int int_value = 123;
 * 		double double_value = 123.456;
 * 
 * 		char *char_pointer_value = &char_value;
 * 		int *int_pointer_value = &int_value;
 * 		double *double_pointer_value = &double_value;
 * 
 * 		return 0;
 * }
 * 
 * 포인터 변수를 선언하면서 일반 변수로 선언된 char_value, int_value, double_value의 메모리 주소를
 * 각각의 포인터 변수에 넣었다. 이때 일반 변수 앞에 붙은 &은 피연산자의 주소를 읽어 오는 주소 연산자이다. 
 */

/**포인터 변수의 크기
 * 
 * 포인터 변수의 크기는 데이터 형식과는 관련이 없다. 따라서 모든 포인터 변수의 크기는 같다. 
 * 포인터 변수는 메모리 주소를 저장하는 데에 사용되며, 주소의 크기는 시스템 아키텍쳐에 따라 
 * 결정된다. 따라서 데이터 형식이나 변수의 크기와는 관계가 없다. 
 * 
 * 그런데도 포인터 변수를 선언할 때 데이터 형식을 지정하는 이유는 해당 포인터가 가리키는 데이터의 형식을 
 * 명시하기 위함이다. 
 * 
 * 		int *ptr;		// int 형 데이터를 가리키는 포인터
 * 		double *ptr2;	// double 형 데이터를 가리키는 포인터
 * 
 * 이처럼 포인터 선언문에 지정한 데이터 형식으로, 해당 포인터가 가리키는 데이터의 크기와 해석 방법이 결정된다. 
 * 이러한 개념은 포인터를 대상으로 연산할 때에 필요하다. 또한 포인터를 사용하는 코드에서 데이터 형식의 일관성을
 * 유지하고 오류를 방지하는 데에 도움이 되기도 한다. 
 */

/**포인터 변수가 가리키는 데이터에 접근하기
 * 
 * 이번에는 포인터 변수에 저장된 주소를 이용해 데이터에 접근하는 방법을 알아보자. 
 * 포인터 변수에 역참조 연산자*를 사용하면 해당 포인터 변수에 저장된 주소가 가리키는 데이터에 접근할 수 있다. 
 * 실제 다음 코드를 살펴보자. 
 */

#include <iostream>
using namespace std;

int main() {

	// 일반 변수 선언
	char char_value = 'A';
	int int_value = 123;
	double double_value = 123.456;

	// 포인터 변수 선언 
	char* char_pointer_value = &char_value;
	int* int_pointer_value = &int_value;
	double* double_pointer_value = &double_value;

	// 일반 변수의 데이터 출력
	cout << "char_value: " << char_value << endl;
	cout << "int_value: " << int_value << endl;
	cout << "double_value: " << double_value << endl;
	cout << endl;

	// 역참조 연산자로 포인터 변수가 가리키는 데이터 출력
	cout << "char_pointer_value: " << char_pointer_value << endl;
	cout << "int_pointer_value: " << int_pointer_value << endl;
	cout << "double_pointer_value: " << double_pointer_value << endl;
	cout << endl;

	// 역참조 연산자로 원본 데이터 덮어쓰기 
	*char_pointer_value = 'Z';
	*int_pointer_value = 321;
	*double_pointer_value = 654.321;

	// 일반 변수의 데이터 출력(업데이트 확인)
	cout << "char_value: " << char_value << endl;
	cout << "int_value: " << int_value << endl;
	cout << "double_value : " << double_value << endl;

	return 0;
}

/*
실행 결과

char_value: A
int_value: 123
double_value: 123.456

*char_pointer_value: A
*int_pointer_value: 123
*double_pointer_value: 123.456

char_value: Z
int_value: 321
double_value : 654.321
*/


/**
 * 실행 결과를 보면 포인터 변수 앞에 역참조 연산자 *를 사용해 포인터 변수가 가리키는
 * 데이터에 직접 접근하는 것을 확인할 수 있다. 심지어 *char_pointer_value = 'Z' 처럼
 * 새로운 값을 넣으면 char_value 변수의 값이 'Z'로 바뀌는 것도 볼 수 있다. 
 */