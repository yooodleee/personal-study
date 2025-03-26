// 어댑티브 크루즈 컨트롤 객체지향 프로그래밍

/**
 * 객체 선언
 * 
 * 클래스의 객체를 선언하는 방법은 데이터 형식으로 변수를 선언하는 것과 같다. 
 * 클래스의 객체를 선언하는 방법은 2가지이다. 클래스를 데이터 형식으로 삼고
 * 객체를 선언하는 방법과 new 키워드를 사용하여 동적으로 메모리를 할당하는 
 * 방법이다. new 키워드로 동적 메모리를 할당한 경우에는 반드시 delete 키워드로 
 * 메모리를 해제해 주어야 한다. 
 * 
 * 
 * 객체 선언 방법
 * 
 * // 클래스 정의
 * class engine {...(생략)...};
 * 
 * // 클래스를 데이터 형식처럼 사용하는 방법
 * engine my_engine;
 * 
 * // 클래스 형식으로 동적 메모리 할당과 해제 방법
 * engine *my_engine_pointer = new engine();
 * delete my_engine_pointer;
 * 
 * 객체를 만들었으면 비로소 클래스의 멤버를 사용할 수 있다. 클래스의 멤버를 사용할 때는
 * 다음처럼 객체 이름에 멤버 접근 연산자(.)를 사용한다. 
 * 
 * my_engine.current_fuel;		// 멤버 변수에 접근
 * my_engine.increasing_piston_speed();	// 멤버 함수 호출 
 */

/**
 * 객체지향 프로그래밍을 적용한 어댑티브 크루즈 컨트롤
 * 
 * 앞서 본 어댑티브 크루즈 컨트롤 코드에 객체지향 프로그래밍을 적용해 보겠다. 다음 코드에서는 
 * 아직 배우지 않은 문법이 포함되어 있다. 따라서 세세한 코드보다는 앞서 배운 내용을 토대로
 * 클래스의 전체 구조와 관계, 접근 제어 등이 어떻게 구성되는지 살펴보기 바란다. 
 */

#include <iostream>
#include <stdlib.h>
#ifdef _WIN32

#include <Windows.h>
#else
#include <unistd.h>
#endif
#include <cstdlib>

using namespace std;



class accelerator;
const int dummy = 0;


class engine {
private:
	virtual void acceleration_output() = 0;
	virtual void reduce_output() = 0;
	friend class accelerator;
};


class ic_engine : public engine {
private:
	virtual void acceleration_output() = 0;
	virtual void reduce_output() = 0;
};


class gs_engine : public ic_engine {
private:
	void acceleration_output() override { increasing_fuel(); };
	void reduce_output() override { decreasing_fuel(); };
	void increasing_fuel() { increasing_piston_speed(); };
	void decreasing_fuel() { decreasing_piston_speed(); };
	void increasing_piston_speed() { cout << "increasing_piston_speed" << endl; };
	void decreasing_piston_speed() { cout << "decreasing_piston_speed" << endl; };
};


class elec_engine : public engine {
private:
	void acceleration_output() override { increasing_motor_speed(); };
	void reduce_output() override { decreasing_motor_speed(); };
	void increasing_motor_speed() { cout << "increasing_motor_speed" << endl; };
	void decreasing_motor_speed() { cout << "decreasing_motor_speed" << endl; };
};


class break_system {
public:
	void pushing_break(accelerator& accelerator_obj);
};


class accelerator {
public:
	accelerator(engine& engine) : my_engine(engine) {};
	void acceleration_output() { my_engine.acceleration_output(); };
	void set_engine(engine& engine) { my_engine = engine; };

private:
	engine& my_engine;

	void reduce_output();
	friend void break_system::pushing_break(accelerator& accelerator_obj);
};


void break_system::pushing_break(accelerator& accelerator_obj) {
	accelerator_obj.reduce_output();
}


void accelerator::reduce_output() {
	my_engine.reduce_output();
}


class sensor {
public:
	int inquiring_range() { return dummy; };
	int inquiring_current_speed() { return dummy; };
};


class cruise_controller {
public:
	cruise_controller(sensor& sensor, accelerator& accelerator, break_system& break_system)
		: my_sensor(sensor),
		my_accelerator(accelerator),
		my_break_system(break_system) {
		acceleration_adjusting_period = 1;
		user_target_speed = 0;
		keep_cruise = false;
	};

	void do_cruise();
	void stop_cruise() { keep_cruise = false; };
	void set_target_speed(int speed) { user_target_speed = speed; };


private:
	int calculating_fit_speed(int range, int original_target_speed) { return dummy; };
	void acceleration_adjusting(int target_speed, int current_speed);

	sensor& my_sensor;
	accelerator& my_accelerator;
	break_system& my_break_system;

	int user_target_speed;
	int acceleration_adjusting_period;
	bool keep_cruise;
};


void cruise_controller::do_cruise() {
	int range = dummy, current_speed = dummy;
	keep_cruise = true;

	while (keep_cruise) {
		range = my_sensor.inquiring_range();
		current_speed = my_sensor.inquiring_current_speed();
		acceleration_adjusting(calculating_fit_speed(range, current_speed), user_target_speed);

#ifdef _Win32
		Sleep(acceleration_adjusting_period);
#else
		Sleep(acceleration_adjusting_period / 1000);
#endif
		keep_cruise = false;
	}
}


void cruise_controller::acceleration_adjusting(int current_speed, int target_speed) {
	if (target_speed == current_speed) {
		return;
	}
	if (target_speed > current_speed) {
		my_accelerator.acceleration_output();
		return;
	}
	my_break_system.pushing_break(my_accelerator);
}


class car {
public:
	car(engine &engine, sensor &sensor, break_system &break_system, accelerator &accelerator, cruise_controller &cruise_controller)
		: my_engine(engine)
		, my_sensor(sensor)
		, my_break_system(break_system)
		, my_accelerator(accelerator)
		, my_cruise_controller(cruise_controller){ };
	void do_cruise();
	void stop();

private:
	engine& my_engine;
	sensor& my_sensor;
	break_system& my_break_system;
	accelerator& my_accelerator;
	cruise_controller& my_cruise_controller;
};


void car::stop() {
	my_break_system.pushing_break(my_accelerator);
}

void car::do_cruise() {
	my_cruise_controller.set_target_speed(100);
	my_cruise_controller.do_cruise();
}

int main(int argc, char** argv) {
	gs_engine my_engine;
	sensor my_sensor;
	break_system my_break_system;
	accelerator my_accelerator(my_engine);
	cruise_controller my_cruise_controller(my_sensor, my_accelerator, my_break_system);
	car my_car(my_engine, my_sensor, my_break_system, my_accelerator, my_cruise_controller);
	my_car.do_cruise();
	
	return 0;
}


/**
 * main 함수를 보면 자동차 부품을 각각 객체로 만들었다. 그리고 car 클래스의 생성자를 통해서
 * 이들의 관계를 포함 또는 사용으로 연결했다.
 * 
 * * car:
 * 		- my_accelerator : 
 * 		- my_break_system: break_system
 * 		- my_cruise_controller : cruise_controller
 * 		- my_engine: engine&
 * 		- my_sensor: sensor&
 * 		+ car(...)
 * 		+ do_cruise() : void
 * 		+ stop(): void
 * 
 * * gs_engine: 
 * 		- decreasing_fuel() : void
 * 		- decreasing_piston_speed() : void
 * 		- increasing_fuel() : void
 * 		- increasing_piston_speed() : void
 * 		+ acceleration_output() : void
 * 		+ reduce_output() : void
 * 
 * * ic_engine:
 * 		- acceleration_output() : void
 * 		- reduce_output() : void
 * 
 * * elec_engine:
 * 		- decreasing_motor_speedl () : void
 * 		- increasing_motor_speed() : void
 * 		+ acceleration_output() : void
 * 		+ reduce_output() : void
 * 
 * * engine: 
 * 		- acceleration_output () : void
 * 		- reduce_output () : void
 * 
 * * accelerator: 
 * 		- my_engine: engine&
 * 		+ acceleration_output () : void
 * 		+ accelerator(engine&)
 * 		- reduce_output () : void
 * 		+ set_engine(engine&) : void
 * 		<<friend>> 
 * 		- pushing_break (accelerator&): void
 * 
 * * sensor: 
 * 		+ inquiring_current_speed() : int
 * 		+ inquiring_range() : int
 * 
 * * break_system: 
 * 		+ pushing_break () : void
 * 
 * * cruise_controller:
 * 		- acceleration_adjusting_period: int
 * 		- keep_cruise: bool
 * 		- my_accelerator: 
 * 		- my_break_system: break_system
 * 		- my_sensor: 
 * 		- user_target_speed: int
 * 		- acceleration_adjusting (int, int): void
 * 		- calculating_fit_speed (int, int): int
 * 		+ do_cruise(...)
 * 		+ set_target_speed (int): void
 * 		+ stop_cruise () : void
 */

/**
 * engine 클래스는 모든 엔진의 최상위 클래스다. acceleration_output 함수가 호출되면 자식 클래스에
 * 적합한 동력이 생성된다. acceleration_output 함수는 해당 클래스와 자식 클래스에서만 접근할 수 있고
 * 다른 클래스에서는 호출할 수 없다. 하지만 가속 페달을 통해서 해당 함수를 호출해야 하므로 가속 페달 
 * 클래스와 프렌드(friend) 관계를 맺어 함수에 접근할 수 있도록 했다. 
 * 
 * 그리고 절차적 프로그래밍 코드의 main 함수에 있던 흐름 코드가 cruise_controller 클래스에 포함됐다. 
 */