
import pandas as pd
from sklearn.cluster import KMeans

def perform_clustering(data_path, num_clusters):
    # Load data
    data = pd.read_csv(data_path)
    
    # Assuming the data has features that can be used for clustering
    features = data.select_dtypes(include='number')
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(features)
    centroids = kmeans.cluster_centers_
    
    return centroids, labels
