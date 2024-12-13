/*
필드의 다형성
 */
public interface Tire {
    public void roll();
}

public class HankookTire implements Tire {
    @java.lang.Override
    public void roll() {
        System.out.println("한국 타이어가 굴러갑니다.");
    }
}

public class KumhoTire implements Tire {
    @java.lang.Override
    public void roll() {
        System.out.println("금호 타이어가 굴러갑니다.");
    }
}

public class Car {
    Tire frontLeftTire = new HankookTire();
    Tire frontRightTire = new HankookTire();
    Tire backLeftTire = new HankookTire();
    Tire backRightTire = new HankookTire();

    void run() {
        frontLeftTire.roll();
        frontRightTire.roll();
        backLeftTire.roll();
        backRightTire.roll();
    }
}

public class CarExample {
    public static void main(String[] args) {
        Car myCar = new Car();

        myCar.run();

        myCar.frontLeftTire = new KumhoTire();
        myCar.frontRightTire = new KumhoTire();

        myCar.run();
    }
}