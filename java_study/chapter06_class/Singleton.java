/*Singleton

전체 프로그램에서 단 하나의 객체만 만들도록 보장해야 하는 경우가 있다. 단 하나만 생성된다고 해서 이 객체를 싱글톤 Singleton이라고 한다.
싱글톤을 호출하려면 클래스 외부에서 new 연산자로 생성자를 호출할 수 없도록 막아야 한다. 생성자를 호출한 만큼 객체가 생성되기 때문이다.
생성자를 외부에서 호출할 수 없도록 하려면 생성자 앞에 private 접근 제한자를 붙여주면 된다.
접근 제한자는 나중에 설명하기로 하고, 여기서는 외부에서 생성자 호출을 막기 위해 private를 붙여준다는 것만 알아두자.

그리고 자신의 타입인 정적 필드를 하나 선언하고 자신의 객체를 생성해 초기화한다. 참고로 클래스 내부에서는 new 연산자로 생성자 호출이 가능하다.
정적 필드로 private 접근 제한자를 붙여 외부에서 필드값을 변경하지 못하도록 막는다. 대신 외부에서 호출할 수 있는 정적 메서드인 getInstance()
를 선언하고 정적 필드에서 참조하고 있는 자신의 객체를 리턴해준다.
 */
public class Singleton {
    // 정적 필드
    private static Singleton singleton = new Singleton();

    // 생성자
    private Singleton() {}

    // 정적 메서드-> 호출
    static Singleton getInstance() {
        return singleton;
    }
}

public class SingletonExample {
    public static void main(String[] args) {
        /*
        Singlenton obj1 = new Singleton();
        Singlenton obj2 = new Singleton();
         */

        Singleton obj1 = Singleton.getInstance();
        Singleton obj2 = Singleton.getInstance();

        if (obj1 == obj2) {
            System.out.println("같은 Singleton 객체입니다.");
        } else {
            System.out.println("다른 Singleton 객체입니다.");
        }
    }
}