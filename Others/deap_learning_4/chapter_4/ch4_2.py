#가치 함수(기존 구현)
from gridworld import *

env=GridWorld()
V={}

#딕셔너리 원소 초기화
for state in env.states():
    V[state]=0

state=(1, 2)
print(V[state]) #상태 (1, 2)의 가치 함수 출력

from collections import defaultdict

env=GridWorld()
V=defaultdict(lambda: 0)

state=(1, 2)
print(V[state])

pi=defaultdict(lambda: {0:0.25, 1:0.25, 2:0.25, 3:0.25})

state=(0, 1)
print(pi[state])
#{0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}



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

def policy_eval(pi, V, env, gamma, threshold=0.001):
    while True:
        old_V=V.copy() #갱신 전 가치 함수
        V=eval_onestep(pi, V, env, gamma)

        #갱신된 양의 최댓값 계산
        delta=0
        for state in V.keys():
            t=abs(V[state]-old_V[state])
            if delta < t:
                delta=t
        
        if delta<threshold:
            break
    
    return V

env=GridWorld()
gamma=0.9 #할인율
pi=defaultdict(lambda: {0:0.25, 1:0.25, 2:0.25, 3:0.25}) #정책
V=defaultdict(lambda: 0) #가치 함수

V=policy_eval(pi, V, env, gamma)
env.render_v(V, pi)

def argmax(d):
    max_value=max(d.values())
    max_key=0
    for key, value in d.items():
        if value==max_value:
            max_key=key
    return max_key

def greedy_policy(V, env, gamma):
    pi={}

    for state in env.states():
        action_values={}

        for action in env.actions():
            next_state=env.next_state(state, action)
            r=env.reward(state, action, next_state)
            value=r+gamma*V[next_state] #(1)
            action_values[action]=value 
        
        max_action=argmax(action_values) #(2)
        action_probs={0:0, 1:0, 2:0, 3:0}
        action_probs[max_action]=1.0
        pi[state]=action_probs #(3)
    return pi

def policy_iter(env, gamma, threshold=0.001, is_render=False):
    pi=defaultdict(lambda: {0:0.25, 1:0.25, 2:0.25, 3:0.25})
    V=defaultdict(lambda: 0)

    while True:
        V=policy_eval(pi, V, env, gamma, threshold) #(1) 평가
        new_pi=greedy_policy(V, env, gamma) #(2) 개선

        if is_render:
            env.render_v(V, pi)

            if new_pi==pi: #(3) 갱신 여부 확인
                break
            pi=new_pi
        return pi

env=GridWorld()
gamma=0.9
pi=policy_iter(env, gamma)

def value_iter_onestep(V, env, gamma):
    for state in env.states():  #(1)모든 상태에 차례로 접근
        if state==env.gaol_state: #목표 상태에서의 가치 함수는 항상 0
            V[state]=0
            continue
        
        action_values=[]
        for action in env.actions(): #(2) 모든 행동에 차례로 접근
            next_state=env.next_state(state, action)
            r=env.reward(state, action, next_state)
            value=r+gamma*V[next_state] #(3) 새로운 가치 함수
            action_values.append(value)

        V[state]=max(action_values) #(4) 최댓값 추출

    return V

def value_iter(V, env, gamma, threshold=0.001, is_render=True):
    while True:
        if is_render:
            env.render_v(V)
        
        old_V=V.copy() #갱신 전 가치 함수
        V=value_iter_onestep(V, env, gamma)

        #갱신된 양의 최댓값 구하기
        delta=0
        for state in V.keys():
            t=abs(V[state]-old_V[state])
            if delta < t:
                delta=t
        
        #임계값과 비교
        if delta < threshold:
            break
    return V

from gridworld import GridWorld
from policy_iter import greedy_policy

V=defaultdict(lambda: 0)
env=GridWorld()
gamma=0.9

V=value_iter(V, env, gamma) #최적 가치 함수 찾기

pi=greedy_policy(V, env, gamma) #최적 경책 찾기
env.render_v(V, pi)