// 절차적 프로그래밍 방식에서 발생할 수 있는 문제점

// 전역 변수들
int user_target_speed;
int acceleration_adjusting_period;

// 전역 함수들
void acceleration_output();
void pushing_break();

int inquiring_current_speed();
int inquiring_range();
int calculating_fit_speed(int range, int original_target_speed);	// 접근을 제어하지 못하고 정보가 공개됨


void acceleration_adjusting(int target_speed, int current_speed) {
	if (target_speed == current_speed) {
		return;
	}

	if (target_speed > current_speed) {
		acceleration_output();
		return;
	}

	pushing_break();
}		// 프로시저 간에 논리적 계층 구조가 존재하지만 관련 코드를 모두 확인하기 전에는 알아채기 어려움


// main 소스 코드
int main() {
	int range, current_speed;

	while (do_cruise) {
		range = inquiring_range();
		user_target_speed = inquiring_current_speed();	// 지역 변수가 아닌 전역 변수를 변경
		acceleration_adjusting(calculating_fit_speed(range, user_target_speed), current_speed);

		acceleration_output();	// 하위 프로시저를 직접 호출
		sleep(acceleration_adjusting_period);
	}
	
	return;
}