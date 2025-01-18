#차원 감소 방식-피쳐 추출feature selection
#PCA 기반의 피쳐 추출 방법

'''
데이터의 변화의 폭이 가장 큰 축을 정하고, 그 다음 그와 직교하는 축을 구한다.
데이터의 중심점에 축을 위치 시켜 0.0을 중심으로 데이터가 양쪽으로 균등하게\
퍼지도록 분포를 시켜 축을 뒤틀어 원래의 데이터를 변화시킨다.
-> 데이터의 중심축을 0, 0으로 위치시킬 수 있고, 가장 데이터의 변화폭이 큰 순으로\
X, Y축 등을 지정하여 데이터를 볼 수 있다.


*PCA를 이용한 차원의 감소

그러면 PCA 분석을 이용하여 차원을 어떻게 감소시킬까?
PCA 분석을 하더라도, 단순히 축을 틀어버려서 차원의 수는 줄어들지 않는다.
pCA 분석을 하면, 각 피쳐(축) 별로, 값의 변화도(Variance:해당 축의 값이 얼마나 크게 변하는가)를\
볼 수 있다.
'''

'''
Sklearn을 이용한 PCA 분석과 차원 감소

3차원인 IRIS 데이터를 PCA 분석을 통해 2차원으로 줄인다.
원본 데이터를 생성하고 시각화한다.
'''
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

iris = datasets.load_iris()
labels = pd.DataFrame(iris.target)
labels.columns=['labels']
#데이터 생성
data = pd.DataFrame(iris.data,columns=['Sepal length','Sepal width','Petal length','Petal width'])

#그래프 시각화(3차원)
fig = plt.figure( figsize=(6,6))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(data['Sepal length'],data['Sepal width'],data['Petal length'],c=labels,alpha=0.5)
ax.set_xlabel('Sepal lenth')    #x축
ax.set_ylabel('Sepal width')    #y축
ax.set_zlabel('Petal length')   #z축
plt.show()


#PCA 분석을 통해, 각 피쳐(축)별 Varience를 분석
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Create scaler: scaler
scaler = StandardScaler()

# # Create a PCA instance: pca
pca = PCA()

# # Create pipeline: pipeline
pipeline = make_pipeline(scaler,pca)

# # Fit the pipeline to 'samples'
pipeline.fit(data)

features = range(pca.n_components_)

# features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()

#PCA 변환된 피쳐(축)중 0, 1번 피쳐만 사용해서 시각화
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model=PCA(n_components=2)
pca_features=model.fit_transform(data)

xf=pca_features[:,0]
yf=pca_features[:,1]
plt.scatter(xf, yf, c=labels)
plt.show()
'''
2차원으로 줄여도 IRIS 군집화의 특성이 어느정도 남아있는 것을 확인할 수 있다.
'''

#1차원으로 줄여서 시각화
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model=PCA(n_components=1)
pca_features=model.fit_transform(data)

xf=pca_features[:,0]
yf=len(xf)*[0]
plt.scatter(xf, yf, c=labels)
plt.show()
'''
2차원에 비해서 -1~4 사이에 분포된 2개의 클래스(녹색과 노랑색)이 다소 겹치는 부분이 있지만\
전체적으로 봤을 때 1차원으로 변환해도 어느 정도 분류 특성을 유지하고 있는 것을 볼 수 있다.

이런 중첩 현상을 줄여주는 차원 감소 기법으로는 t-SNE라는 방법이 있다.
'''