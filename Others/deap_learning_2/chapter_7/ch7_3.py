#초기화 메서드
import numpy as np
from time_layers import TimeEmbedding, TimeLSTM, TimeAffine, TimeSoftmaxWithLoss
from base_model import BaseModel

class Encoder:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V,D,H=vocab_size, wordvec_size, hidden_size
        rn=np.random.randn

        embed_W=(rn(V,D)/100).astype('f')
        lstm_Wx=(rn(D,4*H)/np.sqrt(D)).astype('f')
        lstm_Wh=(rn(H,4*H)/np.sqrt(H)).astype('f')
        lstm_b=np.zeros(4*H).astype('f')

        self.embed=TimeEmbedding(embed_W)
        self.lstm=TimeLSTM(lstm_Wx, lstm_Wh, lstm_b, stateful=False)

        self.params=self.embed.params+self.lstm.params
        self.grads=self.embed.grads+self.lstm.grads
        self.hs=None
    
    def forward(self, xs):
        xs=self.embed.forward(xs)
        hs=self.lstm.forward(xs)
        self.hs=hs
        return hs[:,-1,:]
    
    def backward(self, dh):
        dhs=np.zeros_like(self.hs)
        dhs[:,-1,:]=dh

        dout=self.lstm.backward(dhs)
        dout=self.embed.backward(dout)
        return dout

class Decoder:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V,D,H=vocab_size, wordvec_size, hidden_size
        rn=np.random.randn

        embed_W=(rn(V,D)/100).astype('f')
        lstm_Wx=(rn(D,4*D)/np.sqrt(D)).astype('f')
        lstm_Wh=(rn(D,4*D)/np.sqrt(D)).astype('f')
        lstm_b=np.zeros(V).astype('f')
        affine_W=(rn(H,V)/np.sqrt(H)).astype('f')
        affine_b=np.zeros(V).astype('f')

        self.embed=TimeEmbedding(embed_W)
        self.lstm=TimeLSTM(lstm_Wx, lstm_Wh, lstm_b)
        self.affine=TimeAffine(affine_W, affine_b)

        self.params, self.grads=[], []
        for layer in (self.embed, self.lstm, self.affine):
            self.params+=layer.params
            self.grads+=layer.grads
    
    def forward(self, xs, h):
        self.lstm.set_state(h)

        out=self.embed.forward(xs)
        out=self.lstm.forward(out)
        score=self.affine.forward(out)
        return score
    
    def backward(self, dscore):
        dout=self.affine.backward(dscore)
        dout=self.lstm.backward(dout)
        dout=self.embed.backward(dout)
        dh=self.lstm.dh
        return dh
    
    def generate(self, h, start_id, sample_size):
        sampled=[]
        sample_id=start_id
        self.lstm.set_state()

        for _ in range(sample_size):
            x=np.array(sample_id).reshape((1,1))
            out=self.embed.forward(x)
            out=self.lstm.forward(out)
            score=self.affine.forward(out)

            sample_id=np.argmax(score.flatten())
            sampled.append(int(sample_id))
    
        return sampled

class Seq2seq(BaseModel):
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V,D,H=vocab_size, wordvec_size, hidden_size
        self.encoder=Encoder(V,D,H)
        self.decoder=Decoder(V,D,H)
        self.softmax=TimeSoftmaxWithLoss()

        self.params=self.encoder.params+self.decoder.params
        self.grads=self.encoder.grads+self.decoder.grads

    def forward(self, xs, ts):
        decoder_xs, decoder_ts=xs[:, :-1], ts[:, :-1]
        h=self.encoder.forward(xs)
        score=self.decoder.forward(decoder_xs, h)
        loss=self.softmax.forward(score, decoder_ts)
        return loss
    
    def backward(self, dout=1):
        dout=self.softmax.backward(dout)
        dh=self.decoder.backward(dout)
        dout=self.encoder.backward(dh)
        return dout
    
    def generate(self, xs, start_id, sample_size):
        h=self.encoder.forward(xs)
        sampled=self.decoder.generate(h, start_id, sample_size)
        return sampled


#seq2seq 평가
import sys
sys.path.append('..')
import matplotlib.pyplot as plt
from sequence import load_data, get_vocab
from optimizer import Adam
from trainer import Trainer
from util import eval_seq2seq
from seq2seq import Seq2seq, Encoder
from peeky_seq2seq import PeekySeq2seq

#데이터셋 읽기
(x_train, t_train), (x_test, t_test)=load_data('addition.txt')
x_train, x_test=x_train[:, ::-1], x_test[:, ::-1]
char_to_id, id_to_char=get_vocab()

#하이퍼파라미터 설정
vocab_size=len(char_to_id)
wordvec_size=16
hidden_size=128
batch_size=128
max_epoch=25
max_grad=5.0

#모델/옵티마이저/트레이너 생성
model=Seq2seq(vocab_size, wordvec_size, hidden_size)
optimizer=Adam()
trainer=Trainer(model, optimizer)

acc_list=[]
for epoch in range(max_epoch):
    trainer.fit(x_train, t_train, max_epoch=1, batch_size=batch_size, max_grad=max_grad)
    
    correct_num=0
    for i in range(len(x_test)):
        question, correct=x_test[[i]], t_test[[i]]
        verbose=i<10
        correct_num+=eval_seq2seq(model, question, correct, id_to_char, verbose)
        acc=float(correct_num)/len(x_test)
        acc_list.append(acc)
        print('검증 정확도 %.3f%%' %(acc*100))

class PeekyDecoder:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V,D,H=vocab_size, wordvec_size, hidden_size
        rn=np.random.randn

        embed_W=(rn(V,D)/100).astype('f')
        lstm_Wx=(rn(H+D, 4*H)/np.sqrt(H+D)).astype('f')
        lstm_Wh=(rn(H,4*H)/np.sqrt(H)).astype('f')
        lstm_b=np.zeros(4*H).astype('f')
        affine_W=(rn(H+H, V)/np.sqrt(H+H)).astype('f')
        affine_b=np.zeros(V).astype('f')

        self.embed=TimeEmbedding(embed_W)
        self.lstm=TimeLSTM(lstm_Wx, lstm_Wh, lstm_b)
        self.affine=TimeAffine(affine_W, affine_b)

        self.params, self.grads=[], []
        for layer in (self.embed, self.lstm, self.affine):
            self.params+=layer.params
            self.grads+=layer.grads
        self.cache=None

    def forward(self, xs, h):
        N,T=xs.shape
        N,H=h.shape

        self.lstm.set_state(h)

        out=self.embed.forward(xs)
        hs=np.repeat(h, T, axis=0).reshape(N,T,H)
        out=np.concatenate((hs, out), axis=2)

        out=self.lstm.forward(out)
        out=np.concatenate((hs, out), axis=2)

        score=self.affine.forward(out)
        self.cache=H
        return score

class PeekySeq2seq(Seq2seq):
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V,D,H=vocab_size, wordvec_size, hidden_size
        self.encoder=Encoder(V,D,H)
        self.decoder=PeekyDecoder(V,D,H)
        self.softmax=TimeSoftmaxWithLoss()

        self.params=self.encoder.params+self.decoder.params
        self.grads=self.encoder.grads+self.decoder.grads