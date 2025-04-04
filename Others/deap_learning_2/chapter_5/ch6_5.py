#BetterRnnlm 클래스 구현
import sys
sys.path.append('..')
from time_layers import *
from np import *
from base_model import BaseModel

class BetterRnnlm(BaseModel):
    def __init__(self, vocab_size=10000, wordvec_size=650, hidden_size=650, dropout_ratio=0.5):
        V,D,H=vocab_size, wordvec_size, hidden_size
        rn=np.random.randn

        embed_W=(rn(V,D)/100).astype('f')
        lstm_Wx1=(rn(D,4*H)/np.sqrt(D)).astype('f')
        lstm_Wh1=(rn(H,4*H)/np.sqrt(H)).astype('f')
        lstm_b1=np.zeros(4*H).astype('f')
        lstm_Wx2=(rn(H, 4*H)/np.sqrt(H)).astype('f')
        lstm_Wh2=(rn(H, 4*H)/np.sqrt(H)).astype('f')
        lstm_b2=np.zeros(4*H).astype('f')
        affine_b=np.zeros(V).astype('f')

        #세 가지 개선점
        self.layers=[
            TimeEmbedding(embed_W),
            TimeDropout(dropout_ratio),
            TimeLSTM(lstm_Wx1, lstm_Wh1, lstm_b1, stateful=True),
            TimeDropout(dropout_ratio),
            TimeLSTM(lstm_Wx2, lstm_Wh2, lstm_b2, stateful=True),
            TimeDropout(dropout_ratio),
            TimeAffine(embed_W.T, affine_b) #가중치 공유
        ]
        self.loss_layer=TimeSoftmaxWithLoss()
        self.lstm_layers=[self.layers[2], self.layers[4]]
        self.drop_layers=[self.layers[1], self.layers[3], self.layers[5]]

        self.params, self.grads=[], []
        for layer in self.layers:
            self.params+=layer.parmas
            self.grads+=layer.grads

    def predict(self, xs, train_flg=False):
        for layer in self.drop_layers:
            layer.train_flg=train_flg
        for layer in self.layers:
            xs=layer.forward(xs)
        return xs
    
    def forward(self, xs, ts, train_flg=True):
        score=self.predict(xs, train_flg)
        loss=self.loss_layer.forward(score, ts)
        return loss
    
    def backward(self, dout=1):
        dout=self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout=layer.backward(dout)
        return dout
    
    def reset_state(self):
        for layer in self.lstm_layers:
            layer.reset_state()

            