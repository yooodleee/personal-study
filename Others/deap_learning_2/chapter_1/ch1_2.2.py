#계층으로 클래스화 및 순전파 구현
'''
신경망에서 하는 처리를 계층layer으로 구현해본다.
완전연결계층에 의한 변환을 Affine 계층으로,
시그모이드 함수에 의한 변환을 Sigmoid 계층으로 구현한다.

완전연결계층에 의한 변환은 기하학에서의 아핀affine 변환에 해당하기 때문에\
Affine 계층이라고 이름을 지었다.
또한 각 계층은 파이썬 클래스로 구현하며, 기본 변환을 구행하는 메서드의 이름은 forward()로 한다.

*신경망에는 다양한 계층이 등장한다.
이 계층들을 모두 파이썬 클래스로 구현한다.
모듈화하면 레고 블럭을 조합하듯 신경망을 구축할 수 있다.

모든 계층은 forward()와 backward() 메서드를 가진다.
모든 계층은 인스턴스 변수인 params와 grads를 가진다.

params는 가중치와 편향 같은 매개변수를 담는 리스트이다.
grads는 params에 저장된 각 매개변수에 대응하여, 해당 매개변수의 기울기를 보관하는 리스트이다.
'''
import numpy as np

class Sigmoid:
    def __init__(self):
        self.params=[]

    def forward(self, x):
        return 1/(1+np.exp(-x))

class Affine:
    def __init__(self, W, b):
        self.params=[W,b]
    
    def forward(self, x):
        W,b=self.params #가중치(W)와 편향(b)은 신경망이 학습될 때 수시로 갱신된다.
        out=np.matmul(x,W)+b
        return out
'''
입력 x가 Affine-> Sigmoid-> Affine을 거쳐 점수인 s(score)를 출력한다.
이 신경망을 TwoLayerNet라는 클래스로 추상화하고, 주 추론 처리는 predict(x) 메서드로 구현한다.
'''
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        I,H,O=input_size, hidden_size, output_size

        #가중치와 편향 초기화
        W1=np.random.randn(I,H)
        b1=np.random.randn(H)
        W2=np.random.randn(H,0)
        b2=np.random.randn(0)

        #계층 생성
        self.layers=[
            Affine(W1,b1),
            Sigmoid(),
            Affine(W2,b2)
        ]

        #모든 가중치를 리스트에 모은다.
        self.params=[]
        for layer in self.layers:
            self.params+=layer.params
    
    def predict(self, x):
        for layer in self.layers:
            x=layer.forward(x)  #순전파-> 추론
        return x

x=np.random.randn(10,2)
model=TwoLayerNet(2,4,3)
s=model.predict(x)