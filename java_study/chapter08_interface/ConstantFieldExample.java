/*
상수 필드 선언

인터페이스는 객체 사용 방법을 정의한 것이므로 실행 시 데이터를 저장할 수 있는 인스턴스 또는 정적 필드를 선언할 수 없다.
그러나 상수 필드 Constant Field는 선언이 가능하다. 단, 상수는 인터페이스에 고정된 값으로 실행 시에 데이터를 바꿀 수 없다.

상수는 public static final로 선언한다. 따라서 인터페이스에 선언된 필드는 모두 public static final의 특성을 갖는다.
public static final을 생략하더라도 컴파일 과정에서 자동으로 붙게 된다.
[public static final] 타입 상수이름 = 값;
 */
public interface RemoteControl {
    public int MAX_VOLUME = 10;
    public int MIN_VOLUME = 0;
}