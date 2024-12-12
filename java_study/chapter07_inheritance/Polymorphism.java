/*
필드의 다양성

그렇다면 왜 자동 타입 변환이 필요할까? 그냥 자식 타입으로 사용하면 될 것을 부모 타입으로 변환해서 사용하는 이유가 무엇일까?
그것은 다형성을 구현하기 위함이다. 필드의 타입을 부모 타입으로 선언하면 다양한 자식 객체들이 저장될 수 있기 때문에 필드 사용 결과가 달라질 수
있다. 이것이 필드의 다형성이다.

예를 들면, 자동차를 구성하는 부품은 언제든지 교체할 수 있다. 부품은 고장이 날 수 있고, 성능이 더 좋은 부품으로 교체되기도 한다. 객체 지향
프로그래밍에서도 마찬가지이다. 프로그램은 수많은 객체들이 서로 연결되고 각자의 역할을 하게 되는데, 이 객체들은 다른 객체로 교체될 수 있어야 한다.

자동차 클래스에 포함된 타이어 클래스를 생각해보겠다. 자동차 클래스를 처음 설계할 때 사용한 타이어 객체는 언제든지 성능이 좋은 다른 타이어 객체로
교체할 수 있어야 한다. 새로 교체되는 타이어 객체는 기존 타이어와 사용 방법은 동일하지만 실행 결과는 더 우수하게 나와야 할 것이다. 이것을 프로그램
으로 구현하기 위해 상속과 재정의, 타입 변환을 이용한다.

부모 클래스를 상속하는 자식 클래스는 부모가 가지고 있는 필드와 메서드를 가지고 있으니 사용 방법이 동일할 것이다. 자식 클래스는 부모의 메서드를
재정의해서 메서드의 실행 내용을 변경함으로써 더 우수한 실행 결과가 나오게 할 수도 있다. 그리고 자식 타입을 부모 타입으로 변환할 수 있다. 이 세
가지가 다형성을 구현할 수 있는 기술적 조건이 된다.

필드의 다형성을 코드로 살펴보자.

class Car {
    //field
    Tire frontLeftTire = new Tire();
    Tire frontRightTire = new Tire();
    Tire backLeftTire = new Tire();
    Tire backRightTire = new Tire();
    //method
    void run() {...}
}


Car 클래스는 4개의 필드를 가지고 있다. Car 클래스로부터 Car 객체를 생성하면 4개의 Tire 필드에 각각 하나씩 Tire 객체가 들어가게 된다.
그런데 frontRightTire와 backLeftTire를 HanKookTire와 KumhoTire로 교체할 이유가 생겼다. 이러한 경우 다음과 같은 코드를 사용해서 교체할 수
있다.
Car myCar = new Car();
myCar.frontRightTire = new HanKookTire();
myCar.backLeftTire = new KumhoTire();
myCar.run();

Tire 클래스 타입인 frontRightTire와 backLeftTire는 원래 Tire 객체가 저장되어야 하지만, Tire의 자식 객체가
저장되어도 문제가 없다. 왜냐하면 자식 타입은 부모 타입으로 자동 타입 변환되기 때문이다. frontRightTire와 backLeftTire에 Tire 자식 객체가
저장되어도 Car 객체는 Tire 클래스에 선언된 필드와 메서드만 사용하므로 전혀 문제가 되지 않는다. HankookTire와 KumhoTire는 부모인 Tire의 필드와
메서드를 가지고 있다.

Car 객체에 run() 메서드가 있고, run() 메서드는 각 Tire 객체의 roll() 메서드를 다음과 같이 호출한다고 가정해보자.
void run() {
    frontLeftTire.roll();
    frontRightTire.roll();
    backLeftTire.roll();
    backRightTire.roll();

frontRightTire와 backLeftTire를 교체하기 전에는 Tire 객체의 roll() 메서드가 호출되지만,
HankookTire와 KumhoTire로 교체되면 HankookTire와 KumhoTire가 roll() 메서드를 재정의하고 있으므로 교체 이후에는
HankookTire와 KumhoTire의 roll() 메서드가 호출되어 실행 결과가 달라지낟. 이 성질은 이미 <07-1 메서드 재정의>에서 살펴보았다.

이와 같이 자동 타입 변환을 이용해서 Tire 필드값을 교체함으로써 Car의 run() 메서드를 수정하지 않아도 다양한 roll() 메서드의 실행 결과를
얻게 된다. 이것이 바로 필드의 다형성이다. 예제를 작성해보면서 지금까지 설명했던 내용을 눈으로 확인해보자.
 */
public class Tire {
    //field
    public int maxRotation;
    public int accumulatedRotation;
    public String location;

    //constructor
    public Tire(String location, int maxRotation) {
        this.location = location;
        this.maxRotation = maxRotation;
    }

    //method
    public boolean roll() {
        ++accumulatedRotation;  // 누적 회전수 1 증가
        if(accumulatedRotation < maxRotation) {
            System.out.println(location + " Tire 수명 : " + (maxRotation - accumulatedRotation) + "회");
            return true;    // 정상 회전(누적<최대)일 경우 실행
        } else {
            System.out.println("***" + location + " Tire 펑크 ***");
            return false;   // 펑크(누적=최대)일 경우 실행
        }
    }
}

// Tire를 부품으로 가지는 클래스
public class Car {
    //field
    Tire frontLeftTire = new Tire("앞왼쪽", 6);
    Tire frontRightTire = new Tire("앞오른쪽", 2);
    Tire backLeftTire = new Tire("뒤왼쪽", 3);
    Tire backRightTire = new Tire("뒤오른쪽", 4);
    //constructor
    //method
    int run() {
        System.out.println("[자동차가 달립니다.]");
        if(frontLeftTire.roll() == false) { stop(); return 1; }
        if(frontRightTire.roll() == false) { stop(); return 2; }
        if(backLeftTire.roll() == false) { stop(); return 3; }
        if(backRightTire.roll() == false) { stop(); return 4; }
        return 0;   // 모든 타이어를 1회 운전시키기 위해 각 Tire 객체의 roll() 메서드를 호출
        // false를 리턴하는 roll()이 있을 경우 stop() 메서드를 호출하고 해당 타이어 번호를 리턴
    }

    void stop() {
        System.out.println("[자동차가 멈춥니다]");
    }   // 펑크가 났을 경우
}

// Tire의 자식 클래스
public class HankookTire extends Tire {
    //field
    //constructor
    public HankookTire(String location, int maxRotation) {
        super(location, maxRotation);
    }
    //method

    @java.lang.Override
    public boolean roll() { // 다른 내용을 출력하기 위해 재정의한 roll() 메서드
        ++accumulatedRotation;
        if(accumulatedRotation < maxRotation) {
            System.out.println(location + "HankookTire 수명 : " + (maxRotation - accumulatedRotation) + "회");
            return true;
        } else {
            System.out.println("*** " + location + " HankookTire 펑크 ***");
            return false;
        }
    }
}

// Tire의 자식 클래스
public class KumhoTire extends Tire {
    //field
    //constructor
    public KumhoTire(String location, int maxRotation) {
        super(location, maxRotation);
    }
    //method

    @java.lang.Override
    public boolean roll() {
        ++accumulatedRotation;
        if(accumulatedRotation < maxRotation) {
            System.out.println(location + "KumhoTire 수명 : " + maxRotation - (accumulatedRotation) + "회");
            return true;
        } else {
            System.out.println("*** " + location + " KumhoTire 펑크 ***");
            return false;
        }
    }
}

// 실행클래스
public class CarExample {
    public static void main(String[] args) {
        Car car = new Car();    // car 객체 생성

        for (int i=1;i<=5;i++) {
            int problemLocation = car.run();    // car 객체의 run() 메서드 5번 반복 실행

            switch (problemLocation) {
                case 1:
                    System.out.println("앞왼쪽 HankookTire로 교체");
                    car.frontLeftTire = new HankookTire("앞왼쪽", 15);
                    break;
                case 2:
                    System.out.println("앞오른쪽 KumhoTire로 교체");
                    car.frontRightTire = new KumhoTire("앞오른쪽", 13);
                    break;
                case 3:
                    System.out.println("뒤왼쪽 HankookTire로 교체");
                    car.backLeftTire = new HankookTire("뒤왼쪽", 14);
                    break;
                case 4:
                    System.out.println("뒤오른쪽 KumhoTire로 교체");
                    car.backRightTire = new KumhoTire("뒤오른쪽", 17);
                    break;
            }
            System.out.println("----------------------------------");   //1 회전 시 출력되는 내용을 구분
        }
    }
}