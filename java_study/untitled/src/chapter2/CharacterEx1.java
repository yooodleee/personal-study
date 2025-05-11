package chapter2;

public class CharacterEx1 {
    public static void main(String[] args) {
        char ch1 = 'A';
        System.out.println(ch1);        // 문자 출력
        System.out.println((int)ch1);   // 문자에 해당되는 아스키 코드값 출력

        char ch2 = 66;                  // 정숫값 대입
        System.out.println(ch2);        // 정숫값에 해당하는 문자 출력

        int ch3 = 67;
        System.out.println(ch3);        // 문자 정숫값 출력
        System.out.print((char)ch3);    // 정숫값에 해당하는 문자 출력
    }
}
