#CNN 시각화하기

'''
*1번째 층의 가중치 시각화하기

1번째 층의 핮성곱 계층의 가중치는 그 형상이 (30,1,5,5)였다(필터30, 채널1, 5x5 크기)
필터의 크기가 5x5이고 채널이 1개라는 것은 이 필터를 1 채널의 회색조 이미지로 시각화할 수 있다는 의미이다.
학습 전과 후의 가중치를 비교해본다.

학습 전과 후의 1번 째 층의 합성곱 계층의 가중치
-> 가중치의 원소는 실수이지만, 이미지에서는 가장 작은 값이 0(검은식)
가장 큰 값은 255(흰색)으로 정규화하여 표현한다.

학습 전 필터는 무작위로 초기화되어 있고 흑백의 정도에 규칙성이 없다.
한편, 학습을 마친 필터는 규칙성이 있는 이미지가 되었다.
흰색에서 검은색으로 점차 변화하는 필터와 덩어리(블롭blob)가 진 필터 등, 규칙을 띄는 필터가 되었다.

합성곱 계층의 필터는 에지나 블롭 등의 원시적인 정보를 추출할 수 있다.
이런 원시적인 정보가 뒷단 계층에 전달된다는 것이 앞에서 구현한 CNN에서 일어나는 일이다.
'''
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from simple_convnet import SimpleConvNet

def filter_show(filters, nx=8, margin=3, scale=10):
    """
    c.f. https://gist.github.com/aidiary/07d530d5e08011832b12#file-draw_weight-py
    """
    FN, C, FH, FW = filters.shape
    ny = int(np.ceil(FN / nx))

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    for i in range(FN):
        ax = fig.add_subplot(ny, nx, i+1, xticks=[], yticks=[])
        ax.imshow(filters[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


network = SimpleConvNet()
# 무작위(랜덤) 초기화 후의 가중치
filter_show(network.params['W1'])

# 학습된 가중치
network.load_params("params.pkl")
filter_show(network.params['W1'])