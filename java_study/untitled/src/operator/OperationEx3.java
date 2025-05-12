package operator;

public class OperationEx3 {
    public static void main(String[] args) {
        int num1 = 10;
        int i = 2;

        boolean value = ((num1 = num1 + 10) < 20) && ((i = i + 2) < 10);    // 논리 곱에서 앞 항의 결괏값이 거짓이므로 실행되지 않음
        System.out.println(value);
        System.out.println(num1);
        System.out.println(i);

        value = ((num1 = num1 + 10) > 10) || ((i = i + 2) < 10);    // 논리 합에서 앞 항의 결괏값이 참이므로 실행되지 않음
        System.out.println(value);
        System.out.println(num1);
        System.out.println(i);
    }
}
