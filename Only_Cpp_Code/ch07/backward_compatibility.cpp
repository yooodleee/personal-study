// 파일 읽기 인스턴스 생성

/**
 * 다형성이란 무엇일까? 
 * 
 * 다형성(Polymorphism)은 상속받은 클래스들이 부모와 다른 다양한 특성을 가지는 것을 말한다. 
 * 객체지향 프로그래밍을 설명하면서 살펴본 엔진의 예를 다시 생각해보자. 자동차 엔진은 연료를
 * 소모하여 발생한 운동 에너지를 바퀴로 전달한다. 가솔린과 디젤, 가스, 전기 엔진은 연료만
 * 다를 뿐 엔진이라는 사실은 변함이 없다. 
 * 
 * 이처럼 상위 개념(부모 클래스)의 역할을 대신할 수 있으며 각자의 고유한 특징으로 동작하는 
 * 것이 다형성이다. 새로운 연료를 사용하는 엔진이 만들어지거나 연료를 사용하지 않고 동력을
 * 생산하는 다른 방식이 생기더라도 엔진이라는 형식이 변경되지 않는 한 다형성으로 수용할 수 있다. 
 * 
 * 다형성은 앞으로 만들 새로운 기능을 예상할 수는 없지만, 꼭 해야 할 역할이나 기능을 호출하는
 * 방식은 고정하여 실현할 수 있다. 다형성을 적용하면 새로운 기능이 추가될 때 호출하는 소스 코드는
 * 변경하지 않고, 새로운 클래스를 정의하는 것만으로 기능을 확장할 수 있다. 
 * 
 * 다형성을 활용한 유지 / 보수성 향상
 * 
 * 다형성은 하위 호환성(backward compatibility)을 처리할 때도 사용된다. 하위 호환성이란, 예컨대 
 * 새로운 버전(v2.0)의 소프트웨어가 이전 버전(v1.0)에서 생성한 파일을 읽을 수 있는 것을 말한다. 
 * 하위 버전 호환성을 구현하는 방법은 다양하지만 다형성을 이용하면 유연하고 유지 / 보수가 편리한 
 * 코드로 구현할 수 있다. 
 * 
 * 예컨대 파일을 읽고 처리하는 부분의 코드를 살펴보자. 
 * 
 * ...(생략)... 
 * file_reader_original *reader = nullptr;  // 파일 리터 포인터 선언
 * 
 * reader = file_reader_original::get_reader_instance();    // 파일 리터 인스턴스 생성
 * if (nullptr != reader)
 * {
 *      reader->read_contents();    // 파일 읽기
 *      delete reader;
 * }
 * 
 * return 0;
 * 
 * 이 코드에서는 파일의 버전에 따른 영향이 전혀 없다. 
 * 만약 새로운 버전을 구현한 클래스가 추가되더라도 해당 클래스를 대상으로 유연하게 동작한다. 
 * get_reader_instance()로 파일 리더기를 반환받아 read_contents()로 파일을 읽고 해석한다. 
 * 반환된 클래스는 파일 버전과 일치하는 클래스이며, read_contents()는 버전에 적합하게 정의된
 * 멤버 함수가 동작한다. 
 * 
 * get_reader_instance()는 정적(static) 멤버 함수다. 파일 리더기를 생성해서 반환하는 역할은
 * 모든 파일 읽기 인스턴스에서 할 필요가 없기 때문이다. 인스턴스 생성을 별도의 클래스로 분리하는
 * 것이 더 좋은 설계지만, 지금은 부모 클래스의 정적 멤버 함수로 구현했다. 
 */

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;


class file_reader_original
{
public:
    static int read_header();
    static file_reader_original* get_reader_instance();
    virtual void read_contents() = 0;
};

int file_reader_original::read_header()
{
    // v1.0 이라고 가정
    return 1;

    // v2.0 이라고 가정
    // return 2;

}


class file_reader_v0100 : public file_reader_original
{
private:
    virtual void read_contents() override;
};

void file_reader_v0100::read_contents()
{
    cout << "v1.0 파일 본문 읽기" << endl;
}


class file_reader_v0200 : public file_reader_original
{
public:
    virtual void read_contents() override;
};

void file_reader_v0200::read_contents()
{
    cout << "v2.0 파일 본문 읽기" << endl;
}


file_reader_original* file_reader_original::get_reader_instance()
{
    file_reader_original* reader = nullptr;

    switch (file_reader_original::read_header())    // 파일 헤더를 읽어 버전 확인 
    {
        case 1: // v 1.0으로 파일 리더기 생성 
            reader = new file_reader_v0100();
            break;
        case 2:
        default:    // v 2.0으로 파일 리더기 생성 
            reader = new file_reader_v0200();
            break;
    }
    
    return reader;
}


int main(void)
{
    file_reader_original* reader = nullptr;

    reader = file_reader_original::get_reader_instance();
    if (nullptr != reader)
    {
        reader->read_contents();
        delete reader;
    }

    return 0;
}

/**
 * 함수를 보면 먼저 파일 헤더에서 버전을 확인한다. 파일 버전에 따라 v 1.0 파일 리더기
 * file_reader_v0100 또는 v 2.0 파일 리더기 file_reader_v0200 을 사용한다. 파일 읽기
 * 인스턴스는 별도의 클래스로 생성하는데, 두 클래스 모두 file_reader_original을 상속받았으므로
 * file_reader_original 포인터로 반환한다. 
 * 
 * 이후에 새로운 버전을 개발하면 신규 클래스를 생성하고 파일 리더기를 반환하는 부분의 코드만 수정하면
 * 계속 확장할 수 있다. 이처럼 객체지향 프로그래밍의 다형성을 활용하면 소프트웨어의 버전이 바뀌어도 
 * 주요 로직은 수정할 필요가 없어 유연성이 높아지고 유지 / 보수가 편리해진다. 
 */