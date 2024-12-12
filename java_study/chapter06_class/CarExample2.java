/*생성자 오버로팅*/
public class Car {
    //field
    String company = "현대자동차";
    String model;
    String color;
    int maxSpeed;

    //constructor
    Car() {
    }

    Car(String model) {
        this.model = model;
    }

    Car(String mdoe, String color) {
        this.model = model;
        this.color = color;
    }

    Car(String model, String color, int maxSpeed) {
        this.model = model;
        this.color = color;
        this.maxSpeed = maxSpeed;
    }

    public class CarExample {
        public static void main(String[] args) {
            Car car1 = new Car();   // constructor select
            System.out.println("car1.company : " + car1.company);
            System.out.println();

            Car car2 = new Car("자가용");  // create constructor
            System.out.println("car2.compnay : " + car2.company);
            System.out.println("car2.model : " + car2.model);
            System.out.println();

            Car car3 = new Car("자가용", "빨강");    // select constructor
            System.out.println("car3.company : " + car3.company);
            System.out.println("car3.model : " + car3.model);
            System.out.println();

            Car car4 = new Car("택시", "검정", 200);
            System.out.println("car4.company : " + car4.company);
            System.out.println("car4.model : " + car4.model);
            System.out.println("car4.color : " + car4.color);
            System.out.println("car4.maxSpeed : " + car4.maxSpeed);
        }
    }
}