#네거티브 샘플링의 샘플링 기법
import numpy as np

print(np.random.choice(10))
#6

print(np.random.choice(10))
#7

words=['you', 'say', 'goodbye', 'I', 'hello', '.']
print(np.random.choice(words))
#.

#5개만 무작위로 샘플링(중복 있음)
print(np.random.choice(words, size=5))
#['hello' 'goodbye' 'goodbye' '.' 'goodbye']

#5개만 무작위로 샘플링(중복 없음)
print(np.random.choice(words, size=5, replace=False))
#['you' '.' 'I' 'goodbye' 'say']

#확률 분포에 따라 샘플링
p=[0.5, 0.1, 0.05, 0.2, 0.05, 0.1]
print(np.random.choice(words, p=p))
#you

p=[0.7, 0.29, 0.01]
new_p=np.power(p, 0.75)
new_p/=np.sum(new_p)
print(new_p)
#[0.64196878 0.33150408 0.02652714]

corpus=np.array([0,1,2,3,4,1,2,3])
power=0.75
sample_size=2

from negative_sampling_layer import UnigramSampler, EmbeddingDot
from layers import SigmoidWithLoss

sampler=UnigramSampler(corpus, power, sample_size)
target=np.array([1, 3, 0])
negative_sample=sampler.get_negative_sample(target)
print(negative_sample)

class NegativeSamplingLoss:
    def __init__(self, W, corpus, power=0.75, sample_size=5):
        self.sample_size=sample_size
        self.sampler=UnigramSampler(corpus, power, sample_size)
        self.loss_layer=[SigmoidWithLoss() for _ in range(sample_size+1)]
        self.embed_dot_layers=[EmbeddingDot(W) for _ in range(sample_size+1)]
        self.params, self.grads=[], []

        for layer in self.embed_dot_layers:
            self.params+=layer.params
            self.grads+=layer.grads
    
    def forward(self, h, target):
        batch_size=target.shape[0]
        negative_sample=self.sampler.get_negative_sample(target)

        score=self.embed_dot_layers[0].forward(h, target)
        correct_label=np.ones(batch_size, dtype=np.int32)
        loss=self.loss_layer[0].forward(score, correct_label)

        negative_label=np.zeros(batch_size, dtype=np.int32)
        for i in range(self.sample_size):
            negative_target=negative_sample[:,i]
            score=self.embed_dot_layers[1+i].forward(h, negative_target)
            loss+=self.loss_layer[1+i].forward(score, negative_label)
        
        return loss
    
    def backward(self, dout=1):
        dh=0
        for 10, 11 in zip(self.loss_layer, self.embed_dot_layers):
            dscore=10.backward(dscore)
            dh+=11.backward(dscore)
        
        return dh
    