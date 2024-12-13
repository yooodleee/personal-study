/*
객체 타입 변환

강제 타입 변환은 자식 타입이 부모 타입으로 변환되어 있는 상태에서만 가능하기 때문에 다음과 같이 처음부터 부모 타입으로 생성된 객체는
자식 타입으로 변환할 수 없다.
Parent parent = new Parent();
Child child = (Child) parent;   // 강제 타입 변환할 수 없음

그렇다면 부모 변수는 참조하는 객체가 부모 객체인지 자식 객체인지 확인하는 방법은 없을까?
어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해 instanceof 연산자를 사용한다.
instanceof 연산자의 좌항에는 객체가 오고 우항에는 타입이 오는데, 좌항의 객체가 우항의 인스턴스라면, 즉 우항의 타입으로 객체가 생성되었다면
true를 리턴하고 그렇지 않으면 false를 리턴한다.
boolean result = 좌항(객체) instanceof 우항(타입)

instanceof 연산자는 주로 매개값의 타입을 조사할 때 사용한다. 메서드 내에서 강제 타입 변환이 필요할 경우 반드시 매개값이 어떤 객체인지
instanceof 연산자로 확인하고 안전하게 강제 타입 변환을 해야 한다.
public void method(Parent parent) { // parent-> Parent, Child 객체
    if(parent instanceof Child) {   // parent 매개 변수가 참조하는 객체가 child인지 조사
        Child child = (Child) parent;
        }
}

만약 타입을 확인하지 않고 강제 타입 변환을 시도하면 ClassCastException이 발생할 수 있다.
 */

// 부모클래스
public class Parent {
}

// 자식클래스
public class Child extends Parent {

}

// 객체 타입 확인
public class InstanceofExample {
    public static void method1(Parent parent) {
        if(parent instanceof Child) {   // Child 타입으로 변환이 가능한지 확인
            Child child = (Child) parent;
            system.out.println("method1-Child 타입 변환 성공");
    } else {
            System.out.println("method1-Child 타입 변환 실패");
        }
}

public static void method2(Parent parent) {
    Child child = (Child) parent;   // ClassException이 발생할 가능성 있음
    System.out.println("method2-Chile 변환 성공");
}

public static void main(String[] args) {
    Parent parentA = new Child();
    method1(parentA);
    method2(parentA);   // Child 객체를 매개값으로 전달

    Parent parentB = new Parent();
    method1(parentB);
    method2(parentB);   // Parent 객체를 매개값으로 전달
    }
}
/*
InstanceofExample 클래스에서 method1()과 method2()를 호출할 경우, CHild 객체를 매개값으로 전달하면 두 메서드 모두 예외가 발생하지 않지만,
Parent 객체를 매개값으로 전달하면 method2()에서는 ClassCastException이 발생한다. method1()은 instanceof 연산자로 변환이 가능한지 확인
한 후 변환을 하지만, method2()는 무조건 변환하려고 했기 떄문이다.

예외가 발생하면 프로그램은 즉시 종료되기 때문에 method1()과 같이 강제 타입 변환을 하기 전에 instanceof 연산자로 변환시킬 타입의 객체인지
조사해서 잘못된 매개값으로 인해 프로그램이 종료되는 것을 막아야 한다.
 */