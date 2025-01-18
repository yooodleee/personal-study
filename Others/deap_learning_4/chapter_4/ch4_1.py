#반복적 정책 평가

V={'L1':0.0, 'L2':0.0}
new_V=V.copy() #V의 복사본

for _ in range(100):
    new_V['L1']=0.5*(-1+0.9*V['L1'])+0.5*(1+0.9*V['L2'])
    new_V['L2']=0.5*(0+0.9*V['L1'])+0.5*(-1+0.9*V['L2'])
    V=new_V.copy()
    print(V)

#임계값을설정하여 갱신 횟수를 자동을 결정(cnt)
V={'L1':0.0, 'L2':0.0}
new_V=V.copy()

cnt=0 #갱신 횟수 기록
while True:
    new_V['L1']=0.5*(-1+0.9*V['L1'])+0.5*(1+0.9*V['L2'])
    new_V['L2']=0.5*(0+0.9*V['L1'])+0.5*(-1+0.9*V['L2'])

    #갱신된 양의 최댓값
    delta=abs(new_V['L1']-V['L1'])
    delta=max(delta, abs(new_V['L2']-V['L2']))

    V=new_V.copy()

    cnt+=1
    if delta < 0.0001: #임계값=0.0001
        print(V)
        print("갱신 횟수: ", cnt)
        break

# {'L1': -2.249167525908671, 'L2': -2.749167525908671}
# 갱신 횟수:  76


#덮어쓰기 방식으로 구현
V={'L1':0.0, 'L2':0.0}

cnt=0
while True:
    t=0.5*(-1+0.9*V['L1'])+0.5*(1+0.9*V['L2'])
    delta=abs(t-V['L1'])
    V['L1']=t

    t=0.5*(0+0.9*V['L1'])+0.5*(-1+0.9*V['L2'])
    delta=max(delta, abs(t-V['L2']))
    V['L2']=t

    cnt+=1
    if delta<0.0001:
        print(V)
        print('갱신 횟수: ', cnt)
        break
    
# {'L1': -2.2493782177156936, 'L2': -2.7494201578106514}
# 갱신 횟수:  60  



#GridWorld 클래스 구현(3x4)
import numpy as np

class GridWorld:
    def __init__(self):
        self.action_space=[0, 1, 2, 3] #행동 공간(가능한 행동들)
        self.action_meaning={ #행동의 의미
            0:'UP',
            1:'DOWN',
            2:'LEFT',
            3:'RIGHT',
        }
        self.reward_map=np.array( #보상 맵(각 좌표의 보상값)
            [[0,0,0,1.0],
             [0,None,0,-1,0],
             [0,0,0,0]]
        )
        self.goal_state=(0, 3) #목표 상태(좌표)
        self.wall_state=(1, 1) #벽 상태(좌표)
        self.start_state=(2, 0) #시작 상태(좌표)
        self.agent_state=self.start_state #에이전트 초기 상태(좌표)
    
    @property
    def height(self):
        return len(self.reward_map)
    
    @property
    def width(self):
        return len(self.reward_map[0])
    
    @property
    def shape(self):
        return self.reward_map.shape
    
    def actions(self):
        return self.action_space #[0, 1, 2, 3]
    
    def states(self):
        for h in range(self.height):
            for w in range(self.width):
                yield (h, w)
    
    def next_state(self, state, action):
        #(1)이동 위치 계산
        action_move_map=[(-1, 0), (1, 0), (0, -1), (0, 1)]
        move=action_move_map[action]
        next_state=(state[0]+move[0], state[1]+move[1])
        ny, nx=next_state

        #(2) 이동한 위치가 그리드 월드의 테두리 밖이나 벽인가?
        if nx < 0 or nx >=self.width or ny < 0 or ny >=self.height:
            next_state==state
        elif next_state==self.wall_state:
            next_state
        
        return next_state #(3)다음 상태 반환
    
    def reward(self, state, action, next_state):
        return self.reward_map[next_state]

    # def render_v(self, v=None, policy=None, print_value=True):
    #     renderer = render_helper.Renderer(self.reward_map, self.goal_state,
    #                                       self.wall_state)
    #     renderer.render_v(v, policy, print_value)

    #반복적 정책 평가 구현
def eval_onestep(pi, V, env, gamma=0.9):
    for state in env.states(): #(1) 각 상태에 접근
        if state==env.goal_state: #(2) 목표 상태에서의 가치 함수는 항상 0
            V[state]=0
            continue

        action_probs=pi[state] #pi(probabilities 확률)
        new_V=0

        #(3) 각 행동에 접근
        for action, action_prob in action_probs.items():
            next_state=env.next_state(state, action)
            r=env.reward(state, action, next_state)

            #(4) 새로운 가치 함수
            new_V+=action_prob*(r+gamma*V[next_state])
        
        V[state]=new_V
    return V

env=GridWorld()

#env.height() 대신 env.height로 사용 가능
print(env.height) #3
print(env.width) #4
print(env.shape) #(3, 4)


for action in env.actions(): #모든 행동에 순차적으로 접근
    print(action)

#0
#1
#2
#3

print('===')

for state in env.states(): #모든 상태에 순차적으로 접근
    print(state)

#(0, 0)
#(0, 1)
#...
#(2, 3)
