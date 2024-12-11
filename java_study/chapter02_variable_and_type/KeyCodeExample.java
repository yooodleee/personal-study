/*입력된 키코드를 변수에 저장*/
public class KeyCodeExample {
    public static void main(String[] args) throws Exception {
        int KeyCode;

        KeyCode = System.in.read();
        System.out.println("KeyCode : " + KeyCode); //KeyCode : 97

        KeyCode = System.in.read();
        System.out.println("KeyCode : " + KeyCode); //KeyCode : 13

        KeyCode = System.in.read();
        System.out.print("KeyCode : " + KeyCode);   //KeyCode : 10
    }
}

/*
키보드에서 키 하나를 입력하면 프로그램에서는 숫자로 된 키코드를 읽을 수 있다.
예컨대, 알파벳 a를 입력하면 97번을, 숫자 1을 입력하면 49번을 읽을 수 있다.
키코드를 읽기 위해서는 System.in.read()를 사용하면 된다.

System: 시스템이 가지고 있는 / in: 입력 장치에서 / read: 입력된 키코드를 읽어라.

보통 System.in.read()로 읽은 키코드를 대입 연산자를 사용해 int 변수에 저장한다. 변수에 저장된 값을 조사하면 입력된 키가 무엇인지 알 수 있다.
 */