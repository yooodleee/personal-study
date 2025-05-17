package reference;

public class Student4 {
    int studentID;
    String studentName;
    Subject2 korean;
    Subject2 math;

    public Student4(int studentID, String studentName) {
        this.studentID = studentID;
        this.studentName = studentName;

        korean = new Subject2();
        math = new Subject2();  // 변수 krean과 math의 인스턴스 생성
    }

    public void showStudentInfo() {
        System.out.println(studentName + "님의" + korean.getSubjectName() +
                "과목의 점수는 " + korean.getScorePoint() + "점이며" + math.getSubjectName() +
                "과목의 점수는 " + math.getScorePoint() + "접입니다.");
    }

    public void setKoreanSubject(String subjectName, int score) {
        korean.setSubjectName(subjectName);
        korean.setScorePoint(score);    // 매개변수로 넘긴 값을 이용해 subject 메서드를 호출하고 값을 대입
    }

    public void setMathSubject(String subjectName, int score) {
        math.setSubjectName(subjectName);
        math.setScorePoint(score);
    }
}
