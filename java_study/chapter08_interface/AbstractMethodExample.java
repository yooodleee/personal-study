/*
추상 메서드 선언

인터페이스를 통해 호출된 메서드는 최종적으로 객체에서 실행된다. 그렇기 때문에 인터페이스의 메서드는 실행 블록이 없는 추상 메서드로 선언한다.
추상 메서드는 리턴 타입, 메서드 이름, 매개 변수만 기술되고 중괄호를 붙이지 않고 메서드를 말한다. 인터페이스에 선언된 추상 메서드는 모두
public abstrcat의 특성을 갖기 때문에 public abstract를 생략하더라도 컴파일 과정에서 자동으로 붙게 된다.
[public abstract] 리턴타입 메서드이름(매개변수, ...);
 */
public interface RemoteControl {
    //constant
    public int MAX_VOLUME = 10;
    public int MIN_VOLUME = 0;

    //abstract method       메서드 선언부만 작성
    public void turnOn();
    public void turnOff();
    public void setVolume(int volume);
}