import numpy as np

X=np.array([1.0, 0.5])
W1=np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1=np.array([0.1, 0.2, 0.3])

print(W1.shape) #(2,3)
print(X.shape)  #(2,)
print(B1.shape) #(3,)

A1=np.dot(X, W1)+B1
print(A1)
#[0.3 0.7 1.1]

def sigmoid(x): #넘파이 배열을 받아 같은 수의 원소로 구성된 넘파이 배열을 반환함.
    return 1/(1+np.exp(-x))

Z1=sigmoid(A1)
print(Z1)
#[0.57444252 0.66818777 0.75026011]

#1-> 2층으로 가는 과정
W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2=np.array([0.1,0.2])

print(W2.shape) #(3,)
print(B2.shape) #2,

A2=np.dot(Z1, W2)+B2
Z2=sigmoid(A2)
print(Z2)
#[0.62624937 0.7710107 ]

#2층-> 출력층(신호 전달)
def identity_function(x):   #출력층의 활성화 함수로 항등 함수-> 입력을 그대로 출력하는 함수
    return x

W3=np.array([[0.1, 0.3],[0.2,0.4]])
B3=np.array([[0.1,0.2]])

A3=np.dot(Z2, W3)+B3
y=identity_function(A3)
print(y)
#[[0.31682708 0.69627909]]



#구현 정리하기(3층 신경망)
def init_network(): #가중치와 편향을 초기화, 딕셔너리 network에 저장(key : value)
    network={}
    network['W1']=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])   #가중치(weight)
    network['b1']=np.array([0.1,0.2,0.3])   #편향(bias)
    network['W2']=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2']=np.array([0.1,0.2])
    network['W3']=np.array([[0.1,0.3],[0.2,0.4]])
    network['b3']=np.array([0.1,0.2])

    return network

def forward(network, x):    #입력신호를 출력(순방향-> 순전파)으로 변환하는 처리 과정 
    W1, W2, W3=network['W1'], network['W2'], network['W3']  #가중치
    b1, b2, b3=network['b1'], network['b2'], network['b3']  #편향

    a1=np.dot(x, W1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1, W2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2, W3)+b3
    y=identity_function(a3)

    return y

network=init_network()
x=np.array([1.0, 0.5])
y=forward(network, x)
print(y)    #[0.31682708 0.69627909]