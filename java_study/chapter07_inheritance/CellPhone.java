// 부모 클래스
public class CellPhone {
    //field
    String model;
    String color;

    //constructor

    //method
    void powerOn() {System.out.println("전원을 켭니다.");}
    void pwerOff() {System.out.println("전원을 끕니다.");}
    void bell() {System.out.println("벨이 울립니다.");}
    void sendVoice(String message) {System.out.println("자기: " + message);}
    void receiveVoide(String message) {System.out.println("상대방: " + message);}
    void hangUp() {System.out.println("전화를 끊습니다.");}
}

//자식 클래스
public class DmCellPhone extends CellPhone {
    //field
    int channel;

    //contstructor
    DmCellPhone(String model, String color, int channel) {
        this.model = model;
        this.color = color;
        this.channel = channel;
    }

    //method
    void turnOnDmb() {
        System.out.println("채널 " + channel + "번 DMB 방송 수신을 시작합니다.");
    }
    void changeChannelDmb(int channel) {
        this.channel = channel;
        System.out.println("채널 " + channel + "번으로 바꿉니다.");
    }
    void turnOffDmb() {
        System.out.println("DMB 방송 수신을 멈춥니다.");
    }
}

// 자식 클래스 사용
public class DmbCellPhoneExample {
    public static void main(String[] args) {
        //DmbCellPhone 객체 생성
        DmCellPhone dmbCellPhone = new DmCellPhone("자바폰", "검정", 10);

        //CellPhone 클래스로부터 상속받은 필드
        System.out.println("모델: " + dmbCellPhone.model);
        System.out.println("색상: " + dmbCellPhone.color);

        //DmbCellPhone 클래스의 필드
        System.out.println("채널: " + dmbCellPhone.channel);

        //CellPhone 클래스로부터 상속받은 메서드 호출
        dmbCellPhone.powerOn();
        dmbCellPhone.bell();
        dmbCellPhone.sendVoice("여보세요.");
        dmbCellPhone.receiveVoide("안녕하세요! 저는 홍길동인데요.");
        dmbCellPhone.sendVoice("아~예 반갑습니다.");
        dmbCellPhone.hangUp();

        //DmbCellPhone 클래스의 메서드 호출
        dmbCellPhone.turnOnDmb();
        dmbCellPhone.changeChannelDmb(12);
        dmbCellPhone.turnOffDmb();
    }
}