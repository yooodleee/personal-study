/*char 타입*/
public class CharExample {
    public static void main(String[] args) {
        char c1 = 'A';  //문자를 직접 저장
        char c2 = 65;   //10진수로 저장
        char c3 = '/u0041'; //16진수로 저장

        char c4 = '가';  //문자를 직접 저장
        char c5 = 44032;    //10진수로 저장
        char c6 = '/uac00'; //16진수로 저장

        System.out.println(c1); //A
        System.out.println(c2); //A
        System.out.println(c3); //A
        System.out.println(c4); //가
        System.out.println(c5); //가
        System.out.println(c6); //가
    }
}

/*
하나의 문자를 작은 따옴표(')로 감싼 것을 문자 리터럴이라고 한다. 문자 리터럴은 유니코드(Unicode)로 변환되어 저장된다.
유니코드는 세계 각국의 문자를 2byte로 표현할 수 있는 숫자(0~65535)로 매핑한 국제 표준 규약이다.
자바는 이러한 유니코드를 저장할 수 있도록 2byte 크기인 char 타입을 제공한다.

예컨대, 'A', 'B', '가', '각' 문자를 char 변수에 저장할 수 경우 변수에 저장되는 유니코드 값은 다음과 같다.

char var1 = 'A';    //유니코드: 65
char var2 = 'B';    //유니코드: 66
char var3 = '가';    //유니코드: 44032
char var4 = '각';    //유니코드: 44033

유니코드는 정수이므로 char도 정수 타입에 속한다. 그래서 char 변수에 작은따옴표(')로 감싼 문자가 아니라,
10진수 또는 16진수 형태로 유니코드를 저장할 수 있다. 예컨대, 문자 'A'는 10진수로 65이고, 16진수로는 0x0041이므로
다음과 같이 char 변수에 직접 저장할 수 있다.

char c = 65;    // 10진수
char c = 0x0041;    //16진수
 */