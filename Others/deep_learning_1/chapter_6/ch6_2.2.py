#은닉층의 활성화값 분포

'''
은닉층의 활성화값(활성화 함수의 출력 데이터)의 분포를 관찰하면 중요한 정보를 얻을 수 있다.
가중치의 초깃값에 따라 은닉층 활성화 값들이 어떻게 변화하는지 간단히 알아보자.

구체적으로는 활성화 함수를 시그모이드 함수를 사용하는 5층 신경망에 무작위로 생성한 입력 데이터를\
흘리며 각 층의 활성화값 분포를 히스토그램으로 그려본다.
'''
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x): #활성화 함수로 시그모이드 함수로 사용.
    return 1/(1+np.exp(-x))

x=np.random.randn(10000, 100)   #100개의 데이터(10000개에서 100개를 무작위로 생성)
node_num=100    #각 은닉층의 노드(뉴런) 수
hidden_layer_size=5 #은닉층이 5개
activations={}  #이곳에 활성화 결과(활성화 값)를 저장

for i in range(hidden_layer_size):
    if i!=0:    #은닉층이 0층이면
        x=activations[i-1]
    
    #가중치의 표준편차가 1
    # w=np.random.randn(node_num, node_num)*1

    #가중치의 표준편차가 0.01
    w=np.random.randn(node_num, node_num)*0.01


    a=np.dot(x,w)
    z=sigmoid(a)
    activations[i]=z

#히스토그램 그리기
for i, a in activations.items():
    plt.subplot(1,len(activations),i+1)
    plt.title(str(i+1)+'-layer')
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()
'''
각 층의 활성화값들이 0과 1에 치우쳐 분포되어 있다.
시그모이드 함수는 그 출력이 0에 가까워지자(또는 1에 가까워지자) 그 미분은 0에 다가간다.
-> 데이터가 0과 1에 치우쳐 분포하게 되면 역전파의 기울기 값이 점점 작아지다 사라진다.
-> 기울기 소실gradient vanishing
'''

'''
활성화 값이 치우쳤다는 것은 표현력 관점에서는 큰 문제가 있다.
-> 다수의 뉴런이 거의 같은 값을 출력하고 있으니 뉴런을 여러 개 둔 의미가 없어진다는 의미이다.
-> 활성화 값들이 치우치면 표현력을 제한한다는 관점에서 문제가 된다.
'''
#Xavier초깃값
'''
일반적인 딥러닝 프레임워크들이 표준적으로 사용하고 있다.
앞 층에 노드가 많을수록 대상 노드의 초깃값으로 설정하는 가중치가 좁게 퍼진다.

'''
node_num=100
w=np.random.randn(node_num, node_num)/np.sqrt(node_num)