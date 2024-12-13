/*
추상 클래스 선언

추상 클래스를 선언할 때에는 클래스 선언에 abstract 키워드를 붙여야 한다.
abstract를 붙이면 new 연산자를 이용해서 객체를 만들지 못하고, 상속을 통해 자식 클래스만 만들 수 있다.
public abstract class 클래스 {
    //field
    //constructor
    //method
}

추상 클래스도 일반 클래스와 마찬가지로 필드, 생성자, 메서드 선언을 할 수 있다.
new 연산자로 직접 생성자를 호출할 수는 없지만 자식 객체가 생성될 때 super(...)를 호출해서
추상 클래스 객체를 생성하므로 추상 클래스도 생성자가 반드시 있어야 한다.
 */

// 추상 클래스
public abstract class Phone {
    //field
    public String owner;

    //constructor
    public Phone(String owner) {
        this.owner = owner;
    }

    //method
    public void turnOn() {
        System.out.println("폰 전원을 켭니다.");
    }
    public void turnOff() {
        System.out.println("폰 전원을 끕니다.");
    }
}

// 실체클래스
public class SmartPhone extends Phone {
    //constructor
    public SmartPhone(String owner) {
        super(owner);
    }
    //method
    public void internetSearch() {
        System.out.println("인터넷 검색을 합니다.");
    }
}

// 실행클래스
public class PhoneExample {
    public static void main(String[] args) {
        // Phone phone = new Phone();

        // phone의 메서드
        SmartPhone smartPhone = new SmartPhone("홍길동");
        smartPhone.internetSearch();
        smartPhone.turnOff();
    }
}

/*
추상 클래스는 실체 클래스의 공통되는 필드와 메서드를 추출해서 만들었기 때문에 객체를 직접 생성해서 사용할 수 없다.
Animal animal = new Aninal();   (x)

추상 클래스는 새로운 실체 클래스를 만들기 위해 부모 클래스만 사용된다. 코드로 설명하면 추상 클래스는 extends 뒤에만 올 수 있는 클래스다.
class Ant extends Animal {...} (o)
 */
