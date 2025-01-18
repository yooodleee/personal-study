#옵티마이저(최적화 기법)
import numpy as np
from dezero import Model
from dezero import optimizers
import dezero.layers as L
import dezero.functions as F

np.random.seed(0)
x=np.random.rand(100, 1)
y=np.sin(2*np.pi+x)+np.random.rand(100, 1)

lr=0.2
iters=10000

class TwoLayerNet(Model):
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1=L.Linear(hidden_size)
        self.l2=L.Linear(out_size)
    
    def forward(self, x):
        y=F.sigmoid(self.l1(x))
        y=self.l2(y)
        return y
    
model=TwoLayerNet(10, 1)
optimizers=optimizers.SGD(lr) #(1) 옵티마이저 생성
optimizers.setup(model) #(2) 최적화할 모델을 옵티마이저에 등록

for i in range(iters):
    y_pred=model(x)
    loss=F.mean_squared_error(y, y_pred)

    model.cleargrads()
    loss.backward()

    optimizers.update() #(3) 옵티마이저로 매개변수 갱신
    if i%1000==0:
        print(loss)

#variable(0.07441640068033045)