package constructor;

public class Person {
    String name;
    float height;
    float weight;

    public Person() { } // 디폴트 생성자 추가 

    public Person(String pname) {
        name = pname;   // 사람 이름을 매개변수로 입력 받아서 Person 클래스를 생성하는 생성자 구현
    }
}
