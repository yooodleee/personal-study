#맥락과 타깃
import sys
sys.path.append('..')
from util import preprocess

text='You say goodbye and I say hello.'
corpus, id_to_word, word_to_id=preprocess(text)
print(corpus)
#[0 1 2 3 4 1 5 6]

print(id_to_word)
#{'you': 0, 'say': 1, 'goodbye': 2, 'and': 3, 'i': 4, 'hello': 5, '.': 6}

import numpy as np

def create_context_target(corpus, window_size=1):
    target=corpus[window_size:-window_size]
    context=[]

    for idx in range(-window_size, len(corpus)-window_size):
        cs=[]
        for t in range(-window_size, window_size+1):
            if t==0:
                continue
            cs.append(corpus[idx+1])
        context.append(cs)
    
    return np.array(context), np.array(target)

context, target=create_context_target(corpus, window_size=1)

print(context)
# [[0 0]
#  [1 1]
#  [2 2]
#  [3 3]
#  [4 4]
#  [1 1]
#  [5 5]
#  [6 6]]

print(target)
#[1 2 3 4 1 5]

def create_contexts_target(corpus, window_size=1):
    target=corpus[window_size:-window_size]
    context=[]

    for idx in range(-window_size, len(corpus)-window_size):
        cs=[]
        for t in range(-window_size, window_size+1):
            if t==0:
                continue
            cs.append(corpus[idx+1])
        context.append(cs)
    
    return np.array(context), np.array(target)