/*break 문이 없는 case*/
public class SwitchNoBreakCaseExample {
    public static void main(String[] args) {
        int time = (Math.random() * 4) + 8; // 8<=...<=11사이의 정수 뽑기
        System.out.println("[현재 시각: " + time + " 시]");

        switch (time) {
            case 8:
                System.out.println("출급합니다.");
            case 9:
                System.out.println("회의를 합니다.");
            case 10:
                System.out.println("업무를 봅니다.");
            case 11:
                System.out.println("외근을 나갑니다.");
        }
    }
}