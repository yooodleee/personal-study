# Mean-Shift(평균 이동)
from sklearn.cluster import MeanShift, estimate_bandwidth


# MeanShift 클래스
MeanShift(bandwidth= 9.)    # bandwidth 파라미터로 갖는다.


# estimate_bandwidth
best_bw = estimate_bandwidth(X='', quantile=2.) # Data와 quantile를 인자로 받는다.