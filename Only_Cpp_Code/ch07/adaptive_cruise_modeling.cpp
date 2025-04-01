// 프랜드 클래스

/**
 * private이나 protected로 지정된 멤버 변수와 함수는 외부에서 접근할 수 없고, protected 멤버는 자식
 * 클래스에서만 접근할 수 있다. 그런데 때때로 private이나 protected 멤버를 특정 클래스에서만 public
 * 처럼 접근해야 할 수도 있다. 이때 해당 클래스를 프렌드(friend)로 등록하면 된다. 프렌드 등록은 특정
 * 클래스에서만 예외를 허용하는 것으로 친한 친구끼리 비밀을 공유하는 것과 같다. 
 * 
 * 프렌드 클래스는 대상 클래스 내부에 friend 키워드로 선언한다. 그러면 마치 대상 클래스의 객체처럼
 * 모든 멤버에 접근할 수 있는 권한이 생긴다. 여기서 대상 클래스란 외부에서 접근을 허용할 멤버가 
 * 선언된 클래스를 말한다. 
 * 
 * 프렌드 클래스
 * class gs_engine : public ic_engine
 * {
 * public: 
 *    gs_engine();
 *    ~gs_engine();
 * 
 * private: 
 *    void acceleration_output();
 *    // 프렌드 클래스 선언
 *    friend class automobile;
 * };
 * 
 * gs_engine의 프렌드 클래스로 automobile 클래스가 선언되면 접근 지정자와 상관없이 automobile 클래스
 * 내부에서 gs_engine 클래스의 모든 멤버 변수, 함수에 접근할 수 있다. automobile을 상속받은 클래스는
 * friend 속성을 물려받지 않는다. 상속받은 자식 클래스에서도 접근 지정자와 상관없이 멤버에 접근하게 
 * 허용하려면 gs_engine에서 friend 클래스로 지정해줘야 한다. 
 * 
 * 프렌드 클래스를 사용하는 코드를 살펴보자. 객체지향 프로그래밍을 설명할 때 보았던 크루즈 컨트롤 코드이다. 
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



class engine 
{
private:
  virtual void acceleration_output() = 0;
  virtual void reduce_output() = 0;
  friend class accelerator;
};



class ic_engine : public engine 
{
private:
  virtual void acceleration_output() = 0;
  virtual void reduce_output() = 0;
};



class gs_engine : public ic_engine 
{
private:
  void acceleration_output() override 
  { 
    increasing_fuel(); 
  };
  void reduce_output() override 
  { 
    decreasing_fuel(); 
  };
  void increasing_fuel() 
  { 
    increasing_piston_speed(); 
  };
  void decreasing_fuel() 
  { 
    decreasing_piston_speed(); 
  };
  void increasing_piston_speed() 
  { 
    cout << "increasing_piston_speed" << endl; 
  };
  void decreasing_piston_speed() 
  { 
    cout << "decreasing_piston_speed" << endl; 
  };
};



class elec_engine : public engine 
{
private:
  void acceleration_output() override 
  { 
    increasing_motor_speed(); 
  };
  void reduce_output() override 
  { 
    decreasing_motor_speed(); 
  };
  void increasing_motor_speed() 
  { 
    cout << "increasing_motor_speed" << endl; 
  };
  void decreasing_motor_speed() 
  { 
    cout << "decreasing_motro_speed" << endl; 
  };
};



class break_system 
{
public:
  void pushing_break(accelerator& accelerator_obj);
};



class accelerator 
{
public:
  accelerator(engine& engine) : my_engine(engine) {};
  void acceleration_output() 
  { 
    my_engine.acceleration_output(); 
  };
  void set_engine(engine& engine) 
  { 
    my_engine = engine; 
  };

private:
  engine& my_engine;

  void reduce_output();
  // break_system의 pushing_break 함수를 프렌드로 선언
  friend void break_system::pushing_break(accelerator& accelerator_obj);
};


// break_system의 pushing_break 함수 정의
void break_system::pushing_break(accelerator& accelerator_obj) 
{
  accelerator_obj.reduce_output();
}


void accelerator::reduce_output() 
{
  my_engine.reduce_output();
}



class sensor 
{
public:
  int inquiring_range() 
  { 
    return dummy; 
  };
  int inquiring_current_speed() 
  { 
    return dummy; 
  };
};



class cruise_controller 
{
public:
  cruise_controller(sensor& sensor, accelerator& accelerator, break_system& break_system) :
    my_sensor(sensor), my_accelerator(accelerator), my_break_system(break_system) 
    {
      acceleration_adjusting_period = 1;
      user_target_speed = 0;
      keep_cruise = false;
    };

  void do_cruise();
  void stop_cruise() 
  { 
    keep_cruise = false; 
  };
  void set_target_speed(int speed) 
  { 
    user_target_speed = speed; 
  };

private:
  int calculating_fit_speed(int range, int original_target_speed) 
  { 
    return dummy; 
  };
  void acceleration_adjusting(int target_speed, int current_speed);

  sensor& my_sensor;
  accelerator& my_accelerator;
  break_system& my_break_system;

  int user_target_speed;
  int acceleration_adjusting_period;
  bool keep_cruise;
};


void cruise_controller::do_cruise() 
{

  int range = dummy, current_speed = dummy;
  keep_cruise = true;

  while (keep_cruise) 
  {
    range = my_sensor.inquiring_range();
    current_speed = my_sensor.inquiring_current_speed();
    acceleration_adjusting(calculating_fit_speed(range, current_speed), user_target_speed);
#ifdef _WIN32
    Sleep(acceleration_adjusting_period);
#else
    sleep(acceleration_adjusting_period / 1000);
#endif
    keep_cruise = false;
  }
}


void cruise_controller::acceleration_adjusting(int current_speed, int target_speed) 
{

  if (target_speed == current_speed) 
  {
    return;
  }

  if (target_speed > current_speed) 
  {
    my_accelerator.acceleration_output();
    return;
  }

  my_break_system.pushing_break(my_accelerator);
}



class car 
{
public:
  car(engine& engine, sensor& sensor, break_system& break_system, 
      accelerator& accelerator, cruise_controller& cruise_controller) :
    my_engine(engine), 
    my_sensor(sensor), 
    my_break_system(break_system), 
    my_accelerator(accelerator), 
    my_cruise_controller(cruise_controller) {};
  
  void do_cruise();
  void stop();

private:
  engine& my_engine;
  sensor& my_sensor;
  break_system& my_break_system;
  accelerator& my_accelerator;
  cruise_controller& my_cruise_controller;
};


void car::stop() 
{
  my_break_system.pushing_break(my_accelerator);
}


void car::do_cruise() 
{

  my_cruise_controller.set_target_speed(100);
  my_cruise_controller.do_cruise();
}



int main(int argc, char** argv) 
{

  gs_engine my_engine;
  sensor my_sensor;
  break_system my_break_system;
  accelerator my_accelerator(my_engine);
  cruise_controller my_cruise_controller(my_sensor, my_accelerator, my_break_system);
  car my_car(my_engine, my_sensor, my_break_system, my_accelerator, my_cruise_controller);

  my_car.do_cruise();

  return 0;
}