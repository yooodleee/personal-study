/*print 메서드 사용 방법*/
public class PrintExample {
    public static void main(String[] args) {
        int value = 123;
        System.out.printf("상품의 가격 : %d원\n", value); // 상품의 가격 : 123원
        System.out.printf("상품의 가격 : %6d원\n", value);    // 상품의 가격 :     123원
        System.out.printf("상품의 가격 : %-6d원\n", value);   // 상품의 가격 : 123      원
        System.out.printf("상품의 가격 : %06d원\n", value);   //상품의 가격 : 000123원

        double area = 3.14159 * 10 * 10;
        System.out.printf("반지름이 %d인 원의 넓이 : %10.2f\n", 10, area);   // 반지름이 10인 원의 넓이 :     314.16

        String name = "홍길동";
        String job = "도적";
        System.out.printf("%6d | %-10s | %10s\n", 1, name, job);    //      1 | 홍길동     |       도적
    }
}

/*
우리는 지금까지 표준 출력 장치인 모니터로 출력하기 위해 System.out의 println() 메서드를 이용했다.
System: 시스템이 가지고 있는 / out: 출력 장치로  / println: 괄호 안의 내용을 출력하고 행을 바꿔라.

println(내용): 괄호 안의 내용을 출력하고 행을 바꿔라
print(내용): 괄호 안의 내용을 출력만 하라.
printf("형식문자열".값1, 값2, ...): 괄호 안의 첫 번째 문자열 형식대로 내용을 출력해라
 */