public class CharOperationExample {
    public static void main(String[] args) {
        char c1 = 'A' + 1;  // char c1 = bb;으로 컴파일됨
        char c2 = 'A';
        // char c3 = c2 + c1;   char 변수가 산술 연산에 사용되면 int 타입으로 변환되므로 연산 결과는 int 타입이 됨
        System.out.println("c1: " + c1);    // B
        System.out.println("c2: " + c2);    // A
        //System.out.println("c3: " + c3);
    }
}