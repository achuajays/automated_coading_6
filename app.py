
import streamlit as st
from clustering import perform_clustering
from visualization import plot_clusters

def main():
    st.title('Customer Segmentation App')
    st.write("This app uses K-means clustering to segment customers based on purchasing behavior.")
    
    # Parameters for clustering
    num_clusters = st.sidebar.number_input('Number of Clusters (K)', min_value=2, max_value=20, value=5)
    data_path = st.sidebar.text_input('Data File Path', 'data.csv')
    
    if st.button('Segment Customers'):
        centroids, labels = perform_clustering(data_path, num_clusters)
        plot_clusters(centroids, labels, data_path)

if __name__ == "__main__":
    main()
