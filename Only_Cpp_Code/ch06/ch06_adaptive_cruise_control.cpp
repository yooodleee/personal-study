// 어댑티브 크루즈 컨트롤 의사코드

/**
 * 객체 지향 이전의 프로그래밍 패러다임
 * 
 * 프로그래밍 패러타임(programming paradigm)은 프로그램을 어떤 절차와 구조를 만들 것인지에 
 * 대한 스타일이나 접근 방법을 나타낸다. 프로그래밍 패러다임도 여러 가지가 있으며 복잡도와
 * 필요성에 따라 변화하고 발전했다. 
 * 
 * 각 패러다임은 언어가 지원하는 기능, 코드의 구조, 문제 해결 접근 방식 등에 차이가 있다. 
 * 가끔 프로그래밍 패러다임을 놓고 무엇이 옳고 그른지, 무엇이 좋고 나쁜지 이야기하는 경우가
 * 있다. 하지만 프로그래밍 패러다임에는 옳고 그름이 있는 것이 아니라 방식이 다른 것이다. 
 */

/**
 * 비구조적 프로그래밍
 * 
 * 비구조적 프로그래밍(non-structured programming)은 코드를 구조화하지 않고 작성하는 방법을 
 * 말한다. 비구조적 프로그래밍으로 작성한 코드는 첫 번째 줄부터 마지막 줄까지 차례대로 실행되며,
 * 코드의 흐름을 이동하는 goto 문을 사용하는 특징이 있다. 대표적인 비구조적 프로그래밍 언어로는
 * 어셈블리어(assembly language), 초창기의 포트란(fortran)이 있다. 
 * 
 * X86 어셈블리어의 예
 * 
 * 			global_start
 * 			section.text
 * _start:	mov rax, 1			; 쓰기를 위한 시스템 호출
 * 			mov rdi, 1
 * 			mov rsi, message	; 출력 문자열 주소
 * 			mov rdx, 13			; 바이트 크기
 * 			(... 생략 ...)
 * 			syscall				; 종료를 위한 시스템 기능 실행
 * 			section.data 
 * message: db "Hello, World", 10
 * 
 * 
 * 비구조적 프로그래밍 언어는 컴퓨터를 사용하기 시작할 즈음에 등장하는 기계어와 유사한 
 * 형태로 만들어졌다. 형태를 보아 최근 프로그래밍 언어와는 많이 다른 것을 알 수 있다. 
 * 요즈음 이런 언어를 많이 사용하지 않지만, 현대 프로그래밍 언어가 동작할 수 없는 환경이나
 * 몇 가지 동작만 허용하는 단순한 환경에서는 이런 언어를 사용하기도 한다. 
 */

/**
 * 절차적 프로그래밍
 * 
 * 절차적 프로그래밍(procedural programming)은 비구조적 프로그래밍과는 다르게 소스 코드를 
 * 여러 부분으로 나눠서 활용하는 패러다임으로, 프로시저를 이용해 구조화하는 방식을 말한다. 
 * 이때 프로시저(procedure)는 일련의 코드 묶음을 말하며 보통 함수를 생각하면 된다. 절차적
 * 프로그래밍의 대표 언어는 C이며 코볼(cobol), 포트란(fortran)도 있다. 
 * 
 * 절차적 프로그래밍에서는 코드의 논리 구조를 모듈화(modulation)할 수 있다. 모듈화하려면 같은 
 * 기능을 수행하는 코드를 다시 작성하지 않아도 재사용할 수 있으며, 각 라이브러리처럼 누군가가 
 * 만들어 놓은 기능을 사용하면 프로그램을 더 쉽게 개발할 수 있다. 또한 구조화된 코드는 다른 
 * 사람이 쉽게 읽을 수 있다는 장점도 있다. 
 */

/**
 * 절차적 프로그래밍으로 얻을 수 있는 효과
 * 
 * 여기서는 자동차의 어댑티브 크루즈 컨트롤(adaptive cruise control) 기능을 절차적 프로그래밍으로
 * 구현하는 상황을 가정하여 절차적 프로그래밍으로 얻을 수 있는 효과를 알아보자. 
 * 
 * 어댑티브 크루즈 컨트롤은 앞차와 간격을 유지하며 속도를 자동으로 조절하는 기능이다. 따라서 엔진 
 * 출력, 가속 페달, 브레이크 조정 등 여러 가지 함수가 필요하다. 
 * 
 * 의사 코드(pseudo code)는 사람이 이해하기 쉽게 알고리즘을 기술하는 데 주로 사용된다. 실제 동작하는
 * 코드는 아니므로 문법에 구애받지 않는다. 
 */

// 전역 변수들
int user_target_speed;
int acceleration_adjusting_period;

// 전역 함수들 
void accelration_output();
void pushing_break();

int inquring_current_speed();
int inquiring_range();
int calculating_fit_speed(int range, int original_target_speed);

void acceleration_adjusting(int target_speed, int current_speed) {
	if (target_speed == current_speed) {
		return;
	}

	if (target_speed > current_speed) {
		accelration_output();
		return;
	}
	pushing_break();
}

// 메인 소스 코드 
void main() {
	int range, current_speed;

	while (do_cruise) {
		range = inquiring_range();
		current_speed = inquring_current_speed();
		acceleration_adjusting(calculating_fit_speed(range, user_target_speed), current_speed);
		sleep(acceleration_adjusting_period);
	}

	return;
}

/**
 * main 함수의 while(...) 코드에서는 운전자가 크루즈 컨트롤을 중단할 때까지 일정 주기로 
 * 반복해서 실행할 기능을 순서에 맞게 호출한다. inquiring_range 함수로 앞차와의 거리, 
 * inquiring_current_speed 함수로 차량의 현재 속도를 구하고, 목표 속도를 정하는 calculating_fit_speed 
 * 함수에 전달한다. 이는 다시 엔진의 출력을 조절하는 acceleration_adjusting 함수의 첫 번째 인자로 사용된다.
 * 그리고 크루즈 컨트롤 기능의 동작 주기를 조절하고자 sleep 함수로 동작을 다시 멈춘다. 
 * 
 * 그리고 일부 함수는 하위 프로시저를 호출하기도 한다. 예컨대 acceleration_adjusting 함수에서는 
 * acceleration_output과 pushing_break 함수를 호출한다. 이렇게 하면 가속 페달이나 브레이크 기능이 바뀌어
 * 엔진 출력을 변경해야 할 때 main이나 acceleration_adjusting 함수는 수정할 필요가 없으며 
 * acceleration_output이나 pushing_break 함수의 내부 구현만 변경해 주면 된다. 
 * 
 * 이처럼 어떤 기능을 프로시저 단위로 나누어 구현하면 기능을 변경해야 할 때 프로그램의 전체 흐름은 
 * 그대로 두고 해당 프로시저만 수정하면 된다. 이러한 특징으로 인해 절차적 프로그래밍으로 작성한 코드는
 * 프로그램의 중심 흐름을 담당하는 코드와 프로시저를 구현하는 코드로 나뉜다. 
 * 
 * 프로시저는 또 다른 프로시저를 호출하는 형태로 구현하기도 한다. 프로시저를 직접 만들거나 이미 만들어 놓은
 * 프로시저를 가지고 레고 블록을 조립하듯이 적절하게 배치하고 재사용한다. 
 */

/**
 * 절차적 프로그래밍의 한계
 * 
 * 자동차 운행 프로그램을 개발한다고 가정할 때 앞에서 살펴본 크루즈 컨트롤 외에도 내비게이션 시스템, 공조 시스템,
 * 원격 제어 등 다양한 기능이 필요하다. 이처럼 프로그램의 규모가 커지면 흐름 코드가 복잡해지며 프로시저도 대폭 
 * 늘어난다. 그만큼 프로시저 간에 곤계도 복잡해진다. 
 * 
 * 그러나 절차적 프로그래밍에서는 프로시저의 다층 구조를 표현할 방법이 없다. 이런 문제를 해결하려면 소스 파일을 
 * 논리적인 단위로 나누고 라이브러리를 만들어야 한다. 그리고 프로그램의 전체 논리 구조를 설명하는 문서를 별도로 
 * 만들어 배포해야 한다. 
 * 
 * 하지만 이런 노력에도 불구하고 프로그램에 참여하는 모든 개발자가 프로그램의 논리 구조를 정확하게 이해하지 못하면
 * 직접 접근하지 말아야 할 프로시저에 접근할 수 있다. 특히 전역 변수에 접근을 막을 방법이 없다. 이런 한계점은 
 * 프로그램에 치명적인 문제로 이어질 수 있다. 
 * 
 * 다음 코드는 절차적 프로그래밍 방식이 어떤 문제를 일으킬 수 있는지 보여 주는 예이다. 
 * 
 * 
 * // 전역 변수들
 * int user_target_speed;
 * int acceleration_adjusting_period;
 * 
 * // 전역 함수들
 * void acceleration_output();
 * void pushing_break();
 * int inquiring_current_speed();
 * int inquiring_range();
 * int calculating_fit_speed(int range, int original_target_speed);		// (1) 접근을 제어하지 못하고 정보가 공개됨
 * 
 * 
 * // (2) 프로시저 간에 논리적 계층 구조가 존재하지만 관련 코드를 모두 확인하기 전에 눈치채기 어려움 
 * void acceleration_adjusting(int target_speed, int current_speed)
 * {
 * 		if (target_speed == current_speed)
 * 		{
 * 			return;
 * 		}
 * 		if (target_speed > current_speed)
 * 		{
 * 			acceleration_output();
 * 			return;
 * 		}
 * 		pushing_brea();
 * }		
 * 
 * 
 * // 메인 소스 코드
 * void main()
 * {
 * 		int range, current_speed;
 * 
 * 		while (do_cruise)
 * 		{
 * 			range = inquiring_range();
 * 			user_target_speed = inquiring_current_speed();	// (3) 지역 변수가 아닌 전역 변수를 변경
 * 			acceleration_adjusting(calculating_fit_speed(range, user_target_speed), current_speed);
 * 
 * 			acceleration_output();		// (4) 하위 프로시저를 직접 호출
 * 			sleep(acceleration_adjusting_period);
 * 		}
 * 		return 0;
 * }
 */

/**
 * 먼저, (1)은 전역 함수 사례로, 모든 곳에서 해당 프로시저에 접근할 수 있다는 문제가 있다. 
 * 즉, 프로시저 간에 관계를 고려해 접근을 제어할 수 없다. 이렇게 하면 소스 코드가 복잡해
 * 보이는 문제도 있지만, 별도의 파일로 나누고 라이브러리로 만들더라도 프로시저의 정보가
 * 노출되는 것에는 변함이 없다. 
 * 
 * (2) acceleration_adjusting 함수에는 내부적으로 호출하는 프로시저가 존재한다. 하지만 논리
 * 구조가 복잡할 때는 프로시저 간의 게층을 파악하기가 어렵다. 따라서 논리 구조를 정확하게 
 * 인지하지 못하면 (4) 처럼 acceleration_output 함수를 중복해서 호출하는 실수를 범할 수 있다. 
 * 
 * (3) 절차적 프로그래밍에서는 프로시저에 필요한 데이터를 인자로 전달하거나 전역 변수로 저장해야 
 * 한다. 이는 프로시저의 매개변수가 많아지는 문제점을 야기하기도 하지만, 더 큰 문제는 전역 변수를 
 * 사용하는 일이 많아지면서 중요한 변수가 엉뚱한 곳에서 변경될 가능성도 커진다는 점이다. 
 * 
 * 또한 절차적 프로그래밍 방식으로 작성한 코드는 여러 개의 프로시저를 하나의 흐름으로만 구성해야 
 * 하므로 다층 구조를 논리적으로 모델링하기가 매우 복잡하며, 만약 확장이 필요하면 코드 전체를 
 * 수정해야 한다. 절차적 프로그래밍의 한계를 요약하면 다음과 같다. 
 * 
 * => 프로시저가 가진 논리적 다층 구조를 프로그래밍 내부에서 표현하는 데 한계가 있다. 
 * => 불필요한 프로시저를 호출하거나 전역 변수를 수정할 수 있다. 이때 프로그램 동작에 치명적인 영향을 
 * 	  줄 수 있다. 
 * 
 * 이러한 한계 때문에 절차적 프로그래밍은 여러 명이 큰 규모의 프로젝트를 진행할 때에는 적절하지 않다. 
 * 따라서 이를 보완하는 다양한 프로그래밍 패러다임이 등장했으며, 그 중 하나가 바로 객체지향 프로그래밍이다. 
 */