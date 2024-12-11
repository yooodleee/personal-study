/*자동 타입 변환*/
public class PromotionExample {
    public static void main(String[] args) {
        // 자동 타입 변환
        byte byteValue = 10;
        int intValue = byteValue;
        System.out.println("intValue : " + intValue);   // 10

        char charValue = '가';
        intValue = charValue;
        System.out.println("가의 유니코드 : " + intValue);    // 44032

        intValue = 50;
        long longValue = intValue;
        System.out.println("longValue : " + longValue); // 50

        longValue = 100;
        float floatValue = longValue;
        System.out.println("floatValue : " + floatValue);   // 100.0

        floatValue = 100.5F;
        double doubleValue = floatValue;
        System.out.println("doubleValue : " + doubleValue); // 100.5
    }
}

/*
자동 타입 변환 Promotion은 말 그대로 자동으로 타입 변환이 일어나는 것을 말한다.
자동 타입 변환은 값의 허용 범위가 작은 타입이 허용 범위가 큰 타입으로 저장될 때 발생한다.
큰 허용 범위 타입 <= (자동 타입 변환 Promotion) <= 작은 허용 범위 타입

큰 허용 범위 타입과 작은 허용 범위 타입의 구분은 <02-2 기본 타입>에서 정수 타입과 실수 타입을 참고하길 바란다.
기본 타입을 허용 범위 크기순으로 정리하면 다음과 같다.
byte < short < int < long < float < double

다음 코드는 int 타입이 byte 타입보다 허용 범위가 더 크기 때문에 자동 타입 변환이 일어난다.
byte byteValue = 10;
int intValue = byteValue;   //자동 타입 변환됨

정수 타입이 실수 타입으로 저장될 경우에는 무조건 자동 타입 변환이 일어난다. 실수 타입은 정수 타입보다 허용 범위가 더 크기 때문이다.
long longValue = 10000000L;
float floatValue = longValue;   //5.0E9f 로 저장됨
double doubleValue = longValue; //5.0E9로 저장됨

char 타입의 경우 int 타입으로 자동 타입 변환되면 유니코드 값이 int 타입에 저장된다.
char charValue = "A";
int intValue = charValue;   //65가 저장됨


 */