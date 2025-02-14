// 클래스 정의

class gs_engine : public ic_engine {		// 클래스 선언부
public:
	gs_engine();				// 생성자
	~gs_engine();				// 소멸자
	int_get_current_fuel() {
		return current_fuel;
	};	


private:
	void acceleration_output() override;
	void increasing_fuel() {
		increasing_piston_speed();
	};

	int current_fuel;			// 멤버 변수 선언
	int piston_speed;			// 멤버 변수 선언

};

void gs_engine::acceleration_outout() {		// 멤버 함수 선언부
	increasing_fuel();
	current_fuel++;
}

/*
(1) class: 클래스 선언 키워드:
	클래스를 선언하는 class 키워드입니다.
(2) gs_engine: 클래스 이름
	클래스를 나타태는 이름. 이 클래스의 객체르ㅡㄹ 만들 때 사용하는 데이터 형식으로 볼 수 있다.
(3) ic_engine: 부모 클래스(선택)
	클래스가 다른 클래스를 상속받을 때 쌍점(:) 다음에 접근 지정자와 부모 클래스를 지정한다.
	상속받지 않으면 생략한다.
(4) public: 접근 지정자
	멤버 변수와 함수가 외부에서 접근할 수 있는지를 표시한다.
	접근 지정자 다음에 나오는 멤버 변수와 함수는 해당 접근 제어 설정에 따른다.
(5) gs_engine, ~gs_engine: 생성자와 소멸자(선택)
	객체가 생성되거나 소멸할 때 호출되는 함수.
	선택적으로 사용할 수 있다.
(6) 멤버 함수 선언과 정의:
	객체에 포함할 멤버 함수를 선언한다.
	간단한 함수는 클래스 선언부에 중괄호 { }를 이용해 정의하기도 한다.
(7) 멤버 변수 선언
*/