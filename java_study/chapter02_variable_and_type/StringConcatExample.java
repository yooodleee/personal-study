/*문자열 결합 연산*/
public class StringConcatExample {
    public static void main(String[] args) {
        // 숫자 연산
        int value = 10 + 2 + 8;
        System.out.println("value : " + value); // value : 20

        // 문자열 결합 연산
        String str1 = 10 + 2 + "8";
        System.out.println("str1 : " + str1);   // str1 : 128

        String str2 = 10 + "2" + 8;
        System.out.println("str2 : " + str2);   // str2 : 1028

        String str3 = "10" + 2 + 8;
        System.out.println("str3 : " + str3);   // str3 : 1028

        String str4 = "10" + (2 + 8);
        System.out.println("str4 : " + str4);   // str4 : 1010
    }
}

/*
자바에서 + 연산자는 두 가지 기능을 가지고 있다. 피연산자가 모두 숫자일 경우에는 덧셈 연산을, 피연산자 중 하나가 문자열일 경우
나머지 피연산자도 문자열로 자동 변환되어 문자열 결합을 수행한다.

int value = 3 + 7;  -> int value = 10;
String str = "3" + 7;   -> String str = "3" + "7";  -> String str = "37";
String str = 3 + "7";   -> String str = "3" + "7";  -> String str = "37";

int value = 1 + 2 + 3;  -> int value = 3 + 3;   -> int value = 6;
String str = 1 + 2 + "3";   -> String str = 3 + "3";    -> String str = "33";
String str = 1 + "2" + 3;   -> String str = "12" + 3;   -> String str = "123";
String str = "1" + 2 + 3    -> String str = "12" + 3;   -> String str = "123";
*/