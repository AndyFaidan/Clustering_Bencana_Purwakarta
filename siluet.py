# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt

# Memuat data dari CSV
file_path = "DatasetDRB_peta.csv"
df = pd.read_csv(file_path)

# Normalisasi data menggunakan StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(['Kecamatan', 'Latitude', 'Longitude'], axis=1))

# List untuk menyimpan nilai silhouette score
silhouette_scores = []

# Range jumlah klaster yang akan dicoba
range_n_clusters = [2, 3, 4, 5, 6, 7, 8]

for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, random_state=0, max_iter=50)
    kmeans.fit(X_scaled)

    # Mendapatkan label klaster untuk setiap data point
    cluster_labels = kmeans.labels_

    # Menghitung silhouette score
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    
    # Menyimpan nilai silhouette score
    silhouette_scores.append(silhouette_avg)

    print("For n_clusters = {0}, the silhouette score is {1:.2f}".format(num_clusters, silhouette_avg))

# Menampilkan grafik silhouette score untuk setiap jumlah klaster
plt.plot(range_n_clusters, silhouette_scores, marker='o')
plt.title('Silhouette Score for Different Numbers of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()
