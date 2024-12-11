/*기본 타입과 문자열 간의 변환*/
public class PrimitiveAndStringConversionExample {
    public static void main(String[] args) {
        int value1 = Integer.parseInt("10");
        double value2 = Integer.parseDouble("3.14");
        boolean value3 = Boolean.parseBoolean("true");

        System.out.println("value1 : " + value1);   //value1 : 10
        System.out.println("value2 : " + value2);   //value2 : 3.14
        System.out.println("value3 : " + value3);   //value3 : true

        String str1 = String.valueOf(10);
        String str2 = String.valueOf(3.14);
        String str3 = String.valueOf(true);

        System.out.println("str1 : " + str1);   //str1 : 10
        System.out.println("str2 : " + str2);   //str2 : 3.14
        System.out.println("str3 : " + str3);   //str3 : true
    }
}

/*
문자열을 기본 타입으로 강제 타입 변환

프로그램에서 문자열을 기본 타입으로 변환하는 경우가 매우 많다. 예컨대, '12'와 '3.5'를 정수 및 실수 타입으로 변환해서 숫자 연산을 하는 경우이다.
자바에서 문자열을 기본 타입으로 변환하는 방법을 참고하라.

문자열이 숫자가 아닌 알파벳이나 특수 문자, 한글 등을 포함하고 있을 경우 숫자 타입으로 변환을 시도하면 숫자 형식 제외
(NumberFormatException)가 발생한다.

반대로 기본 타입(byte, short, char, int, long, float, double, boolean)의 값을 문자열로 변경하는 경우도 있는데,
이 경우는 간단히 String.valueOf() 메서드를 사용하면 된다.
 */