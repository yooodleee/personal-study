// ������ ���α׷��� ��Ŀ��� �߻��� �� �ִ� ������

// ���� ������
int user_target_speed;
int acceleration_adjusting_period;

// ���� �Լ���
void acceleration_output();
void pushing_break();

int inquiring_current_speed();
int inquiring_range();
int calculating_fit_speed(int range, int original_target_speed);	// ������ �������� ���ϰ� ������ ������


void acceleration_adjusting(int target_speed, int current_speed) {
	if (target_speed == current_speed) {
		return;
	}

	if (target_speed > current_speed) {
		acceleration_output();
		return;
	}

	pushing_break();
}		// ���ν��� ���� ���� ���� ������ ���������� ���� �ڵ带 ��� Ȯ���ϱ� ������ �˾�ä�� �����


// main �ҽ� �ڵ�
int main() {
	int range, current_speed;

	while (do_cruise) {
		range = inquiring_range();
		user_target_speed = inquiring_current_speed();	// ���� ������ �ƴ� ���� ������ ����
		acceleration_adjusting(calculating_fit_speed(range, user_target_speed), current_speed);

		acceleration_output();	// ���� ���ν����� ���� ȣ��
		sleep(acceleration_adjusting_period);
	}
	
	return;
}