// ¹æ¹®ÇÏ´Â ¼Õ´Ô ¼ö¸¸Å­ »§ ¸¸µé±â

#include <iostream>
#include <string>


using namespace std;

int main() {

	int customer_num = 0;

	cout << "¿À´Ã ¹æ¹® ¼Õ´Ô: ";
	cin >> customer_num;	// ¼Õ´Ô ¼ö ÀÔ·Â

	string* bread = new string[customer_num];	// ¼Õ´Ô ¼ö¸¸Å­ string ¹è¿­ »ý¼º

	for (int i = 0; i < customer_num; i++)	// ÀÔ·Â¹ÞÀº ¼Õ´Ô ¼ö¸¸Å­ ¹Ýº¹
	{
		bread[i] = "»§_" + to_string(i);		// '»§_¼ýÀÚ' ÇüÅÂ·Î ¹è¿­¿¡ ÀúÀå
	}

	cout << endl << "--»ý¼ºµÈ »§--" << endl;
	for (int i = 0; i < customer_num; i++)
	{
		cout << *(bread + i) << endl;	// »ý»êµÈ »§ Ãâ·Â(Æ÷ÀÎÅÍ ¿¬»ê Âü°í)
	}

	delete[] bread;	// string ¹è¿­ »èÁ¦

	return 0;
}

/*
¿À´Ã ¹æ¹® ¼Õ´Ô: 5

--»ý¼ºµÈ »§--
»§_0
»§_1
»§_2
»§_3
»§_4
*/