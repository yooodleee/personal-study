package conditional;

public class BreakExample2 {
    public static void main(String[] args) {
        int sum = 0;
        int num = 0;

        for (num = 0; ; num++) {
            // 조건식을 생략한 대신 break 문을 사용합니다.
            sum += num;
            if (sum >= 100) // sum이 100보다 크거나 같을 때 종료 조건
                break;
            
        }
        System.out.println("num: " + num);
        System.out.println("sum: " + sum);
    }
}
