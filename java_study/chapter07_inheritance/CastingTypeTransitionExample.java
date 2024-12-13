/*
강제 타입 변환 Casting

강제 타입 변환은 부모 타입을 자식 타입으로 변환하는 것을 말한다. 그렇다고 해서 모든 부모 타입을 자식 타입으로
강제 변환할 수 있는 것은 아니다. 자식 타입이 부모 타입으로 자동 타입 변환한 후 다시 자식 타입으로 변환할 때 강제 타입 변환을
사용할 수 있다.
자식타입 변수 = (자식 타입) 부모타입; // 부모 타입을 자식 타입으로 변환

예를 들어 다음 코드와 같이 Child 객체가 Parent 타입으로 자동 변환된 상태에서 원래 Child로 강제 변환할 수 있다.
Parent parent = new Child();    // 자동 타입 변환
Child child = (Child) parent;   // 강제 타입 변환

자식 타입이 부모 타입으로 자동 타입 변환하면, 부모에 선언된 필드와 메서드만 사용 가능하다는 제역 사항이 따른다.
만약 자식에 선언된 필드와 메서드를 꼭 사용해야 한다면 강제 타입 변환을 해서 다시 자식 타입으로 변환한 다음 자식의 필드와 메서드를 사용하면 된다.

// Parent
class Parent {
    String field;
    void method1() {...};
    void method2() {...};
}

// Child
class Child extentds Parent {
    Sting field2;
    void method3() {...};
}

// ChildExample
class ChildExample {
    public static void main(String[] args) {
        Parent parent = new Child();    // 자동 타입 변환
        parent.field1 = "xxx";
        parent.method1();
        parent.method2();
        parent.field2 = "yyy";  // 불가능
        parent.method3();   // 불가능

        Child child = (Child) parent;   // 강제 타입 변환
        child.field2 = "yyy";   // 가능
        child.method3();    // 가능
        }
}

field2 필드와 method3() 메서드는 Child 타입에만 선언되어 있으므로 Parent 타입으로 자동 타입 변환하면 사용할 수 없다.
field2 필드와 method3() 메서드를 사용하고 싶다면 다시 Child 타입으로 강제 타입 변환을 해야 한다.
 */

// 부모클래스
public class Parent {
    public String field1;

    public void method1() {
        System.out.println("Parent-method1()");
    }

    public voidk method2() {
        System.out.println("Parent-method2()");
    }
}

// 자식클래스
public class Child extends Parent {
    public String filed2;

    public void method3() {
        System.out.println("Child-method3()");
    }
}

// Casting
public class ChildExample {
    public static void main(String[] args) {
        Parent parent = new Child();    // 자동 타입 변환
        parent.field1 = "data1";
        parent.method1();
        parent.method2();

        /*
        parent.field2 = "data2";
        parent.method3();   // 불가능
         */

        Child child = (Child) parent;   // 자동 타입 변환
        child.filed2 = "yyy";
        child.method3();
    }
}