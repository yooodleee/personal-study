#Trainer 클래스
'''
초기화 메서드는 신경망(모델)과 옵티마이저를 인수로 받는다.
'''
import sys
sys.path.append('..')
from optimizer import SGD
from trainer import Trainer
from dataset import spiral
from two_layer_net import TwoLayerNet

max_epoch=300   #학습을 수행하는 에폭 수
batch_size=30   #미니배치 크기
hidden_size=10  
learning_rate=1.0

x, t=spiral.load_data()
model=TwoLayerNet(input_size=2, hidden_size=hidden_size, output_size=3)
optimizer=SGD(lr=learning_rate)

trainer=Trainer(model, optimizer)
trainer.fit(x, t, max_epoch, batch_size, eval_interval=10)  
#eval_interval:결과(평균 손실 등)을 출력하는 간격, 10번째 반복마다 손실의 평균을 구해 출력한다.
trainer.plot()