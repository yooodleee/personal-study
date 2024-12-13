/*
인터페이스 구현

개발 코드가 인터페이스 메서드를 호출하면 인터페이스는 객체의 메서드를 호출한다.
객체는 인터페이스에서 정의된 추상 메서드와 동일한 메서드 이름, 매개 타입, 리턴 타입을 가진 실체 메서드를 가지고 있어야 한다.
이러한 객체를 인터페이스의 구현(implement) 객체라고 하고, 구현 객체를 생성하는 클래스를 구현 클래스라고 한다.

* 구현 클래스
구현 클래스는 보통 클래스와 동일한데, 인터페이스 타입으로 사용할 수 있음을 알려주기 위해 클래스 선언부에 implements 키워드를 추가하고 인터페이스
이름을 명시해야 한다. 그리고 인터페이스에 선언된 추상 메서드의 실체 메서드를 선언해야 한다.
public class 구현클래스이름 implements 인터페이스이름 {
    //인터페이스에 선언된 추상 메서드의 실체 메서드 선언
}
 */
public interface RemoteControl {
    //constant
    public int MAX_VOLUME = 10;
    public int MIN_VOLUME = 0;

    //abstract method
    public void turnOn();
    public void turnOff();
    public void setVolume(int volume);
}

public class Television implements RemoteControl {
    //field
    private int volume;

    //turnOn() 추상 메서드의 실체 메서드
    public void turnOn() {
        System.out.println("TV를 켭니다.");
    }
    //turnOff() 추상 메서드의 실체 메서드
    public void turnOff() {
        System.out.println("TV를 끕니다.");
    }
    //setVolume() 추상 메서드의 실체 메서드
    public void setVolume(int volume) {
        if(volume > RemoteControl.MAX_VOLUME) {
            this.volume = RemoteControl.MAX_VOLUME;
        } else if(volume < RemoteControl.MIN_VOLUME) {
            this.volume = RemoteControl.MIN_VOLUME;
        } else {
            this.volume = volume;
        }
        System.out.println("현재 TV 볼륨 : " + this.volume);
    }
}

public class Audio implements RemoteControl {
    //field
    private int volume;

    //turnOn() 추상 메서드의 실체 메서드
    public void turnOn() {
        System.out.println("Audio를 켭니다.");
    }
    //turnOff() 추상 메서드의 실체 메서드
    public void turnOff() {
        System.out.println("Audio를 끕니다.");
    }
    //setVolume() 추상 메서드의 실체 메서드
    public void setVolume(int volume) {
        if(volume > RemoteControl.MAX_VOLUME) {
            this.volume = RemoteControl.MAX_VOLUME;
        } else if(volume < RemoteControl.MIN_VOLUME) {
            this.volume = RemoteControl.MIN_VOLUME;
        } else {
            this.volume = volume;
        }
        System.out.println("현재 Audio 볼륨 : " + this.volume);
    }
}

public class RemoteControlExample {
    public static void main(String[] args) {
        RemoteControl rc;
        rc = new Television();
        rc = new Audio();
    }
}

public class Searchable {
    void search(String url);
}

// 다중 인터페이스 구현 클래스
public class SmartTelevision implements RemoteControlExample, Searchable {
    private int volume;

    public void turnOn() {
        System.out.println("TV를 켭니다.");
    }
    public void turnOff() {
        System.out.println("TV를 끕니다.");
    }
    public void setVolume(int volume) {
        if(volume > RemoteControl.MAX_VOLUME) {
            this.volume = RemoteControl.MAX_VOLUME;
        } else if (volume < RemoteControl.MIN_VOLUME) {
            this.volume = RemoteControl.MIN_VOLUME;
        } else {
            this.volume = volume;
        }
        System.out.println("현재 TV 볼륨 : " + this.volume);
    }

    public void search(String url) {
        System.out.println(url + "을 검색합니다.");
    }
}

// 인터페이스 변수에 구현 객체 대입
public class SmartTelevisionExample {
    public static void main(String[] args) {
        SmartTelevision tv = new SmartTelevision();

        RemoteControl rc = tv;
        Searchable searchable = tv;
    }
}

// 인터페이스 사용
public class MyClass {
    //field
    RemoteControl rc = new Television();

    //constructor
    MyClass() {
    }

    MyClass(RemoteControl rc) {
        this.rc = rc;
        rc.turnOn();
        rc.setVolume(5);
    }

    //method
    void methodA() {
        RemoteControl rc = new Audio();
        rc.turnOn();
        rc.setVolume(5);
    }

    void methodB(RemoteControl rc) {
        rc.turnOn();
        rc.setVolume(5);
    }
}

public class MyClassExample {
    public static void main(String[] args) {
        System.out.println("1)------------------");

        MyClass myClass1 = new MyClass();
        myClass1.rc.turnOn();
        myClass1.rc.setVolume(5);

        System.out.println("2)-----------------");

        MyClass myClass2 = new MyClass(new Audio());

        System.out.println("3)----------------");

        MyClass myClass3 = new MyClass();
        myClass3.methodA();

        System.out.println("4)----------------");

        MyClass myClass4 = new MyClass();
        myClass4.methodB(new Television());
    }
}