package main

import (
	"fmt"
)

func main() {
	var a int = 10
	var b float64 = 3.5

	// 직접적인 타입 변환 없이는 다음과 같은 연산은 허용되지 않습니다:
	// c := a + b // 컴파일 에러: mismatched types int and float64

	// 명시적 타입 변환을 통해 연산이 가능:
	c := float64(a) + b
	fmt.Println(c) // 13.5

	// 문자열과 정수의 결합도 명시적 변환이 필요:
	var age int = 30
	greeting := "나이는 " + fmt.Sprint(age) + "살입니다."
	fmt.Println(greeting) // 나이는 30살입니다.
}