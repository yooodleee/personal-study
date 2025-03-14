// 배열과 포인터가 같은지 확인하기 

/**
 * 배열과 포인터는 같을까?
 * 
 * 배열 변수가 가리키는 주소는 배열의 첫 번째 원소의 주소이기도 하고, 배열 인덱스와 포인터 연산이
 * 같아서 배열과 포인터가 같다고 생각할 수 있다. 하지만 이 둘은 엄연히 다르다. 다음의 예를 통해 
 * 확인해보자. 
 */

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

/**
 * array와 pointer_array가 같은 주소를 가리키고 있지만, sizeof로 크기를 확인해보면
 * 완전히 다른 것을 확인할 수 있다. array는 int[5] 형식이고, pointer_array는 int* 형이기
 * 때문이다. 따라서 array의 sizeof는 배열 전체 크기인 20byte (4byte x 5)가 출력됐고,
 * pointer_array는 포인터 변수의 크기인 8byte가 출력됐다. 
 * 
 * 이처럼 배열과 포인터는 다르지만, 배열의 이름을 사용할 때 자동으로 첫 번째 원소를 가리키는
 * 포인터가 되므로 마치 배열과 포인터가 같다고 생각할 수 있다. 
 * 
 * 배열과 포인터의 관계에서 핵심은 배열의 원소에 접근할 때 포인터 연산으로도 가능하다는 것이다. 
 */