/*
매개변수의 다형성

자동 타입 변환은 필드의 값을 대입할 때에도 발생하지만, 주로 메서드를 호출할 때 많이 발생한다.
매개값을 다양화하기 위해 상속에서는 매개 변수를 부모 타입으로 선언하고 호출할 때에는 자식 객체를 대입했다.

이번에는 매개변수를 인터페이스 타입으로 선언하고 호출할 때에는 구현 객체를 대입한다.
예를 들면, 다음과 같이 Driver 클래스에는 drive() 메서드가 정의되어 있는데 Vehicle 타입의 매개 변수가 선언되어 있다.
public class Driver {
    public void drive(Vehicle vehicle) {
        vehicle.run();
    }
}

Vehicle을 다음과 같이 인터페이스 타입이라고 가정해보자.
public interface Vehicle {
    public void run();
}

만약 Bus가 구현 클래스라면 다음과 같이 Drive의 drive() 메서드를 호출할 때 Bus 객체를 생성해서 매개값으로 줄 수 있다.
Driver driver = new Driver();
Bus bus = new Bus();
driver.drive(bus);  // 자동 타입 변환 발생 Vehicle vehicle = bus;

drive() 메서드는 Vehicle 타입을 매개 변수로 선언했지만, Vehicle을 구현한 Bus 객체가 매개값으로 사용되면 자동 타입 변환이 발생한다.
Vehicle vehicle = bus;  // 자동 타입 변환

매개 변수의 타입이 인터페이스일 경우 어떠한 구현 객체도 매개값으로 사용할 수 있고, 어떤 구현 객체가 제공되느냐에 따라
메서드의 실행결과는 다양해질 수 있다. 이것이 인터페이스 매개 변수의 다형성이다.
void drive(Vehicle vehicle) {   // vehicle: 구현 객체
    vehicle.run();  // 구현 객체의 run() 메서드가 실행됨
}

* 매개변수의 다형성

인터페이스는 메서드의 매개 변수로 많이 등장한다. 인터페이스 타입으로 매개 변수를 선언하면 메서드 호출 시 매개값
으로 여러 가지 종류의 구현 객체를 줄 수 있기 때문에 메서드 실행결과가 다양하게 나온다(매개 변수의 다형성).

useRemoteControl() 메서드의 매개 변수가 RemoteControl 인터페이스 타입일 경우, 매개값으로 Television 객체 또는 Audio 객체를 선택적으로
줄 수 있다. 메서드 호출 시 어떤 객체를 매개값으로 주느냐에 따라 useRemoteControl() 메서드의 실행결과는 다르게 나온다.
 */
public class Driver {
    public void drive(Vehicle vehicle) {
        vehicle.run();
    }
}

public interface Vehicle {
    public void run();
}

public class Bus implements Vehicle {
    @java.lang.Override
    public void run() {
        System.out.println("버스가 달립니다.");
    }
}

public class Taxi implements Vehicle {
    @java.lang.Override
    public void run() {
        System.out.println("택시가 달립니다.");
    }
}

public class DriverExample {
    public stat void main(String[] args) {
        Driver driver = new Driver();

        Bus bus = new Bus();
        Taxi taxi = new Taxi();

        driver.drive(bus);
        driver.drive(taxi);
    }
}