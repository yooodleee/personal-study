/*입력된 키의 개수와 상관없이 키코드 읽기*/
public class ContinueKeyCodeReadExample {
    public static void main(String[] args) throws Exception {
        int KeyCode;

        while(true) {   // 반복 실행
            KeyCode = System.in.read();
            System.out.println("KeyCode : " + KeyCode);
        }
    }
}

/*
위 예제는 while(true) 때문에 무한 반복을 실행한다.
 */