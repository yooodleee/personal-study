#하이퍼 파라미터 최적화 구현하기

'''
학습률과 가중치 감소의 세기를 조절하는 개수(가중치 감소 계수)를 탐색한다.
하이퍼 파라미터의 검증은 그 값을 0.001~1,000(10^-3~10^3) 사이 같은 로그 스케일 범위에서\
무작위로 추출해 수행한다.

'''
import numpy as np

weight_decay=10**np.random.uniform(-8,-4)   #가중치 감소 계수:10^-8~10^-4
lr=10**np.random.uniform(-6,-2) #학습률:10^-6~10^-2

'''
여러 차례 다양한 하이퍼 파라미터 값으로 학습을 반복하며 신경망에 좋을 것 같은 값이\
어디에 존재하는지 관찰한다.
'''
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from multi_layer_net import MultiLayerNet
from chapter_7.util import shuffle_dataset
from trainer import Trainer

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 결과를 빠르게 얻기 위해 훈련 데이터를 줄임
x_train = x_train[:500]
t_train = t_train[:500]

# 20%를 검증 데이터로 분할(하이퍼 파라미터 최적화)
validation_rate = 0.20
validation_num = int(x_train.shape[0] * validation_rate)
x_train, t_train = shuffle_dataset(x_train, t_train)    #오버피팅을 방지하기 위해 shuffle
x_val = x_train[:validation_num]    
t_val = t_train[:validation_num]    #validation(검증 데이터): 20%의 훈련 데이터
x_train = x_train[validation_num:]  
t_train = t_train[validation_num:]  #훈련 데이터: 나머지 80%의 훈련 데이터


def __train(lr, weight_decay, epocs=50):
    network = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                            output_size=10, weight_decay_lambda=weight_decay)
    trainer = Trainer(network, x_train, t_train, x_val, t_val,
                      epochs=epocs, mini_batch_size=100,
                      optimizer='sgd', optimizer_param={'lr': lr}, verbose=False)
    trainer.train()

    return trainer.test_acc_list, trainer.train_acc_list


# 하이퍼파라미터 무작위 탐색======================================
optimization_trial = 100
results_val = {}    #validation(검증 데이터 딕셔너리)
results_train = {}  #훈련 데이터 딕셔너리
for _ in range(optimization_trial):
    # 탐색한 하이퍼파라미터의 범위 지정===============
    weight_decay = 10 ** np.random.uniform(-8, -4)  #가중치 감소 계수:10^-8~10^-4
    lr = 10 ** np.random.uniform(-6, -2)    #학습률:10^-6~10^-2
    # ================================================

    val_acc_list, train_acc_list = __train(lr, weight_decay)
    print("val acc:" + str(val_acc_list[-1]) + " | lr:" + str(lr) + ", weight decay:" + str(weight_decay))
    key = "lr:" + str(lr) + ", weight decay:" + str(weight_decay)
    results_val[key] = val_acc_list
    results_train[key] = train_acc_list

# 그래프 그리기========================================================
print("=========== Hyper-Parameter Optimization Result ===========")
graph_draw_num = 20
col_num = 5
row_num = int(np.ceil(graph_draw_num / col_num))
i = 0

for key, val_acc_list in sorted(results_val.items(), key=lambda x:x[1][-1], reverse=True):
    print("Best-" + str(i+1) + "(val acc:" + str(val_acc_list[-1]) + ") | " + key)

    plt.subplot(row_num, col_num, i+1)
    plt.title("Best-" + str(i+1))
    plt.ylim(0.0, 1.0)
    if i % 5: plt.yticks([])
    plt.xticks([])
    x = np.arange(len(val_acc_list))
    plt.plot(x, val_acc_list)
    plt.plot(x, results_train[key], "--")
    i += 1

    if i >= graph_draw_num:
        break

plt.show()

# Best-1 (val acc:0.83) | lr:0.0092, weight decay:3.86e-07
# Best-2 (val acc:0.78) | lr:0.00956, weight decay:6.04e-07
# Best-3 (val acc:0.77) | lr:0.00571, weight decay:1.27e-06
# Best-4 (val acc:0.74) | lr:0.00626, weight decay:1.43e-05
# Best-5 (val acc:0.0052) | lr:0.0052, weight decay:8.97e-06

'''
학습이 잘 진행될 때의 학습률은 0.001~0.01, 가중치 감소 계수는 10^-8~10^-6정도라는 것을 알 수 있다.
-> 잘 될 것 같은 값의 범위를 관찰하고 범위를 좁혀간다.
-> 축소된 범위로 똑같은 작업을 반복한다.
-> 적절한 값이 위치한 범위를 좁혀가다가 특정 단계에서 최종 하이퍼 파라미터 값 하나를 선택한다.
'''