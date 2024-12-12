// 부모 클래스
public class Calculator {
    double areaCircle(double r) {
        System.out.println("Calculator 객체의 areaCircle() 실행");
        return 3.14159 * r * r;
    }
}

// 자식 클래스
public class Computer extends Calculator {
    @java.lang.Override
    double areaCircle(double r) {
        System.out.println("Computer 객체의 areaCircle() 실행");
        return Math.PI * r * r;
    }   // 재정의
}

// 메서드 재정의 테스트
public class ComputerExample {
    public static void main(String[] args) {
        int r = 10;

        Calculator calculator = new Calculator();
        System.out.println("원면적 : " + calculator.areaCircle(r));
        System.out.println();

        Computer computer = new Computer();
        System.out.println("원면적 : " + computer.areaCircle(r));  //재정의된 메서드 호출(computer.areaCricle()
    }
}