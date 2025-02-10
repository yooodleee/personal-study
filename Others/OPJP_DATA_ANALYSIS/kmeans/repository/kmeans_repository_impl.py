import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from kmeans.repository.kmeans_repository import KMeansRepository


class KMeansRepositoryImpl(KMeansRepository):
    SAMPLE_COUNT = 100

    def createData(self):
        return {
            'AgeGroup': [],
            'FPS'
        }