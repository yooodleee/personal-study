package conditional;

public class ContinueExample {
    public static void main(String[] args) {
        int total = 0;
        int num;

        for (num = 1; num <= 100; num++) {
            // 100까지 반복
            if (num % 2 == 0)
                continue;
            total += num;
        }
        
        System.out.println("1부터 100까지의 홀수의 합은: " + total + "입니다.");
    }
}
