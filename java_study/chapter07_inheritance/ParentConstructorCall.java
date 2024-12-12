// 부모 클래스
public class ParentConstructorCall {
    public String name;
    public String ssn;

    public ParentConstructorCall(String name, String ssn) {
        this.name = name;
        this.ssn = ssn;
    }
}

// 자식 클래스
public class Child extends ParentConstructorCall {
    public int childNo;

    public Child(String name, String ssn, int childNo) {
        super(name, ssn);   // 부모 생성자 호출
        this.childNo = childNo;
    }
}

// 자식 객체 이용
public class ChildExample {
    public static void main(String[] args) {
        Child child = new Child("홍길동", "123456-1234567", 1);
        System.out.println("name : " + child.name);
        System.out.println("ssn : " + child.ssn);
        System.out.println("childNo : " + child.childNo);
    }
}