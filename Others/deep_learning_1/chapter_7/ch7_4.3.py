#합성곱 계층 구현하기
import sys, os
sys.path.append(os.pardir)
from util import im2col
import numpy as np

x1=np.random.rand(1,3,7,7)  #데이터(배치크기)1, 채널3, 높이7, 너비7
col1=im2col(x1,5,5,stride=1,pad=0)
print(col1.shape)   #im2col은 마지막에 reshape!
#(9, 75)

x2=np.random.rand(10,3,7,7) #데이터10, 채널3, 높이7, 너비7
col2=im2col(x2,5,5,stride=1,pad=0)
print(col2.shape)   #reshape!
#(90, 75)
#(10,3,5,5) 형상을 한 다차원 배열 W의 원소 수는 총 750개.
#reshape(10,-1)을 호출하면 750개의 원소를 10묶음으로, 즉 형상이 (10,75)인 배열로 만들어준다.

'''
*im2col의 인터페이스

im2col(input_data, filter_h, filter_w, stride=1, pad=0)

input_data: (데이터 수, 채널 수, 높이, 너비)의 4차원 배열로 이뤄진 입력 데이터
filter_h: 필터의 높이
filter_w: 필터의 너비
stride: 스트라이드
pad: 패딩
'''
class Convolution:
    def __init__(self, w, b, stride=1, pad=0):  #w:너비, b:편향, stride, padding
        self.w=w
        self.b=b
        self.stride=stride
        self.pad=pad
    
    def forward(self, x):   #순전파 
        FN, C, FH, FW=self.w.shape  #필터개수, 채널수, 필터높이, 필터너비
        N, C, H, W=x.shape  #데이터수(배치크기), 채널수, 높이, 너비
        out_h=int(1+(H+2*self.pad-FH)/self.stride)
        out_w=int(1+(W+2*self.pad-FW)/self.stride)

        col=im2col(x, FH, FW, self.stride, self.pad)  #입력 데이터를 im2col  
        col_W=self.w.reshape(FN,- 1).T  #reshape을 사용해 2차원 배열로 전개.
        #reshape(,-1)은 다차원 배열의 원소 수가 변환 후에도 똑같이 유지되도록 적절히 묶어준다.
        out=np.dot(col, col_W)+self.b   #전개한 두 행렬의 곱을 구한다.

        out=out.reshape(N, out_h, out_w, -1).transponse(0,3,1,2)
        #출력 데이터를 적절한 형상으로 바꿔준다.
        #넘파이의 transponse 함수를 사용하는데, 다차원 배열의 축 순서를 바꿔준다.
        #-> 인덱스(0부터 시작)를 지정하여 축의 순서를 변경한다.

        #형상(N,H,W,C)->transponse(전치행렬)=.T-> 형상(N,C,H,W)
        #인덱스0,1,2,3                            인덱스0,3,1,2 

        return out

'''
im2col로 전개한 덕분에 완전 연결 계층의 Affine 계층과 거의 똑같이 구현할 수 있다.

*합성곱 계층의 역전파는 Affine 계층의 구현과 공통점이 많지만, 합성곱 계층의 역전파에서는\
im2col을 역으로 처리해야 한다.
-> col2im 함수를 사용한다.
-> col2im 함수를 사용하는 점을 제외하면 합성곱 계층의 역전파는 Affine 계층과 똑같다.
'''

#풀링 계층 구현하기
'''
풀링의 경우엔 채널 쪽이 독립적이라는 점이 합성곱 계층과 다르다.
구체적으로 풀링 적용 영역을 채널마다 독립적으로 전개한다.
그리고 전개한 행렬에서 행별 최댓값을 구하고 적절한 형상으로 성형하기만 하면 된다.

최댓값 계산에는 넘파이의 np.max를 사용할 수 있다.
인수로 축(axis)을 지정할 수 있는데, 이 인수로 지정한 축마다 최댓값을 구할 수 있다.
가령, np.max(x, axis=1)과 같이 쓰면 입력 x의 1번째 차원의 축마다 최댓값을 구한다.

*axis=0(열방향), axis=1(행방향)
'''
class Pooling:
    #1)입력 데이터를 전개한다.
    #2)행별 최댓값을 구한다.
    #3)적절한 모양으로 성형한다.
    def __init__(self, pool_h, pool_w, stride=1, pad=0):    #풀링높이, 풀링너비, 스트라이드, 패딩
        self.pool_h=pool_h
        self.pool_w=pool_w
        self.stride=stride
        self.pad=pad

    def forward(self, x):
        N,C,H,W=x.shape #데이터수(배치크기), 채널수, 높이, 너비
        out_h=int(1+(H-self.pool_h)/self.stride)    #출력되는 맵의 높이
        out_w=int(1+(W-self.pool_w)/self.stride)    #출력되는 맵의 너비

        #1) 전개
        col=im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col=col.reshape(-1, self.pool_h*self.pool_w)

        #2)최댓값
        out=np.max(col, axis=1) #칼럼(행), 평면에서의 최댓값

        #3)성형
        out=out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        return out

#CNN 구현하기

'''
Conv-> ReLU-> Pooling-> Affine-> ReLU-> Affie-> Softmax->...

CNN 네트워크는 convolution-ReLU-Pooling-Affine-Softmax 순으로 흐른다.

*초기화 때 받는 인수

input_dim=입력 데이터(채널수, 높이, 너비)의 차원
cont_param=합성곱 계층의 하이퍼 파라미터(딕셔너리), 딕셔너리의 키는 다음과 같다.
    filter_num=필터수
    filter_size=필터 크기(데이터 수)
    stride=스트라이드
    pad=패딩
hidden_size=은닉층(완전연결)의 뉴런 수
output_size=출력층(완전연결)의 뉴런 수
weight_init_std=초기화 때의 가중치 표준편차

합성곱 계층의 하이퍼 파라미터는 딕셔너리 형태로 주어진다.(conv_param)
이것은 필요한 하이퍼 파라미터의 값이 {'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1}\
처럼 저장된다는 뜻이다.
'''
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from collections import OrderedDict
from chapter_8.layers import *

class SimpleConvNet:
    def __init__(self, input_dim=(1,28,28),conv_param={'filter_num':30,'filter_size':5,
                                                       'pad':0,'stride':1},
                                                       hidden_size=100, output_size=10, weight_init_std=0.01):
        #초기화 인수로 주어진 합성곱 계층의 하이퍼 파라미터를 딕셔너리에서 꺼낸다.
        filter_num=conv_param['filter_num']
        filter_size=conv_param['filter_size']
        filter_pad=conv_param['pad']
        filter_stride=conv_param['stride']
        input_size=input_dim[1]

        #합성곱 계층의 출력 크기를 계산한다.
        conv_output_size=int(input_size-filter_size+2*filter_pad)/filter_stride+1
        pool_output_size=int(filter_num*(conv_output_size/2)*(conv_output_size/2))

        #학습에 필요한 매개변수는 1번째 층의 합성곱 계층과 나머지 두 완전연결 계층의 가중치와 편향.
        self.params={}
        self.params['W1']=weight_init_std*np.random.randn(filter_num, input_dim[0],filter_size,filter_size)
        self.params['b1']=np.zeros(filter_num)
        self.params['W2']=weight_init_std*np.random.randn(pool_output_size, hidden_size)
        self.params['b2']=np.zeros(hidden_size)
        self.params['W3']=weight_init_std*np.random.randn(hidden_size, output_size)
        self.params['b3']=np.zeros(output_size)

        #순서가 있는 딕셔너리OrderdDict인 layers에 계층들을 차례로 추가함.
        self.layers=OrderedDict()
        self.layers['Conv1']=Convolution(self.params['W1'], #합성곱(너비, 편향, 스트라이드, 패딩)
                                         self.params['b1'],
                                         self.params['stride'],
                                         self.params['pad'])
        self.layers['Relu1']=Relu()
        self.layers['Pool1']=Pooling(pool_h=2, pool_w=2, stride=2)  #풀링높이, 풀링너비, 스트라이드
        self.layers['Affine1']=Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2']=Relu()
        self.layers['Affine2']=Affine(self.params['W3'], self.params['b3'])
        
        self.last_layer=SoftmaxWithLoss()   #lasy_layer라는 별도 변수에 저장함.

def predict(self, x):   #추론 수행
    for layer in self.layers.values():
        x=layer.forward(x)  
        #layer에 추가한 계층을 맨 앞에서부터 차례로(OrderDict) forward 호출하며 그 결과를 다음 계층에 전달
    return x

def loss(self, x, t): #손실 함수를 구함-> predict의 결과를 인수로 마지막 층의 forward를 호출  
    y=self.predict(x)
    return self.last_year.forward(y, t) #x:입력 데이터, t=정답 레이블

#오차역전파법으로 기울기를 구한다(순전파, 역전파를 반복한다.)
def gradient(self, x, t):
    #순전파
    self.loss(x, t)

    #역전파
    dout=1
    dout=self.last_layer.backward(dout)

    layers=list(self.layers.values())
    layers.reverse()    
    for layer in layers:
        dout=layer.backward(dout)
    
    #결과 저장
    grads={}
    grads['W1']=self.layers['Conv1'].dW
    grads['b1']=self.layers['Conv1'].db
    grads['W2']=self.layers['Affine1'].dW
    grads['b2']=self.layers['Affine1'].db
    grads['W3']=self.layers['Affine2'].dW
    grads['b3']=self.layers['Affine2'].db

    return grads