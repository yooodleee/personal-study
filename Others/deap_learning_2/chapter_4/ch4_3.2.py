#CBOW 모델 학습 코드
import sys
sys.path.append('..')
import numpy as np
from common import config

config.GPU=True

import pickle
from trainer import Trainer
from optimizer import Adam
from cbow import CBOW
from util import create_contexts_target, to_cpu, to_gpu
from dataset import ptb

#하이퍼 파라미터 설정
window_size=5
hidden_size=100
bath_size=100
max_epoch=10

#데이터 읽기
corpus, word_to_id, id_to_word=ptb.load_data('train')
vocab_size=len(word_to_id)

contexts, target=create_contexts_target(corpus, window_size)
if config.GPU:
    contexts, target=to_gpu(contexts), to_gpu(target)

#모델 생성
model=CBOW(vocab_size, hidden_size, window_size, corpus)
optimizer=Adam()
trainer=Trainer(model, optimizer)

#학습 시작
trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()

#나중에 사용할 수 있도록 필요한 데이터 저장
words_vecs=model.word_vecs
if config.GPU:
    words_vecs=to_gpu(words_vecs)
params={}
params['word_vecs']=words_vecs.astype(np.float16)
params['word_to_id']=word_to_id
params['id_to_word']=id_to_word
pkl_file='cbow_params.pkl'
with open(pkl_file, 'wb') as f:
    pickle.dump(params, f, -1)