/*연산식에서 자동 타입 변환*/
public class OperationsPromotionExample {
    public static void main(String[] args) {
        byte byteValue1 = 10;
        byte byteValue2 = 20;
        // byte byteValue3 = byteValue1 + bytevalue2;   -> compile error
        int intvalue1 = byteValue1 + byteValue2;
        System.out.println(intvalue1);  // 30

        char charValue1 = 'A';
        char charValue2 = 1;
        // char charValue3 = charValue1 + charValue2;   -> compile error
        int intValue2 = charValue1 + charValue2;
        System.out.println("유니코드=" + intvalue1);    // 유니코드=66
        System.out.println("출력문자=" + (char)intValue2);  // 출력문자=B

        int intValue3 = 10;
        int intValue4 = intValue3 / 4;
        System.out.println(intValue4);  // 2

        int intValue5 = 10;
        // int intValue6 = 10 / 4.0;    -> compile error
        double doubleValue = intValue5 / 4.0;
        System.out.println(doubleValue);    // 2.5

        int x = 1;
        int y = 2;
        double result = (double) x / y;
        System.out.println(result); // 0.5
    }
}

/*
실수 타입 변수가 산술 연산식에서 피연산자로 사용될 경우 두 피연산자가 동일한 타입이라면 해당 타입으로 연산되지만,
피연산자 중 하나가 double 타입이라면 다른 피연산자도 double 타입으로 자동 타입 변솬되어 연산을 수행한다.
따라서 연산 결과는 double 타입이 된다.

int 타입과 double 타입을 연산해도 동일한 과정을 거친다. 먼저 int 타입의 피연산자가 double 타입으로 자동 변환되고 연산을 수행한다.
int intValue = 10;
double doubleValue = 5.5;
double result = intValue + doubleValue; //result에 15.5가 저장됨

만약 꼭 int 타입으로 연산을 해야 한다면 double 타입을 int 타입으로 강제 변환하고 덧셈 연산을 수행하면 된다.
int intValue = 10;
double doubleValue = 5.5;
int result = intvalue + (int) doubleValue;  //result에 15가 저장됨

수학에서 1을 2로 나누면 결과값은 0.5가 된다. 이것을 코드로 옮기면 다음과 같다. result의 결과값으로 0.5가 츨력될까?
int x = 1;
int y = 2;
double result = x / y;
System.out.println(result); //0.0

위 코드를 실행하면 0.5가 출력되는 것이 아니라 0.0이 출력된다. 그 이유는 자바에서 정수 연산의 결과는 정수가 출력되기 때문이다.
x / y의 연산 결과는 0.5가 아니라 0이 되고, 0을 double 타입 변수 result에 저장하므로 0.0이 되는 것이다.

위 코드의 결과가 0.5가 되기 위해서는 x / y를 정수 연산이 아니라 실수 연산으로 변경해야 한다.
즉 x와 y 둘 중 하나 또는 둘 모두를 double 타입으로 변환해야 하는 것이다. 정수 타입을 실수 타입으로 변환하는 방법은 다음과 같다.
float floatValue = (float) 정수;
double doublevalue = (double) 정수;
 */