#Rnnlm 클래스 구현
import sys
sys.path.append('..')
from time_layers import *
import pickle
import numpy as np

class Rnnlm:
    def __init__(self, vocab_size=10000, wordvec_size=100, hidden_size=100):
        V,D,H=vocab_size, wordvec_size, hidden_size
        rn=np.random.randn

        #가중치 초기화
        embed_W=(rn(V,D)/100).astype('f')
        lstm_Wx=(rn(D,4*H)/np.sqrt(D)).astype('f')
        lstm_Wh=(rn(H,4*H)/np.sqrt(H)).astype('f')
        lstm_b=np.zeros(4*H).astype('f')
        affine_W=(rn(H,V)/np.sqrt(H)).astype('f')
        affine_b=np.zeros(V).astype('f')

        #계층 생성
        self.layers=[
            TimeEmbedding(embed_W),
            TimeLSTM(lstm_Wx, lstm_Wh, lstm_b, stateful=True),
            TimeAffine(affine_W, affine_b)
        ]
        self.loss_layer=TimeSoftmaxWithLoss()
        self.lstm_layer=self.layers[1]

        #모든 가중치와 기울기를 리스트에 모은다.
        self.parmas, self.grads=[], []
        for layer in self.layers:
            self.parmas+=layer.params
            self.grads+=layer.grads
    
    def predict(self, xs):
        for layer in self.layers:
            xs=layer.forward(xs)
        return xs
    
    def forward(self, xs, ts):
        score=self.predict(xs)
        loss=self.loss_layer.forward(score, ts)
        return loss
    
    def backward(self, dout=1):
        dout=self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout=layer.backward(dout)
        return dout
    
    def reset_state(self):
        self.lstm_layer.reset_state()
    
    def save_params(self, file_name='Rnnlm.pkl'):
        with open(file_name, 'wb') as f:
            pickle.dump(self.parmas, f)
    
    def load_params(self, file_name='Rnnlm.pkl'):
        with open(file_name, 'rb') as f:
            self.parmas=pickle.load(f)


import sys
sys.path.append('..')
from optimizer import SGD
from trainer import RnnlmTrainer
from ptb import load_data
from util import eval_perplexity

#하이퍼파라미터 설정
batch_size=20
wordvec_size=100#RNN의 은닉 상태 벡터의 원소 수
hidden_size=100#RNN을 펼치는 크기
time_size=35
lr=20.0
max_epoch=4
max_grad=0.25

#학습 데이터 읽기
corpus, word_to_id, id_to_word=load_data('train')
corpus_test, _, _=load_data('test')
vocab_size=len(word_to_id)
xs=corpus[:-1]
ts=corpus[1:]

#모델 생성
model=Rnnlm(vocab_size, wordvec_size, hidden_size)
optimizer=SGD(lr)
trainer=RnnlmTrainer(model, optimizer)

#(1) 기울기 클리핑을 적용하여 학습
trainer.fit(xs, ts, max_epoch, batch_size, time_size, max_grad, eval_interval=20)
trainer.plot(ylim=(0, 500))

#(2) 테스트 데이터로 평가
model.reset_state()
ppl_test=eval_perplexity(model, corpus_test)
print('테스트 퍼플렉서티: ', ppl_test)

#(3) 매개변수 저장
model.save_params()

# #기울기 구하기
# model.forward(...)
# model.backward(...)
# params, grads=model.parmas, model.grads

# #기울기 클리핑
# if max_grad is not None:
#     clip_grads(grads, max_grad)

# #매개변수 갱신
# optimizer.update(params, grads)