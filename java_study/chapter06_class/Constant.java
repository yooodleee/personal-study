/*
final 필드를 상수라고 부르지는 않는다.
왜냐하면 불변의 값은 객체마다 저장할 필요가 없는 공용성을 띠고 있으며, 여러 가지 값으로 초기화될 수 없기 때문이다.
final 필드는 객체마다 저장되고, 생성자의 매개값을 통해서 여러 가지 값을 가질 수 있기 때문에 상수가 될 수 없다.

상수는 final이면서 static이어야 한다. static final 필드는 객체마다 존재하지 않고 클래스에만 존재한다.
그리고 한 번 초기값이 저장되면 변경할 수 없다.
 */
import  Math

public class Constant {
    static final double EARTH_RADIUS = 6400;
    static final double EARTH_AREA = 4 * Math.PI * EARTH_RADIUS * EARTH_RADIUS;
}

public class EarthExample {
    public static void main(String[] args) {
        System.out.println("지구의 반지름 : " + Constant.EARTH_RADIUS + "km");
        System.out.println("지구의 표면적 : " + Constant.EARTH_AREA + "km^2");
    }
}