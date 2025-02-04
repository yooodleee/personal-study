// string으로 문자열 사용하기

#include <iostream>
// #include <string>	// iostream 헤더에 string도 포함됨

using namespace std;

int main() {

	string string_value("Hello");
	cout << string_value << endl;

	string_value = "World";
	cout << string_value << endl;

	return 0;
}

/*
Hello
World
*/