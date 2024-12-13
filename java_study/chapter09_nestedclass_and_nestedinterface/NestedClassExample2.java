/*
중첩 클래스의 접근 제한

멤버 클래스 내부에서 바깥 클래스의 필드와 메서드에 접근할 때는 제한이 따른다.
또한 메서드의 매개 변수나 로컬 변수를 로컬 클래스에서 사용할 때도 제한이 따른다.

# 바깥 필드와 메서드에서 사용 제한
바깥 클래스에서 인스턴스 멤버 클래스를 사용할 때 제한이 있다.
 */
public class A {
    //instance field
    B field1 = new B();
    C field2 = new C();

    //instance method
    void method1() {
        B var1 = new B();
        C var2 = new C();
    }

    //static filed init
    static void method2() {
        //B var1 = new B();
        C var2 = new C();
    }

    //instance member class
    class B { }

    //static member class
    static class C { }
}