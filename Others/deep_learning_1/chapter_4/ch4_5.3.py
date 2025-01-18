#시험 데이터로 평가하기
'''
훈련 데이터의 미니 배치에 대한 손실 함수의 값이 작아지는 것은 신경망이 잘 학습하고 있다는 방증\
이나, 이 결과만으로는 다른 데이터셋에서도 비슷한 실력을 발휘할지는 확실하지 않다.

신경망 학습에서는 훈련 데이터 외의 데이터를 올바르게 인식하는지를 확인해야 한다.
다른 말로 '오버피팅'을 일으키지 않는지 확인해야 한다.
-> 훈련 데이터에 포함된 이미지만 제대로 구분하고, 그렇지 않은 이미지는 식별할 수 없다는 뜻이다.

신경망 학습의 원래 목표는 범용적인 능력을 익히는 것이다.
범용 능력을 평가하려면 훈련 데이터에 포함되지 않은 데이터를 사용해 평가해봐야 한다.
-> 학습 도중 정기적으로 훈련 데이터와 시험 데이터를 대상으로 정확도를 기록한다.

*epoch

1에폭은 학습에서 훈련 데이터를 모두 소진했을 때의 횟수에 해당한다.
예컨대 훈련 데이터 10,000개를 100개의 미니배치로 학습할 경우, 확률적 경사 하강법을\
100회 반복하면 모든 훈련 데이터를 '소진'하게 된다.
이 경우 100회가 1에폭이 된다.
'''
import numpy as np
import sys, os
sys.path.append(os.pardir)
from ..chapter_5.mnist import load_mnist
from chapter_5.two_layer_net import TwoLayerNet

(x_treain, t_train), (x_test, t_test)=\
    load_mnist(normalize=True, one_hot_label=True)

train_loss_list=[]

network=TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

#하이퍼 파라미터
iters_num=10000
train_size=x_treain.shape[0]
batch_size=100
learning_rate=0.1

train_loss_list=[]
train_acc_list=[]
test_acc_list=[]

#1에폭당 반복 수
iters_per_epoch=max(train_size/batch_size, 1)

for i in range(iters_num):
    #미니배치 획득
    batch_mask=np.random.choice(train_size, batch_size)
    x_batch=x_treain[batch_mask]
    t_batch=t_train[batch_mask]

    #기울기 계산
    grad=network.numerical_gradient(x_batch, t_batch)
    # grad=network.gradient(x_batch, t_batch)   -> 성능 개선판!

    #매개변수 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key]-=learning_rate*grad[key]

    #학습 경과 기록
    loss=network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    #1에폭당 정확도 계산-> for 문 안에서 매번 계산하기에는 시간이 오래 걸리고, 자주 기록할 필요도 없음
    if i%iters_per_epoch==0:

        train_acc=network.accuracy(x_treain, t_train)   #모든 훈련 데이터의 정확도
        test_acc=network.accuracy(x_test, t_test)   #모든 시험 데이터의 정확도
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print('train acc, test acc | '+str(train_acc)+','+str(test_acc))
'''
에폭이 진행될수록(학습이 진행될수록) 훈련 데이터와 시험 데이터를 사용하고\
평가한 정확도가 모두 좋아지고 있다.
또, 두 정확도에는 차이가 없음을 알 수 있다.
-> 이번 학습에서는 오버피팅이 일어나지 않는다.
'''