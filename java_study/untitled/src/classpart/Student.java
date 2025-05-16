package classpart;

public class Student {
    int studentId;          // 학번
    String studentName;     // 학생 이름
    int grade;              // 학년
    String address;         // 사는 곳

    public void showStudentInfo() {
        System.out.println(studentName + ", " + address);   // 이름, 주소 출력
    }

    public String getStudentName() {
        return studentName; // studnetName을 반환하는 get() 메서드 구현
    }

    public void setStudentName(String name) {
        studentName = name;
    }

    public static void main(String[] args) {
        Student studentAhn = new Student(); // Student 클래스 생성
        studentAhn.studentName = "안연수";

        System.out.println(studentAhn.studentName);
        System.out.println(studentAhn.getStudentName());
    }
}
