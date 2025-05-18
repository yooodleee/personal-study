package thisex;


class BirthDay {
    int day;
    int month;
    int year;
}

public void setYear(int year) {
    this.year = year;
}

public void printThis() {
    System.out.println(this);       // this 출력 메서드
}

public class ThisExample {
    public static void main(String[] args) {
        BirthDay bDay = new BirthDay();
        bDay.setYear(2000);         // 태어난 연도를 2000으로 지종
        System.out.println(bDay);   // 참조 변수 출력
        bDay.printThis();           // this 출력 메서드 호출
    }
}
