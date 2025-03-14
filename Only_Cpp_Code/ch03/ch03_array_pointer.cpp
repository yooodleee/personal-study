// 배열 원소의 주소와 포인터 연산의 결과 비교하기

/**
 * 포인터 연산으로 배열의 원소에 접근하기
 * 
 * 배열은 '포인터를 다루면서 배열과의 관계는 빼놓을 수 없다'고 할 정도로 배열의 인덱스로 각 원소에 
 * 접근하는 것처럼, 포인터 연산으로도 각 원소에 접근할 수 있다. 
 * 
 * 먼저, 배열 원소의 주소를 출력한 결과와 포인터 연산으로 출력한 결과를 비교해보도록 하자. 
 */

#include <iostream>
using namespace std;

int main() {

	int lotto[45] = {
		1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
		16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
		31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45
	};

	cout << "lotto[0] Address: " << &lotto[0] << endl;
	cout << "lotto[1] Address: " << &lotto[1] << endl;
	cout << "lotto[2] Address: " << &lotto[2] << endl;
	cout << "lotto[3] Address: " << &lotto[3] << endl;
	cout << "lotto[4] Address: " << &lotto[4] << endl;
	cout << "lotto[5] Address: " << &lotto[5] << endl << endl;

	cout << "(lotto + 0) Address: " << lotto + 0 << endl;	// 포인터 연산으로 배열 원소에 접근 
	cout << "(lotto + 1) Address: " << lotto + 1 << endl;
	cout << "(lotto + 2) Address: " << lotto + 2 << endl;
	cout << "(lotto + 3) Address: " << lotto + 3 << endl;
	cout << "(lotto + 4) Address: " << lotto + 4 << endl;
	cout << "(lotto + 5) Address: " << lotto + 5 << endl;

	return 0;
}

/*
lotto[0] Address: 000000498A9BF830
lotto[1] Address: 000000498A9BF834
lotto[2] Address: 000000498A9BF838
lotto[3] Address: 000000498A9BF83C
lotto[4] Address: 000000498A9BF840
lotto[5] Address: 000000498A9BF844

(lotto + 0) Address: 000000498A9BF830
(lotto + 1) Address: 000000498A9BF834
(lotto + 2) Address: 000000498A9BF838
(lotto + 3) Address: 000000498A9BF83C
(lotto + 4) Address: 000000498A9BF840
(lotto + 5) Address: 000000498A9BF844
*/

/**
 * 인덱스로 접근하나 포인터 연산으로 접근하나 결과가 같다는 것을 확인할 수 있다. 
 * 여기서 눈에 띄는 특징을 뽑으면 다음과 같다. 
 * 
 * 1. &lotto[0] == lotto + 0
 * 2. &배열_변수 [인덱스] == 배열_변수 + 인덱스
 * 
 * 이러한 특징이 성립하는 이유는 배열의 이름인 lotto가 첫 번째 원소의 주소 &lotto[0]를 가리키기 때문이다. 
 * 그리고, 포인터 연산에서 덧셈은 자료형의 크기를 곱한 만큼 덧셈을 수행한다. 예에서는 lotto가 int 형이므로
 * 덧셈할 숫자에 4byte 크기가 곱해진다. 따라서 주소가 4byte씩 늘어난다. 이 원리는 포인터의 사칙 연산과 
 * 증감 연산(++, --) 같은 단항 연산자에서도 같다. 
 */