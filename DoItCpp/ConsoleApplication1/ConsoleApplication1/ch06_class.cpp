// Ŭ���� ����

class gs_engine : public ic_engine {		// Ŭ���� �����
public:
	gs_engine();				// ������
	~gs_engine();				// �Ҹ���
	int_get_current_fuel() {
		return current_fuel;
	};	


private:
	void acceleration_output() override;
	void increasing_fuel() {
		increasing_piston_speed();
	};

	int current_fuel;			// ��� ���� ����
	int piston_speed;			// ��� ���� ����

};

void gs_engine::acceleration_outout() {		// ��� �Լ� �����
	increasing_fuel();
	current_fuel++;
}

/*
(1) class: Ŭ���� ���� Ű����:
	Ŭ������ �����ϴ� class Ű�����Դϴ�.
(2) gs_engine: Ŭ���� �̸�
	Ŭ������ ��Ÿ�´� �̸�. �� Ŭ������ ��ü���Ѥ� ���� �� ����ϴ� ������ �������� �� �� �ִ�.
(3) ic_engine: �θ� Ŭ����(����)
	Ŭ������ �ٸ� Ŭ������ ��ӹ��� �� ����(:) ������ ���� �����ڿ� �θ� Ŭ������ �����Ѵ�.
	��ӹ��� ������ �����Ѵ�.
(4) public: ���� ������
	��� ������ �Լ��� �ܺο��� ������ �� �ִ����� ǥ���Ѵ�.
	���� ������ ������ ������ ��� ������ �Լ��� �ش� ���� ���� ������ ������.
(5) gs_engine, ~gs_engine: �����ڿ� �Ҹ���(����)
	��ü�� �����ǰų� �Ҹ��� �� ȣ��Ǵ� �Լ�.
	���������� ����� �� �ִ�.
(6) ��� �Լ� ����� ����:
	��ü�� ������ ��� �Լ��� �����Ѵ�.
	������ �Լ��� Ŭ���� ����ο� �߰�ȣ { }�� �̿��� �����ϱ⵵ �Ѵ�.
(7) ��� ���� ����
*/