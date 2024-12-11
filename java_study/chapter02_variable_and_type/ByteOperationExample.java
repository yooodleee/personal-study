/*정수 타입 연산*/
public class ByteOperationExample {
    public static void main(String[] args) {
        byte result1 = 10 + 20;
        System.out.println(result1);    // 30

        byte x = 10;
        byte y = 20;
        result2 = x + y;
        System.out.println(result2);    // 30
    }
}

/*
정수 타입 변수가 산술 연산식에서 피연산자로 사용되면 int 타입보다 작은 byte, short 타입의 변수는 int 타입으로 자동 타입 변환되어 연산을 수행한다.
* byte 타입 변수가 피연산자로 사용된 경우
    byte x = 10;
    byte y = 20;
    byte result = x + y;    //compile error
    int result = x + y;

* int 타입 변수가 피연산자로 사용된 경우
    int x = 10;
    int y = 20;
    int result = x + y;

위 경우에서 첫 번째의 예시처럼 byte 변수 x, y가 피연산자로 사용되면 int 타입으로 변환되어 연산되므로
연산 결과를 byte 변수에 저장하면 컴파일 에러(compile error: Type mismatch: cannot convert from int to byte)가 발생한다.
따라서 연산 결과를 int 변수에 저장해야 한다.

두 번째 예시는 처음부터 x, y를 int 타입으로 선언한 것이다. 앞의 두 가지 코드를 컴파일하면 동일한 바이트 코드를 얻기 때문에
특별한 이유가 없는 경우 정수 연산에 사용되는 변수는 두 번째 에시와 같이 int 타입으로 선언하는 것이 타입 변환을 줄여주는 방법이다.
타입 변환이 줄면 실행 성능이 향상될 수밖에 없다.
 */