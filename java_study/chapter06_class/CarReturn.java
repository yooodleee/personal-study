public class Car {
    //field
    int gas;

    //constructor

    //method
    void setGas(int gas) {
        this.gas = gas; // 리턴값이 없는 메서드로 매개값을 받아서 gas 필드값을 변경
    }

    boolean isLetGas() {
        if(gas == 0) {
            System.out.println("gas가 없습니다.");
            return false;   // false를 리턴
        }
        System.out.println("gas가 있습니다.");
        return true;    // true를 리턴
    }   // 리턴값이 boolean인 메서드로 gas 필드값이 0이면 false, 0이 아니면 true를 리턴

    void run() {
        while (true) {
            if(gas > 0) {
                System.out.println("달립니다.(gas잔량:" + gas + ")");
                gas -= 1;
            } else {
                System.out.println("멈춥니다.(gas잔량:" + gas + ")");
                return; // 메서드 실행 종료
            }   // 리턴값이 없는 메서드로 gas 필드값이 0이면 return 문으로 메서드를 강제 종료
        }
    }

    public class CarExample {
        public static void main(String[] args) {
            Car myCar = new Car();

            myCar.setGas(5);    // Car의 setGas() 메서드 호출

            boolean gasState = myCar.isLetGas();    // Car의 isLeftGas() 메서드 호출
            if(gasState) {
                System.out.println("출발합니다.");
                myCar.run();    // Car의 run() 메서드 호출
            }

            if(myCar.isLetGas()) {  // Car의 isLeftGas() 메서드 호출
                System.out.println("gas를 주입할 필요가 없습니다.");
        } else {
                System.out.println("gas를 주입하세요");
            }
    }
}