/*이스케이프 문자 출력*/
public class EscapeExample {
    public static void main(String[] args) {
        System.out.println("번호\t이름\t직업");   // 번호       이름          직업
        System.out.println("행 단위 출력\n");    //행 단위 출력
        System.out.println("행 단위 출력\n");    //행 단위 출력
        System.out.println("우리는 \"개발자\" 입니다."); // 우리는 "개발자" 입니다.
        System.our.println("봄\\여름\\가을\\겨울");    // 봄\여름\가을\겨울
    }
}

/*
문자열 내부에 역슬래시(\)가 붙은 문자를 사용할 수 있는데, 이것을 이스케이프escape 문자라고 한다.
이스케이프 문자를 사용하면 문자열 내부에 특정 문자를 포함시킬 수 있다.
예를 들어 큰따옴표는 문자열 식별 기호인데, 데이터로써 큰따옴표를 사용하고 싶을 때는 이스케이프 문자\"를 사용한다.

String str = "나는 \"자바\"를 좋아합니다.";
System.out.println(str);
-> 나는 "자바"를 좋아합니다.

또한 이스케이프 문자를 사용하면 출력을 제어할 수 있다. 예를 들어, 탭만큼 띄우거나(\t) 개행(한 줄 내림, \n)을 지시할 수 있다.
String str = "번호\t이름\t나이";
System.out.println(str);
-> 번호       이름      나이

String str = "홍길동\n감자바";
System.out.println(str);
-> 홍길동
-> 감자바
 */