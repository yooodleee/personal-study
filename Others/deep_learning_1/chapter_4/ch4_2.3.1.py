#미니배치 학습(np.random.choice)
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset import load_mnist
import random

(x_train, y_train), (x_test, y_test)=\
    load_mnist(normalize=True, one_hot_label=True)

train_size=x_train.shape[0]
batch_size=10
batch_mask=np.random.choice(train_size, batch_size)

x_batch=x_train[batch_mask]
y_batch=y_train[batch_mask]

np.random.choice(60000, 10) #훈련 데이터 60000개 중에 10개만 무작위로 출력
#array([8013, 14666, 58210, 23832, 52091, 10153, 8107, 19410, 27260, 21411])