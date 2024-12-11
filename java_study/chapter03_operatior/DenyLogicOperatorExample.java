/*논리 부정 연산자*/
public class DenyLogicOperatorExample {
    public static void main(String[] args) {
        boolean play = true;
        System.out.println(play);   //true

        play = !play;
        System.out.println(play);   //false

        play = !play;
        System.out.println(play);   //true
    }
}