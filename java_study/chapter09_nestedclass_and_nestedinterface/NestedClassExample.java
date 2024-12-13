/*중첩 클래스*/

// 바깥 클래스
class A {
    A() {System.out.println("A 객체가 생성됨");}

    // 인스턴스 멤버 클래스
    class B {
        B() {System.out.println("B 객체가 생성됨");}
        int field1;
        //static int field2;
        void method1() { }
        //static void method2() { }
    }

    // 정적 멤버 클래스
    static class C {
        C() {System.out.println("C 객체가 생성됨");}
        int field1;
        static int field2;
        void method1() { }
        static void method2() { }
    }

    void method() {
        // 로컬 클래스
        class D {
            D() {System.out.println("D 객체가 생성됨");}
            int field1;
            //static int field2;
            void method1() { }
            //static void method2() { }
        }
        D d = new D();
        d.field1 = 3;
        d.method1();
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();

        //인스턴스 멤버 클래스 객체 생성
        A.B b = a.new B();
        b.field1 = 3;
        b.method1();

        //정적 멤서 클래스 객체 생성
        A.C c = new A.C();
        c.field1 = 3;
        c.method1();
        A.C.field2 = 3;
        A.C.method2();

        //로컬 클래스 객체 생성을 위한 메서드 호출
        a.method();
    }
}