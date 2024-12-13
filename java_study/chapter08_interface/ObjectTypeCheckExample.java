/*
객체 타입 확인

강제 타입 변환은 구현 객체가 인터페이스 타입으로 변환되어 있는 상태에서 가능하다. 그러나 어떤 구현 객체가 변환되어 있는지 알 수 없는 상태에서
무작정 강제 타입 변환할 경우 ClassCastException이 발생할 수도 있다.

예를 들어 다음과 같이 Taxii 객체가 인터페이스로 변환되어 있을 경우, Bus 타입으로 강제 타입 변환하면 구현 클래스 타입이 다르므로
ClassCastException이 발생한다.
Vehicle vehicle = new Taxi();
Bus bus = (Bus) vehicle();

메서드의 매개 변수가 인터페이스로 선언된 경우, 메서드를 호출할 때 다양한 구현 객체들을 매개값으로 저장할 수 있다(매개 변수의 다향성). 어떤 구현
객체가 지정될지 모르는 상황에서 다음과 같이 매개값을 Bus로 강제 타입 변환하면 ClassCastException이 발생할 수 있다.
public void drive(Vehicle vehicle) {
    Bus bus = (Bus) vehicle;
    bus.checkFare();
    vehicle.run();
}

그렇다면 어떤 구현 객체가 인터페이스 타입으로 변환되었는지 확인하는 방법은 없을까? 우리는 상속에서 객체 타입을 확인하기 위해 instanceof 연산자를
사용했다. instanceof 연산자는 인터페이스 타입에서도 사용할 수 있다. 예를 들어 Vehicle 인터페이스 타입으로 변환된 객체가 Bus 인지 확인하려면
다음과 같이 작성하면 된다.
if(vehicle instanceof Bus) {
    Bus bus = (Bus) vehicle;
}

인터페이스 타입으로 자동 타입 변환된 매개값을 메서드 내에서 다시 구현 클래스 타입으로 강제 타입 변환해야 한다면 반드시 매개값이 어떤 객체인지
instanceof 연산자로 확인하고 안전하게 강제 타입 변환해야 한다.
 */
public class Driver {
    public void drive(Vehicle vehicle) {    // vehicle: Bus 객체, Taxi 객체
        if(vehicle instanceof Bus) {    // vehicle 매개변수가 참조하는 객체가 Bus인지 조사
            Bus bus = (Bus) vehicle;    // Bus 객체일 경우 안전하게 강제 타입 변환
            bus.checkFare();    // Bus 타입으로 강제 타입 변환을 하는 이유
        }
    }
    vehicle.run();
}

public class DriverExample {
    public static void main(String[] args) {
        Driver driver = new Driver();

        Bus bus = new Bus();
        Taxi taxi = new Taxi();

        driver.drive(bus);
        driver.drive(taxi);
    }
}