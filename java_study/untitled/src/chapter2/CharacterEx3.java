package chapter2;

public class CharacterEx3 {
    public static void main(String[] args) {
        int a = 65;
        int b = -65;

        char a2 = 65;
        // char b2 = -65;   문자형 변수에 음수를 넣으면 오류가 발생하므로 이와 같이 주석 처리함.

        System.out.println((char)a);
        System.out.println((char)b);
        System.out.println(a2);
    }
}
