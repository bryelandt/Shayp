from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering

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

def calculate_dendrogram(points):

# setting distance_threshold=0 ensures we compute the full tree.
    model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

    model = model.fit(points)

    plt.title('Hierarchical Clustering Dendrogram')
    # plot the top three levels of the dendrogram
    plot_dendrogram(model)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()

    n_cluster = int(input('enter the number of clusters: '))
    model = AgglomerativeClustering(n_clusters=n_cluster)

    model = model.fit(points)
    return model.labels_

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix)
