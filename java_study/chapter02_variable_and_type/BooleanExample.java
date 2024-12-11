/*논리 타입*/
public class BooleanExample {
    public static void main(String[] args) {
        boolean stop = true;
        if(stop) {
            System.out.println("중지합니다.");
        } else {
            System.out.println("시작합니다.");
        }
    }
}   // 중지합니다.

/*
자바는 참과 거짓을 의미하는 논리 리터럴로 true와 false를 사용한다.
논리 리터럴은 다음과 같이 1byte 크기의 boolean 타입 변수에 저장할 수 있다.
boolean stop = true;
boolean state = false;

boolean 타입 변수는 주로 두 가지 상태값에 따라 조건문과 제어문의 실행 흐름을 변경하는 데 사용한다.

위 코드를 보면 stop 변수가 true 값을 가지고 있기 때문에 if 블록이 실행되어 "중지합니다."가 출력된다.
만약 stop 변수가 false 값을 가지고 있다면 else 블록이 실행되어 "시작합니다."를 출력한다.
 */