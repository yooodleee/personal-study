// 파일 읽기

// ... (생략) ...
file_reader_original *reader = nullptr; // 파일 리더 포인터 선언
reader = file_reader_original::get_reader_instance();   // 파일 리더 인스턴스 생성
if (nullptr != reader) {
    reader->read_countents();   // 파일 읽기
    delete reader;  // 파일 리더 소멸

}

return 0;

/*
파일의 버전에 따른 영향이 전혀 없음. 만약 새로운 버전을 구현한 클래스가 추가되더라도 해당 클래스를
대상으로 유연하게 동작함. get_reader_instance()로 파일 리더기를 반환받아 read_contents()로 파일을 
읽고 해석함. 반환된 클래스는 파일 버전과 일치하는 클래스이며, read_contents()는 버전에 적합하게 정의된 
멤버 함수가 동작함. 
*/

/*
get_reader_instance()는 정적(static) 멤버 함수. 파일 리더기를 생성해서 반환하는 역할은 모든
파일 읽기 인스턴스에서 할 필요가 없기 때문이다. 인스턴스 생성을 별도의 클래스로 분리하는 것이 더 좋은 
설계이지만, 지금은 부모 클래스의 정적 멤버 함수로 구현함. 
*/

/*
팩토리 패턴(factory pattern) 설계 방식

인스턴스를 생성하는 별도의 팩토리 클래스를 도입하여 인스턴스 생성을 캡슐화한다.
이렇게 하면 유연성을 높이고 인스턴스가 생성되는 방식을 쉽게 변경할 수 있다. 
*/