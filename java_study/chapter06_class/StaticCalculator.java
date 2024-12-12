public class StaticCalculator {
    static double pi = 3.14159;

    static int plus(int x, int y) {
        return x + y;
    }

    static int minus(int x, int y) {
        return x - y;
    }
}

public class CalculatorExample {
    public static void main(String[] args) {
        double result1 = 10 * 10 * StaticCalculator.pi;
        int result2 = StaticCalculator.plus(10, 5);
        int result3 = StaticCalculator.minus(10, 5);

        System.out.println("result1:" + result1);
        System.out.println("result2:" + result2);
        System.out.println("result3:" + result3);
    }
}