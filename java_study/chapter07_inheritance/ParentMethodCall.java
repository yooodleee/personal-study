// super 변수
public class Airplane {
    public void land() {
        System.out.println("착륙합니다.");
    }
    public void fly() {
        System.out.println("일반비행합니다.");
    }
    public void takeOff() {
        System.out.println("이륙합니다.");
    }
}

// super 변수
public class SupersonicAirpline extends Airplane {
    public static final int NORMAL = 1;
    public static final int SUPERSONIC = 2;

    public int flyMode = NORMAL;

    @java.lang.Override
    public void fly() {
        if(flyMode == SUPERSONIC) {
            System.out.println("초음속비행합니다.");
        } else {
            super.fly();    // Airplane 객체의 fly() 메서드 호출
        }
    }
}

// super 변수
public class SupersonicAirplaneExample {
    public static void main(String[] args) {
        SupersonicAirpline sa = new SupersonicAirpline();
        sa.takeOff();
        sa.fly();
        sa.flyMode = SupersonicAirpline.SUPERSONIC;
        sa.fly();
        sa.flyMode = SupersonicAirpline.NORMAL;
        sa.fly();
        sa.land();
    }
}