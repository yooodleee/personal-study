// �ƽ�Ű �ڵ� ����ϱ�

#include <iostream>
using namespace std;

int main()
{
	cout << "�ƽ�Ű �ڵ� ����ϱ� [32 ~ 126]:\n";

	for (char i = 32; i <= 126; i++)	// 32���� 126���� 1�� �����ϸ� �ݺ�
	{
		// �ƽ�Ű �ڵ带 ����� �� ������ �ְ� 16������ �� �ٲٱ�
		cout << i << ((i % 16 == 15) ? '\n' : ' ');
	}

	return 0;
}

//�ƽ�Ű �ڵ� ����ϱ�[32 ~126]:
//!" # $ % & ' ( ) * + , - . /
//0 1 2 3 4 5 6 7 8 9 : ; < = > ?
//@ A B C D E F G H I J K L M N O
//P Q R S T U V W X Y Z[\] ^ _
//` a b c d e f g h i j k l m n o
//p q r s t u v w x y z{ | } ~