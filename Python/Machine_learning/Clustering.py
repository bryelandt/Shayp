from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# K_means calculation -------------------------

def K_means(events_array,k):
    """
        Define k clusters for the event list return array of labels
    """

    kmeans = KMeans(n_clusters=k)

    # print(events_array[0:10,:])

    kmeans.fit(events_array)

    return kmeans.labels_

# Clusters evaluation -------------------------

def calculate_WSS(points, kmax):
    """
        Calculate within cluster sum of squares

        input:
        - data to cluster
        - kmax (max number of clusters)
        return sum of square for each cluster number (0 to kmax)
    """

    sse = []
    for k in range(1, kmax+1):
        kmeans = KMeans(n_clusters = k).fit(points)
        centroids = kmeans.cluster_centers_
        pred_clusters = kmeans.predict(points)
        curr_sse = 0

        # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
        for i in range(len(points)):
            curr_center = centroids[pred_clusters[i]]
            curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2

        sse.append(curr_sse)
    return sse

def calculate_Silouette(points,kmax):
    """
        Calculate within cluster sum of squares

        input:
        - data to cluster
        - kmax (max number of clusters)
        return silouette score for each cluster number (0 to kmax)
    """

    sil = []

    # dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
    for k in range(2, kmax+1):
        kmeans = KMeans(n_clusters = k).fit(points)
        labels = kmeans.labels_
        sil.append(silhouette_score(points, labels, metric = 'euclidean'))

    return sil
