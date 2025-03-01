
import matplotlib.pyplot as plt
import pandas as pd

def plot_clusters(centroids, labels, data_path):
    data = pd.read_csv(data_path)
    data['Cluster'] = labels  # Add the cluster label to data
    
    features = data.select_dtypes(include='number')
    
    # Plotting only first two features for simplicity
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(features.iloc[:, 0], features.iloc[:, 1], c=data['Code'], cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', label='Centroids')
    plt.xlabel(features.columns[0])
    plt.ylabel(features.columns[1])
    plt.title('Customer Segments')
    plt.legend()
    plt.show()
