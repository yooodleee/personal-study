public class CantUseThisForStaticMethod {
    int speed;

    void run() {
        System.out.println(speed + "으로 달립니다.");
    }

    public static void main(String[] args) {
        CantUseThisForStaticMethod myCar = new CantUseThisForStaticMethod();
        myCar.speed = 60;
        myCar.run();
    }
}