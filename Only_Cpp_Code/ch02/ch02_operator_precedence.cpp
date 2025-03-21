// 연산자의 우선순위 확인하기

/**
 * 연산자 우선순위
 * 
 * 연산자 우선순위는 연산자를 여러 개 사용할 때, 또는 연산자 위치에 따라 연산 순서를 나타낸다. 
 * C++ 언어의 연산자 우선순위는 다음과 같다. 
 * 
 * 
 * 1. :: => 범위 지정 연산자
 * 
 * 2. a++, a-- => 변수의 값을 먼저 반환한 후 증가 또는 감소
 * 	  type(), type() => 형 변환
 * 	  a() => 함수 호출
 * 	  a[] => 배열 요소 접근
 * 	  ., -> => 멤버 접근
 * 
 * 3. ++a, --a => 변수의 값을 증가 또는 감소시킨 후 반환 
 * 	  +a, -a => 양수 또는 음수 반환 
 * 	  !, ~ => 논리 NOT과 비트 NOT 연산자
 * 	  (type) => C 스타일 형 변환
 * 	  *a => 포인터 변수 a가 가리키는 메모리에 있는 값 반환
 * 	  &a => 변수 a의 주소 반환
 * 	  sizeof => 피연산자의 크기 반환
 * 	  co_await => 대기 표현식 사용(C++20부터)
 * 	  new, new[] => 동적 메모리 할당
 * 	  delete, delete[] => 동적으로 할당한 메모리 해제
 * 
 * 4. .*, ->* => 멤버 포인터를 통한 멤버 접근
 * 
 * 5. a*b, a/b, a%b => 곱셈, 나눗셈, 나머지 연산
 * 
 * 6. a+b, a-b => 덧셈과 뺄셈 연산
 * 
 * 7. <<, >> => 비트 단위로 왼쪽 또는 오른쪽으로 시프트
 * 
 * 8. <=> => 세 가지 비교 연산자를 비교한 비교(C++20부터)
 * 
 * 9. <, <=, >, >= => 등호를 사용한 관계 비교 
 * 
 * 10. ==, != => 등호와 부등호를 사용한 비교 
 * 
 * 11. a&b => 두 비트가 모두 1이면 1 반환, 그 외에는 0 반환
 * 
 * 12. ^ => 두 비트가 서로 다르면 1 반환, 같으면 0 반환
 * 
 * 13. | => 두 비트 중 하나라도 1이면 1 반환
 * 
 * 14. && => 두 피연산자 중 참일때만 참 반환
 * 
 * 15. || => 두 피연산자 중 하나라도 참이면 참 반환 
 * 
 * 16. a?b:c => 조건이 참이면 b 반환, 거짓이면 c 반환
 * 	   throw => 예외 발생
 * 	   co_yield => 현재 코루틴을 일시 중단하고 값 반환(C++20부터)
 * 	   = => 대입 연산. C++ 클래스에 기본으로 제공됨
 * 	   +=, -= => 현재 변수에 값을 더하거나 빼서 결과 저장
 * 	   *=, /=, %= => 현재 변수에 값을 곱하거나 나누어 결과 저장
 * 	   <<=, >>= => 현재 변수의 비트를 왼쪽이나 오른쪽으로 시프트 후 저장
 * 	   &=, &=, |= => 현재 변수와 다른 값을 AND, XOR, OR 연산 후 저장
 * 
 * 17. , => 한 문장에서 표현식 구분분
 */

#include <iostream>
using namespace std;

int main() {

	int a = 5, b = 2, c = 8;

	int result_1 = a + b * c;	// 곱셈 먼저 연산(오른쪽으로 결합)
	cout << "Result_1 : " << result_1 << endl;

	int result_2 = (a + b) * c;	// 괄호로 우선순위 변경
	cout << "Result_2 : " << result_2 << endl;

	a += b * c;	// 곱셈 먼저 연산
	cout << "Result_3 : " << a << endl;

	bool condition = true;
	int result_4 = (condition && a > b) ? a : b;	// > 먼저 연산(왼쪽으로 결합)
	cout << "Result 4 : " << result_4 << endl;

	return 0;
}

/*
Result_1 : 21
Result_2 : 56
Result_3 : 21
Result 4 : 21
*/