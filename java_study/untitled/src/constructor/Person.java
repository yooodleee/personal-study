package constructor;

public class Person {
    String name;
    float height;
    float weight;

    public Person() { } // 디폴트 생성자 추가

    public Person(String pname) {
        name = pname;   // 사람 이름을 매개변수로 입력 받아서 Person 클래스를 생성하는 생성자 구현
    }

    public Person(String pname, float pheight, float pweight) { // 이름, 키, 몸무게를 매개변수로 입력받는 생성자
        name = pname;
        height = pheight;
        weight = pweight;
    }
}
