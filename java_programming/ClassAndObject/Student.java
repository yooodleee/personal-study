package ClassAndObject;

public class Student {
    // 멤버 변수
    int studentId;          // 학번
    String studentName;     // 이름
    int grade;              // 학년
    String address;         // 주소

    public void showStudentInfo() {
        System.out.println(studentName + ", " address); // 이름, 주소 출력
    }
}
