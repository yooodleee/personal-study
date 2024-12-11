/*정수 타입의 연산*/
public class LongOperationExample {
    public static void main(String[] args) {
        byte value1 = 10;
        int value2 = 100;
        long value3 = 1000L;
        long result = value1 + value2 + value3;
        System.out.println(result); //1110
    }
}

/*
정수 연산식에서 모든 변수가 int 타입으로 변환되는 것은 아니다. 두 피연산자 중 허용 범위가 큰 타입으로 변환되어
연산을 수행한다. 예를 들어, int 타입보다 허용 범위가 큰 long 타입이 피연산자로 사용되면 다른 피연산자는 무조건 long 타입으로 변환하고
연산을 수행한다. 따라서 연산 결과를 long 타입 변수에 저장해야 한다.

long result = long 타입 연산자(+, -, *, %) -> byte/char/short/int 타입
 */