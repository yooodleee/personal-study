/*
인터페이스 상속

public interface 하위인터페이스 extends 상위인터페이스1, 상위인터페이스2 {...}

하위 인터페이스를 구현하는 클래스는 하위 인터페이스의 메서드뿐만 아니라 상위 인터페이스의 모든 추상 메서드에 대한 실체 메서드를
가지고 있어야 한다. 그렇기 때문에 구현 클래스로부터 객체를 생성한 후에 다음과 같이 하위 및 상위 인터페이스 타입으로 변환이 가능하다.

하위인터페이스 변수 = new 구현클래스(...);
하위인터페이스1 변수 = new 구현클래스(...);
하위인터페이스2 변수 = new 구현클래스(...);
하위인터페이스3 변수 = new 구현클래스(...);

하위 인터페이스로 타입 변환이 되면 상위 및 하위 인터페이스에 선언된 모든 메서드를 사용할 수 있으나,
상위 인터페이스로 타입 변환되면 상위 인터페이스에 선언된 메서드만 사용 가능하고 하위 인터페이스에 선언된 메서드는 사용할 수 없다.
 */
public interface InterfaceA {
    public void methodA();
}

public interface InterfaceB {
    public void methodB();
}

public interface InterfaceC extends InterfaceA, InterfaceB {
    public void methodC();
}

public class ImplementationC implements InterfaceC {
    public void methodA() {
        System.out.println("ImplementationC-methodA() 실행");
    }

    public void methodB() {
        System.out.println("ImplementationC-methodB()");
    }

    public void methodC() {
        System.out.println("ImplementationC-methodC()");
    }
}

public class Example {
    public static void main(String[] args) {
        ImplementationC impl = new ImplementationC();

        InterfaceA ia = impl;
        ia.methodA();   // InterfaceA 변수는 methodA()만 호출 가능

        InterfaceB ib = impl;
        ib.methodB();   // InterfaceB 변수는 methodB()만 호출 가능
        System.out.println();

        InterfaceC ic = impl;
        ic.methodC();
        ic.methodB();
        ic.methodA();
    }
}