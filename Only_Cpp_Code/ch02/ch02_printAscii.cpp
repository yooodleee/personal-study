// 아스키 코드 출력하기

#include <iostream>
using namespace std;

int main()
{
	cout << "아스키 코드 출력하기 [32 ~ 126]:\n";

	for (char i = 32; i <= 126; i++)	// 32부터 126까지 1씩 증가하며 반복
	{
		// 아스키 코드를 출력할 때 공백을 넣고 16개마다 줄 바꾸기
		cout << i << ((i % 16 == 15) ? '\n' : ' ');
	}

	return 0;
}

//아스키 코드 출력하기[32 ~126]:
//!" # $ % & ' ( ) * + , - . /
//0 1 2 3 4 5 6 7 8 9 : ; < = > ?
//@ A B C D E F G H I J K L M N O
//P Q R S T U V W X Y Z[\] ^ _
//` a b c d e f g h i j k l m n o
//p q r s t u v w x y z{ | } ~