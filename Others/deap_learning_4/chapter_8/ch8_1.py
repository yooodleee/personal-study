import gym

env=gym.make('CartPole-v1', render_mode='human')

state=env.reset()[0] #상태 초기화
print('상태: ', state)
#상태:  [ 0.04580889 -0.03004625 -0.03301764  0.02644667]

action_space=env.action_space
print('행동의 차원 수: ', action_space)
#행동의 차원 수:  Discrete(2)

action=0 #or 1
next_state, reward, terminated, trucated, info=env.step(action)
print(next_state)
#[ 0.03502674 -0.16600586  0.01690378  0.2593155 ]