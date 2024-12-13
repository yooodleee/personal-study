/*
매개변수의 다형성

자동 타입 변환은 필드의 값을 대입할 때에도 발생하지만, 주로 메서드를 호출할 때 많이 발생한다.
메서드를 호출할 때에는 매개 변수의 타입과 동일한 매개값을 지정하는 것이 정석이지만, 매개값을 다양화하기 위해 매개 변수에 자식 객체를 지정할 수도
있다. 예를 들어 다음과 같이 Driver 클래스에는 drive() 메서드가 정의되어 있는데 Vehicle 타입의 매개변수가 선언되어 있다.

class Driver {
    void drive(Vehicle vehicle) {
        vehicle.run();
    }
}

drive() 메서드를 정상적으로 호출한다면 다음과 같을 것이다.
Driver driver = new Driver();
Vehicle vehicle = new Vehicle();
driver.drive(vehicle);

만약 Vehicle의 자식 클래스인 Bus 객체를 drive() 메서드의 매개값으로 넘겨준다면 어떻게 될까?
drive() 메서드는 Vehicle 타입을 매개변수로 선언했지만, Vehicle을 상속받은 Bus 객체가 매개값으로 사용되면 자동 타입 변환이 발생한다.
Vehicle vehicle = bus;(자동 타입 변환)

우리는 여기서 매우 중요한 것을 하나 알게 되었다. 매개변수의 타입이 클래스일 경우, 해당 클래스의 객체 뿐만 아니라 자식 객체까지도 매개값으로 사용
할 수 잇다는 것이다. 즉, 매개값으로 어떤 자식 객체가 제공되느냐에 따라 메서드의 실행결과는 다양해질 수 있다. 자식 객체가 부모의 메서드를 재정의
했다면 메서드 내부에서 재정의된 메서드를 호출함으로써 메서드의 실행결과는 다양해진다.

void drive(vehicle vehicle) {
    vehicle.run();  // 자식 객체가 재정의한 run() 메서드 실행
}
 */
public  class Vehicle {
    public void run() {
        System.out.println("차량이 달립니다.");
    }
}

// Vehicle을 이용하는 클래스
public class Driver {
    public void drive(Vehicle vehicle) {
        vehicle.run();
    }
}

// 자식클래스
public class Bus extends Vehicle {
    @java.lang.Override
    public void run() {
        System.out.println("버스가 달립니다.");
    }
}

// 자식클래스
public class Taxi extends Vehicle {
    @java.lang.Override
    public void run() {
        System.out.println("택시가 달립니다.");
    }
}

// 실행클래스
public class DriveExampme {
    public static void main(String[] args) {
        Driver driver = new Driver();
        Bus bus = new Bus();
        Taxi taxi = new Taxi();

        driver.drive(bus);  // 자동 타입 변환: Vehicle vehicle = bus;
        driver.drive(taxi); // 자동 타입 변환: Vehicle vehicle = taxi;
    }
}