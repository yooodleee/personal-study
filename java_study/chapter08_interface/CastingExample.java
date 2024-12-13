/*
강제 타입 변환

구현 객체가 인터페이스 타입으로 자동 타입 변환하면, 인터페이스에 선언된 메서드만 사용 가능하다는 제약 사항이 따른다.
예컨대 인터페이스에는 3개의 메서드만 선언되어 있고 클래스에는 5개의 메서드가 선언되어 있다면, 인터페이스로 호출 가능한 메서드는 3개 뿐이다.

하지만 경우에 따라서는 구현 클래스에 선언된 필드와 메서드를 사용해야 할 경우도 발생한다.
이때 강제 타입 변환 Casting을 해서 다시 구현 클래스 타입으로 변환한 다음, 구현 클래스의 필드와 메서드를 사용할 수 있다.

interface Vehicle {
    void run();
}

class Bus implements Vehicle {
    void run() {...};
    void checkFare () {...};
}

Vehicle vehicle = new Bus();

vehicle.run();  // 가능
vehicle.checkFare();    (x)

Bus bus = (Bus) vehicle();  // 강제 타입 변환

bus.run();  // 가능
bus.checkFare();  // 가능
 */
public interface Vehicle {
    public void run();
}

public class Bus implements Vehicle {
    @java.lang.Override
    public void run() {
        System.out.println("버스가 달립니다.");
    }

    public void checkFare() {
        System.out.println("승차요금을 체크합니다.");
    }
}

public class VehicleExample {
    public static void main(String[] args) {
        Vehicle vehicle = new Bus();

        vehicle.run();
        // vehicle.checkFare(); Vehicle 인터페이스에는 checkFare()가 없음

        Bus bus = (Bus) vehicle;    // 강제 타입 변환

        bus.run();
        bus.checkFare();    // Bus 클래스에는 checkFare()가 있음
    }
}