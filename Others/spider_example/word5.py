#데이터 정규화
from collections import Counter
...

def getNgrams(content, n):
    content=cleanInput(content) 
    #cleanInput 메서드에 content=content.upper()를 추가-> 2-그램의 총 숫자는 변함 없지만 중복을 제거한 숫자는 줄어든다.
    ngrams=Counter()

    ngrams_list=[]
    for sentence in content:
        newNgrams=[' '.join(ngrams) for ngram in getNgramsFromSentence(sentence, n)]
        ngrams_list.extend(newNgrams)   #2-그램을 만나면 리스트에 추가
        ngrams.update(newNgrams)

    return(ngrams)

'''
중복된 2-그램이 많다.
2-그램을 만나면 리스트에 추가할 뿐 그 빈도를 기록하지도 않았다.
2-그램이 존재하느지만 보기보다는 그 빈도를 기록하면 데이터 정리 알고리즘이나\
정규화 알고리즘을 바꿨을 때 어떤 효과가 있는지 알아보는 데 유용하다.

데이터를 성공적으로 정규화하면 중복 없는 n-그램의 총 숫자는 줄어들겠지만\
n-그램의 총 숫자는 줄어들지 않을 것이다.
'''

'''
n-그램을 딕셔너리 객체에 추가하고 값은 해당 n-그램이 몇번 나타났는지 나타내면\
코드 관리가 좀 더 복잡하고 정렬하기도 어렵다는 단점이 있다.

반면, Counter 객체를 쓸 때, 리스트는 해시를 적용할 수 없으므로 Counter 객체에 저장할 수 없어\
각 n-그램마다 리스트 내포 안에서 ' '.join(ngram)을 통해 먼저 문자열로 바꿔야 한다.
'''