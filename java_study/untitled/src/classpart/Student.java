package classpart;

public class Student {
    int studentId;          // 학번
    String studentName;     // 학생 이름
    int grade;              // 학년
    String address;         // 사는 곳

    public void showStudentInfo() {
        System.out.println(studentName + ", " + address);   // 이름, 주소 출력
    }
}
