// 어댑티브 크루즈 컨트롤 의사코드

// 전역 변수
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