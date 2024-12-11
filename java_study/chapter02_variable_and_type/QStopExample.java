/*q를 입력하면 반복 종료*/
public class QStopExample {
    public static void main(String[] args) throws Exception {
        int KeyCode;

        while(true) {
            KeyCode = System.in.read();
            System.out.println("KeyCode : " + KeyCode);
            if (KeyCode == 113) {
                break;  // KeyCode가 113일 경우 while 반복을 중지함
            }
        }
        System.out.println("종료");
    }
}