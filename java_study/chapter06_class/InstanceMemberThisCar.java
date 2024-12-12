public class InstanceMemberThisCar {
    //field
    String model;
    int speed;

    //constructor
    InstanceMemberThisCar(String model) {
        this.model = model;
    }

    //method
    void setSpeed(int speed) {
        this.speed = speed;
    }

    void run() {
        for(int i=10;i<=50;i++) {
            this.setSpeed(i);
            System.out.println(this.model + "가 달립니다.(시속:" + this,speed + "km/h");
        }
    }
}

public class CarExample {
    public static void main(String[] args) {
        InstanceMemberThisCar myCar = new InstanceMemberThisCar("포르쉐");
        InstanceMemberThisCar yourCar = new InstanceMemberThisCar("벤츠");

        myCar.run();
        yourCar.run();
    }
}