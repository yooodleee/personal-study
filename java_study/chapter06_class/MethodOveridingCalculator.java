public class MethodOveridingCalculator {
    // 정사각형의 넓이
    double areaRectangle(double width) {
        return width * width;
    }

    // 직사각형의 넓이
    double areaRectangle(double width, double height) {
        return width * height;
    }
}

public class CalculatorExample {
    public static void main(String[] args) {
        MethodOveridingCalculator myCalc = new MethodOveridingCalculator();

        // 정사각형의 넓이 구하기
        double result1 = myCalc.areaRectangle(10);

        // 직사각형의 넓이 구하기
        double result2 = myCalc.areaRectangle(10, 20);

        // 결과 출력
        System.out.println("정사각형 넓이=" + result1);
        System.out.println("직사각형 넓이=" + result2);
    }
}