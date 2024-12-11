/*키보드에서 입력된 내용을 문자열로 얻기*/
import java.util.Scanner

public class ScannerExample {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String inputData;

        while(true) {
            inputData = scanner.nextLine();
            System.out.println("입력된 문자열 : \"" + inputData + "\"");
            if (inputData.equals("q")) {
                break;
            }
        }
        System.out.println("종료")
    }
}
/*
System.in.read()의 단점은 코드를 하나씩 읽기 때문에 2개 이상의 키가 조합된 한글을 읽을 수 없다는 것이다.
그리고 키보드로부터 입력된 내용을 통 문자열로 읽지 못한다. 이러한 단점을 보완하기 위해 자바는 Scanner 클래스를 제공하고 있다.

Scanner scanner는 Scanner 타입의 변수 scanner를 선언한다.
new Scanner(System.in)은 시스템의 입력 장치로부터 읽는 Scanner를 생성하는 코드이다. 생성된 Scanner는 scanner 변수에 저장했다가
언제든지 키보드에서 읽고 싶을 때 scanner.nextLine() 메서드를 실행하면 된다.
scanner.nextLine() 메서드는 Enter 키가 입력되기 전까지 대기 상태가 되며, Enter 키가 입력되면 입력된 모든 내용을 문자열로 읽는다.


QStopExamle.java에서는 System.in.read()로 읽었기 때문에 int 타입의 키코드를 읽었고, ScannerExample.java에서는 scanner.nextLine()으로
읽었기 때문에 String 타입의 문자열을 얻었다.

자바는 기본 타입의 값이 동일한지 비교할 때 ==를 사용하고, 문자열(String)이 동일한지 비교할 때에는 equals() 메서드를 사용한다.
 */