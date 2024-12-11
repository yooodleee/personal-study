public class LongExample {
    public static void main(String[] args) {
        long var1 = 10;
        long var2 = 20L;
        //long var3 = 100000000000;     -> compile error
        long var4 = 10000000000L;

        System.out.println(var1);
        System.out.println(var2);
        System.out.println(var4);
    }
}

/*long 타입
long 타입은 수치가 큰 데이터를 다루는 프로그램에서 주로 사용된다.
대표적으로 은행이나 과확 관련 프로그램들이다.

기본적으로 컴파일러는 정수 리터럴을 int 타입으로 간주한다. 그래서 정수 리터럴이 int 타입의 허용 범위
(-2,147,483,648 ~ 2,147,483,647)를 초과할 경우, long 타입임을 컴파일러에게 알려줘야 한다.

방법은 정수 리터럴 뒤에 소문자 l이나 대문자 L을 붙이면 된다.
일반적으로 소문자 l은 숫자 1과 비슷해 혼동하기 쉬우므로 대문자 L을 사용한다.

* long 타입 변수에 정수 리터럴을 저장할 때 반드시 L을 붙여야 하는 것은 아니다.
정수 리터럴이 int 타입의 허용 범위 이내라면 L을 붙이지 않아도 된다.
 */