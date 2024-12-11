/*String 타입*/
public class StringExample {
    public static void main(String[] args) {
        String name = "홍길동";
        String job = "프로그래머";
        System.out.println(name);
        System.out.println(job);
    }
}

/*
작은따옴표(')로 감싼 문자는 char 타입 변수에 저장되어 유니코드로 저장되지만, 큰따옴표(")로 감싼
문자 또는 여러 개의 문자들은 유니코드로 변환되지 않는다. 따라서 다음은 잘못 작성된 코드이다.
char var1 = "A";
char var2 = "홍길동";

자바에서 큰따옴표(")로 감싼 문자들을 문자열이라고 부른다. 작은따옴표와 큰따옴표는 컴파일러가 문자 리터럴과 문자열 리터럴을 구별하는 기호로
사용된다. 문자열을 변수에 저장하고 싶다면 다음과 같이 String 타입을 사용해야 한다.
String var1 = "A";
String var2 = "홍길동";

* String 타입은 기본 타입이 아니다. String은 클래스 타입이다.
 */