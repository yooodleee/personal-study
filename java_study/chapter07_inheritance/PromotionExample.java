// 자동 타입 변환 후의 멤버 접근
// 부모클래스
public class Parent {
    public void method() {
        System.out.println("Parent-mehtod()");
    }

    public void method2() {
        system.out.println("Parent-method2()");
    }
}

// 자식클래스
public class Child extends Parent {
    @java.lang.Override
    public void method2() {
        System.out.println("Child-method2()");
    }   // 재정의

    public void method3() {
        System.out.println("Child-method3()");
    }
}

public class ChildExample {
    public static void main(String[] args) {
        Child child = new Child();

        Parent parent = child;  // 자동 타입 변환
        parent.method();
        parent.method2();   // 재정의된 메서드가 호출됨
        // parent.method3();    호출 불가능
    }
}