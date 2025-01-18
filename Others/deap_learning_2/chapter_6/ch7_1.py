#문장 생성 구현(RnnlmGen)
import sys
sys.path.append('..')
from functions import softmax
from rnnlm import Rnnlm
from better_rnnlm import BetterRnnlm
import numpy as np

class RnnlmGen(Rnnlm):
    def generate(self, start_id, skip_ids=None, sample_size=100):
        word_ids=[start_id]

        x=start_id
        while len(word_ids)<sample_size:
            x=np.array(x).reshape(1,1)
            score=self.predict(x)
            p=softmax(score.flatten())

            sampled=np.random.choice(len(p), size=1, p=p)
            if (skip_ids is None) or (sampled not in skip_ids):
                x=sampled
                word_ids.append(int(x))
        return word_ids

import sys
sys.path.append('..')
from rnnlm_gen import RnnlmGen
from ptb import load_data

corpus, word_to_id, id_to_word=load_data('train')
vocab_size=len(word_to_id)
corpus_size=len(corpus)

model=RnnlmGen()
#model.load_params('../Rnnlm.pkl')

#시작(start) 문자와 건너뜀(skip) 문자 설정
start_word='you'
start_id=word_to_id[start_word]
skip_word=['N', '<unk>', '$']
skip_ids=[word_to_id[w] for w in skip_word]

#문장 생성
word_ids=model.generate(start_id, skip_ids)
txt=' '.join([id_to_word[i] for i in word_ids])
txt=txt.replace(' <eos>', '.\n')
print(txt)

# ' '.join(['you', 'say', 'goodbye'])

model.load_params('../Rnnlm.pkl')