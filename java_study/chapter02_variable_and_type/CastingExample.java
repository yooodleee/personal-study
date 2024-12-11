/*강제 타입 변환*/
public class CastingExample {
    public static void main(String[] args) {
        int intValue = 44032;
        char charValue = (char) intValue;
        System.out.println(charValue);  // 가

        long longValue = 500;
        intValue = (int) longValue;
        System.out.println(intValue);   // 500

        double doubleValue = 3.14;
        intValue = (int) doubleValue;
        System.out.println(intValue);   // 3
    }
}

/*
큰 허용 범위 타입은 작은 허용 범위 타입으로 자동 타입 변환될 수 없다.
마치 큰 그릇에 가득 채운 물을 작은 그릇 안에 모두 넣을 수 없는 것과 동일한 이치이다.
하지만 큰 그릇의 물을 작은 그릇 크기로 나눠서 한 부분만 작은 그릇에 넣는 것은 가능하다.

이와 같이 큰 허용 범위 타입을 작은 허용 범위 타입으로 강제로 나눠서 저장하는 것을 강제 타입 변환 Casting이라고 한다.
강제 타입 변환은 캐스팅 연산자 괄호 ()를 사용하는데, 괄호 안에 들어가는 타입은 나누는 단위이다.
작은 허용 범위 타입 <= (강제 타입 변환) (작은 허용 범위 타입) 큰 허용 범위 타입

int 타입은 byte 타입보다 더 큰 허용 범위를 가진다. 따라서 int 타입은 byte 타입으로 자동 변환되지 않는다.
하지만 (byte) 캐스팅 연산자를 사용해서 byte 타입으로 강제 변환할 수 있다.
int intValue = 10;
byte byteValue = (byte) intValue;   //강제 타입 변환 Casting

int 타입은 char 타입보다 더 큰 허용 범위를 가진다. 따라서 int 타입은 char 타입으로 자동 변환되지 않는다.
하지만 (char) 캐스팅 연산자를 사용해서 char 타입으로 강제 변환할 수 있다.
char 타입으로 변환하는 이유는 문자를 출력할 수 있기 때문이다.
int intValue = 65;
char charValue = (char) intValue;
System.out.println(charValue);  //"A"가 출력

실수 타입(float, double)은 정수 타입(byte, short, int, long)으로 자동 변환되지 않기 때문에 강제 타입 변환을 사용해야 한다.
이 경우 소수점 이하 부분은 버려지고, 정수 부분만 저장된다.
double doubleValue = 3.14;
int intValue = (int) doubleValue;   //intValue는 정수 부분인 3만 저장
 */