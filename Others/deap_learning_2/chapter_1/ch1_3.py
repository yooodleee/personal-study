#신경망 학습
'''
학습되지 않은 신경망은 '좋은 추론'을 해낼 수 없다.
그래서 학습을 먼저 수행하고, 그 학습된 매개변수를 이용해 추론을 수행하는 흐름이 일반적이다.
신경망의 추론은 문제에서 답을 구하는 작업이고, 학습은 최개의 매개변수 값을 찾는 작업이다.
'''
#손실 함수
'''
신경망 학습에는 학습이 얼마나 잘 되고 있는지를 알기 위한 '척도'가 필요하다.
학습 단계 특정 시점에서 신경망의 성능을 나타내는 척도로 '손실'loss를 사용한다.
-> 학습 데이터와 신경망이 예측한 결과를 비교해 예측이 얼마나 나쁜가를 산출할 단일 값(스칼라)이다.

신경망의 손실은 손실 함수loss function를 사용해 구한다.
다중 클래스 분류multi-class classification 신경망에서는 손실 함수로 흔히 교차 엔트로피 오차cross entropy error를 이용한다.
-> 신경망이 출력하는 각 클래스의 '확률'과 정답 레이블'을 이용해 구할 수 있다.
-> Softmax 계층은 소프트맥스 함수를, Cross Entropy Error 계층은 교차 엔트로피 오차를 구하는 계층이다.

*신경망의 계층 구성

x->Affine->sigmoid->Affine->Softmax->CrrosEntropyError->L

Softmax 계층의 출력은 확률이 되어, 다음 계층인 Cross Entropy Error 계층에는 확률과 정답 레이블이 입력된다.
소프트맥스 함수의 출력의 각 원소는 0.0~1.0 사이의 실수이다.
그리고 그 원소들을 모두 더하면 1.0이 된다.

소프트맥스의 출력인 '확률'이 다음 차례인 교차 엔트로피 오차에 입력된다.
log는 네이피어 상수(오일러 상수)e를 밑으로 하는 로그이며, 정답 레이블 t=[0,0,1]\
처럼 원-핫 벡터로 표기한다.(단 하나의 원소만 1이고 나머지는 0->1인 원소가 정답 클래스에 해당->1의 원소에 해당하는 출력의 자연로그를 계산함)

하나의 데이터에 대한 손실 함수를 나타낸 식을 데이터 N개로 확장할 경우,\
N으로 나눠서 1개당의 '평균 손실 함수'를 구한다.
-> 미니 배치의 크기에 상관없이 항상 일관된 척도를 얻을 수 있다.

소프트맥스 함수와 교차 엔트로피 오차를 계산하는 계층을 Softmax with Loss 계층 하나로 구현한다.
'''
#미분과 기울기
'''
신경망 학습의 목표는 손실을 최소화하는 매개변수를 찾는 것이다.
벡터의 각 원소에 대해 미분을 정리한 것이 기울기gradient이다.
'''
#연쇄법칙
'''
학습 시 신경망은 학습 데이터를 주면 손실을 출력한다.(손실 함수-교차 엔트로피 오차)
여기서 우리가 얻고 싶은 것은 각 매개변수에 대한 손실의 기울기이다.(gradient)
기울기를 얻을 수 있다면, 매개변수를 갱신할 수 있기 때문이다.
-> 오차역전파법back-propagation을 이용할 수 있다.

연쇄법칙chain rule이란 합성함수에 대한 미분의 법칙이다.
우리가 다루는 함수가 아무리 복잡하고 많더라도, 그 미분은 개별 함수의 미분들을 이용해 구할 수 있다.
달리 말하면, 각 함수의 국소적인 미분을 계산할 수 있다면 그 값들을 곱해서 전체의 미분을 구할 수 있다.
'''
#계산 그래프
'''
연쇄 법칙에 따르면 역전파로 흐르는 미분 값은 상류로부터 흘러온 미분과 각 연산 노드의\
국소적인 미분을 곱해 계산할 수 있다(상류란 출력 쪽).

계산 그래프를 구축하는 연산 노드로는 다양한 연산 노드가 있다.

1) 덧셈 노드
상루로부터 받은 값에 1을 곱하여 하류로 기울기를 전파한다.
-> 상류로부터의 기울기를 그대로 흘리기만 한다.

2) 곱셈 노드
상류로부터 받은 기울기에 순전파 시의 입력을 서로 바꾼 값을 곱한다.
-> 순전파 시 입력이 x면 y를 곱하고, y면 x를 곱한다.

3) 분기 노드
분기 노드는 단순히 선이 2개로 나뉘도록 그리는데, 이때 같은 값이 복제되어 분기한다.
-> 복제 노드라고도 한다.
-> 역전파는 상류에서 온 기울기들의 '합'이 된다.

4) Repeat 노드
2개로 분기하는 분기 노드를 일반화하면 N개로의 분기(복제)가 된다.-> Repeat
-> N개의 분기 노드로 볼 수 있으므로, 그 역전파는 N개의 기울기를 모두 더해 구할 수 있다.
'''
#Repeat 구현
import numpy as np

D, N=8, 7

x=np.random.randn(1, D) 
y=np.repeat(x, N, axis=0)   #원소 복제를 수행(repeat-> x를 8개로 분기(복제))
dy=np.random.randm(N,D)
dx=np.sum(dy, axis=0, keepdims=True)    
#역전파(총합), keepdims=True(2차원 배열의 차원 수를 유지)
#Ture(결과의 형상은 (1,D))/False((D))

'''
5) Sum 노드
범용 덧셈 노드이다.
NxD 배열에 대해 그 총합을 0축에 대해 구한다.
Sum 노드의 역전파는 상류로부터의 기울기를 모든 화살표에 분배한다.
-> 덧셈 노드의 역전파를 자연스럽게 확장한 것.
'''

#Sum 노드 구현
#Sum 노드와 Repeat 노드는 서로 '반대 관계'
#Sum 노드의 순전파-> Repeat 노드의 역전파(np.sum)
#Sum 노드의 역전파-> Repeat 노드의 순전파(np.repeat)
import numpy as np

D, N=8, 7
x=np.random.randn(N,D)  #입력
y=np.sum(x, axis=0, keepdims=True)  #순전파

dy=np.random.randn(1,D) #무작위 기울기
dx=np.repeat(dy, N, axis=0) #역전파


#Matmul 노드
'''
행렬의 곱셈을 MatMul 노드로 표현한다.
역전파는 다소 복잡하므로 직관적인 이해가 중요하다.

y=xW라는 계산을 예로 들어본다.
x, W, y의 형상은 각각 (1xD), (DxH), (1xH)

이때 x의 i번째 원소에 대한 미분 dL/dx_i은 다음과 같이 구한다.
dL/dx_i=sigma(j) (dL/dy_j)*(dy_j/dx_i)

dL/dx_i은 x_i를 (조금) 변화시켰을 때 L이 얼마나 변화할 것인가라는 '변화의 정도'를 나타낸다.
x_i를 변화시켜 벡터 y의 모든 원소가 변하고, 그로 인해 최종적으로 L이 변하게 된다.
-> x_i에서 L에 이르는 연쇄 법칙의 경로는 여러 개가 있으며, 그 총합은 dL/dx_i이 된다.

dy_j/dx_i=W_ij가 성립하므로, 이를 위의 식에 대입하면 다음처럼 된다.
dL/dx_i=sigma(j) (dL/dy_j)*(dy_i/dx_i)=sigma(j) (dL/dy_j)*W_ij

dL/dx_i는 벡터 dL/dy과 W의 i행 벡터의 내적으로 구해짐을 알 수 있다.
다음을 유도할 수 있다.
dL/dx=(dL/dy)*W^t

dL/dx은 행렬의 곱을 사용해 단번에 구할 수 있다.
여기서 W^t는 W의 전치행렬이라는 뜻이다.

*위 식을 역을 취해(그 정확성이 성립되게 함으로써), 역전파의 수식(구현)을 유도할 수 있다.
y=xW라는 행렬 곱 계산을 예로 설명해본다.

이번에는 미니배치 처리를 고려해 x에는 N개의 데이터가 담겨 있다고 가정한다.
그러면 x, W, y의 형상은 각각 NxD, DxH, NxH가 된다.

이제 dL/dx은 어떻게 계산할지 생각해보자.
이때 dL/dx과 관련된 변수(행렬)는 상류에서의 기울기 dL/dy과 W이다.
W가 관여된 이유는 곱셈의 역전파를 생각하면 이해하기 쉽다.

곱셈의 역전파에서는 순전파시의 입력을 서로 바꾼 행렬을 사용했다.
이와 마찬가지로 행렬의 역전파에서도 순전파 시의 입력을 서로 바꾼 행렬을 사용한다.
각 행렬의 형상에 주목해 정합성이 유지되도록 행렬 곱을 조합한다.
'''
import numpy as np

class MatMul:
    def __init__(self, W):
        self.params=[]
        self.grads=[np.zeros_like(W)]
        self.x=None
    
    def foward(self, x):
        W,=self.params
        out=np.matmul(x, W) #입력 데이터와 가중치를 행렬의 곱셈
        self.x=x
        return out
    
    def backward(self, dout):
        W,=self.params
        dx=np.matmul(dout, W.T) #가중치의 전치행렬(W.T)
        dW=np.matmul(self.x.T, dout)    #x(입력 데이터)의 전치행렬
        self.grads[0][...]=dW   
        #[...]생략eclips 기호-> 넘파이 배열이 가리키는 메모리 위치를 고정시키고, 그 위치에 원소들을 덮어쓴다.
        #grads[0]=dW-> 얕은 복사
        #grads[0][...]=dW-> 깊은 복사
        return dx

'''
a=np.array([1,2,3])
b=np.array([4,5,6])

a=b와 a[...]=b 모두 a에는 [4,5,6]이 할당된다.
그러나 두 경우에 a가 가리키는 메모리의 위치는 다르다.
생략 기호는 데이터를 덮어쓰기 때문에 변수가 가리키는 메모리의 위치는 변하지 않는다.

a=b에서는 a가 가리키는 메모리 위치가 b가 가리키는 위치와 같아진다.
실제 데이터 (4,5,6)은 복제되지 않는다는 뜻으로, '얕은 복사'라고 한다.

a[...]=b는 a의 메모리 위치는 변하지 않고, 대신 a가 가리키는 메모리에 b의 원소가 복제된다.
실제 데이터가 복제된다는 뜻으로 '깊은 복사'라고 한다.

-> 생략 기호를 이용하여 변수의 메모리 주소를 고정할 수 있음을 알 수 있다.
-> 메모리 주소를 고정함으로써 인스턴스 변수 grads를 다루기가 더 쉬워진다.
'''
#기울기 도출과 역전파 구현
'''
1) Sigmoid 계층

시그모이드 함수
-> 1/(1+np.exp(-x))의 미분은 dy/dx=y(1-y)이다.

출력 쪽 계층으로부터 전해진 기울기(dy/dx)에 시그모이드 함수의 미분(dy/dx), 즉\
y(1-y)를 곱하고, 그 값을 입력 쪽 계층으로 전파한다.
'''
class Sigmoid:
    def __init__(self):
        self.params, self.grads=[], []
        self.out=None
    
    def forward(self, x):
        out=1/(1+np.ext(-x))
        self.out=out
        return out
    
    def backward(self, dout):
        dx=dout*(1.0-self.out)*self.out
        return dx

#Affine 계층
'''
Affine 계층의 순전파는 y=np.matmul(x,W)+b로 구현할 수 있다.
여기서 편향을 더할 때는 브로드캐스트가 사용된다.

MatMul 노드로 행렬 곱을 계산한다.
편향은 Repeat 노드에 의해 복제된 후 더해진다.
(Repeat 노드가 수행하는 복제가 넘파이의 브로트캐스트 기능에 해당한다.)
'''
class MatMul:
    def __init__(self, W, b):
        self.params=[W,b]   #인스턴스 변수 params에는 매개변수 가중치(W)와 편향(b)을 저장한다.
        self.grads=[np.zeros_like(W), np.zeros_like(b)] 
        #Return an array of zeros with the same shape and type as a given array
        self.x=None
    
    def forward(self, x):
        W,b=self.params
        out=np.matmul(W,b)  #행렬의 곱 계산
        self.x=x
        return out
    
    def backward(self,dout):
        W,b=self.params
        dx=np.matmul(dout, W.T) #matmul(dout과 W의 전치행렬임에 주의!)
        dW=np.matmul(self.x.T, dout)    #matmul(dout과 x의 전치행렬임에 주의!)
        db=np.sum(dout, axis=0) #repeat의 역전파는 np.sum으로 구할 수 있다.

        self.grads[0][...]=dW
        self.grads[1][...]=db

        return dx

#Sotfmax with Loss 계층
'''
소프트맥스 함수와 교차 엔트로피 오차는 하나의 계층으로 구현한다.
3-클래스 분류를 가정하여 이전 계층(입력층에 가까운 계층)으로부터 3개의 입력을 받는다.

Softmax 계층은 입력 (a1, a2, a3)를 정규화하여 (y1, y2, y3)를 출력한다.
Cross Entropy Error 계층은 소프트맥스의 출력 (y1, y2, y3)와 정답 레이블(t1, t2, t3)를 받고,\
이 데이터로부터 손실 L을 구해 출력한다.

*역전파의 결과

Softmax 계층의 역전파는 (y1-t1, y2-t2, y3-t3)로 깔끔하게 떨어진다.
(y1, y2, y3)은 소프트맥스 계층의 출력이고, (t1, t2, t3)은 정답 레이블이므로,\
softmax 계층의 역전파는 자신의 출력과 정답 레이블의 차이이다.
-> 신경망의 역전파는 이 차이(오차)를 앞 계층에 전해주는 것으로, 신경망 학습에서 아주 중요한 성질이다.
'''
#가중치 갱신
'''
오차역전파법으로 기울기를 구했으면, 그 기울기를 사용해 신경망의 매개변수를 갱신한다.
미니배치(훈련 데이터 중 무작위로 다수의 데이터를 골라냄)
기울기 계산(오차역전파법으로 각 가중치 매개변수에 대한 손실함수의 기울기를 구한다)
매개변수 갱신(기울기를 사용하여 가중치 매개변수를 갱신한다)
반복(필요한 만큼 반복함)

상위의 단계를 거쳐 신경망 학습이 이뤄진다.
오차역전파법으로 얻은 기울기는 현재의 가중치 매개변수에서 손실을 가장 크게 하는 방향을 가리킨다.
-> 기울기와 반대 방향으로 갱신하면 손실을 줄일 수 있다.
-> 경사하강법Gradient Descent라고 한다.

가중치 갱신 기법의 종류는 아주 다양한데 그중 가장 단순한 확률적 경사 하강법(SGD)를 구현한다.
확률적Stochastic은 무작위로 선택한 데이터(미니배치)에 대한 기울기를 이용한다는 뜻이다.
SGD는 (현재의) 가중치를 기울기 방향으로 일정 거리만큼 갱신한다.

갱신하는 가중치 매개변수가 W이고, W에 대한 손실 함수의 기울기가 dL/dW이다.
etha는 학습률learning rate를 나타내며, 실제로는 0.01이나 0.001의 값을 미리 정해 사용한다.
'''
class SGD:
    def __init__(self, lr=0.01):
        self.lr=lr
    
    def update(self, params, grads):    #매개변수 갱신
        for i in range(len(params)):    #params 리스트에서
            params[i]-=self.lr*grads[i] #학습률*기울기

model=TwoLayerNet(...)
optimizer=SGD()

for i in range(10000):
    ...
    x_batch, t_batch=get_mini_batch(...)    #미니배치 획득
    loss=model.forward(x_batch, t_batch)    
    #손실 함수는 입력 데이터, 훈련 데이터(20% 정도의 입력 데이터)를 순전파한다.
    model.backward()    #역전파
    optimizer.update(model.params, model.grads)