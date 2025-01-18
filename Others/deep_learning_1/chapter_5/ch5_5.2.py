#sigmoid 계층(역전파)

'''
y=1/(1+np.exp(-x))

1) '/'-> y=1/x를 미분하면
    dy/dx=-1/x**2=-y**2

    역전파 때는 상류에서 흘러온 값에 -y**2(순전파의 출력을 제곱한 후 마이너스를 붙인 값)을\
    곱해서 하류로 전달한다.

2) '+'노드는 상류의 값을 여과 없이 하류로 내보낸다.

3) exp 노드는 y=exp(x) 연산을 수행하며, 그 미분은 다음과 같다.
    dy/dx=exp(x)

4) 'x' 노드는 순전파 때의 값을 '서로 바꿔' 곱한다.

역전파의 최종 출력인 dL/dy y**2 exp(-x) 값이 하류 노드로 전파된다.
여기서 dL/dy y**2 exp(-x)를 순전파의 입력 x와 출력 y만으로 계산할 수 있다.
단순한 sigmoid 노드 하나로 대체할 수 있다.

간소화 버전은 역전파 과정의 중간 계산들을 생략할 수 있어 더 효율적인 계산이다.
또, 노드를 그룹화하여 Sigmod 계층의 세세한 내용을 노출하지 않고 입력과 출력에만 집중할 수 있다.

dL/dy y**2 exp(-x)  =dL/dy {1/(1+exp(-x))**2}*exp(-x)
                    =dL/dy {1/(1+exp(-x))}*exp(-x)/(1+exp(-x))
                    =dL/dy y(1-y)

-> y의 출력만으로 계산할 수 있다.
'''
import numpy as np

class Sigmoid:
    def __init__(self): #순전파의 출력을 out에 보관했다가 역전파 계산 때 그 값을 사용한다.
        self.out=None

    def forward(self, x):   #순전파 계산
        out=1/(1+np.exp(-x))   #시그모이드 함수
        self.out=out

        return out
    
    def backward(self, dout):   #역전파 계산
        dx=dout*(1.0-self.out)*self.out

        return dx