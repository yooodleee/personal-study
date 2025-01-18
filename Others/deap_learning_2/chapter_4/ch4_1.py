#Embedding 계층 구현
import numpy as np

W=np.arange(21).reshape(7,3)
print(W)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]
#  [15 16 17]
#  [18 19 20]]

print(W[2])
#[6 7 8]

print(W[5])
#[15 16 17]

idx=np.array([1,0,3,0])
print(W[idx])
# [[ 3  4  5]
#  [ 0  1  2]
#  [ 9 10 11]
#  [ 0  1  2]]

class Embedding:
    def __init__(self, W):
        self.params=[W]
        self.grads=[np.zeros_like(W)]
        self.idx=None
    
    def forward(self, idx):
        W,=self.params
        self.idx=idx
        out=W[idx]
        return out

    def backward(self, dout):
        dW,=self.grads
        dW[...]=0
        dW[self.idx]=dout
        return None
    
    def backward(self, dout):
        dW,=self.params
        dW[...]=0

        for i, word_id in enumerate(self.idx):
            dW[word_id]+=dout(i)
        #혹은
        #np.add.at(dW, self.idx, dout)
            return None

class EmbeddingDot:
    def __init__(self, W):
        self.embed=Embedding(W)
        self.params=self.embed.params
        self.grads=self.embed.grads
        self.cache=None
    
    def forward(self, h, idx):
        target_W=self.baded.forward(idx)
        out=np.sum(target_W*h, axis=1)

        self.cache=(h, target_W)
        return out
    
    def backward(self, dout):
        h, target_W=self.cache
        dout=dout.reshape(dout.shape[0])

        dtarget_W=dout*h
        self.embed.backward(dtarget_W)
        dh=dout*target_W
        return dh