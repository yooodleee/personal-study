# K-Means Clustering(K-Means)
import sklearn
import sklearn.cluster
import sklearn.metrics


sklearn.cluster.KMeans(
    n_clusters=8,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=0.0001,
    precompute_distance="auto",
    verbose=0,
    random_state=None,
    copy_x=True,
    n_jobs=1,
    algorithm="auto"
)


# Cluster Evaluation
sklearn.metrics.silhouette_samples(X='', labels='')
sklearn.metrics.silhouette_score(X='', labels='')