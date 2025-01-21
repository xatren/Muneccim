from .base_agent import BaseAgent
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import json

class DataProcessor(BaseAgent):
    def __init__(self):
        super().__init__("data_processor")
        
    def process(self, message):
        # Gelen veriyi DataFrame'e dönüştür
        data = pd.DataFrame(json.loads(message)["data"])
        
        # Veri temizleme ve dönüştürme
        processed_data = self._preprocess_data(data)
        
        # PCA uygula
        pca_results, explained_variance = self._apply_pca(processed_data)
        
        # Kümeleme
        clusters, inertia = self._apply_clustering(pca_results)
        
        return self.create_message({
            "pca_results": pca_results.tolist(),
            "explained_variance": explained_variance.tolist(),
            "clusters": clusters.tolist(),
            "inertia": float(inertia)
        }, "processed_data")
        
    def _preprocess_data(self, data):
        # Veri temizleme işlemleri
        return data
        
    def _apply_pca(self, data, n_components=2):
        pca = PCA(n_components=n_components)
        results = pca.fit_transform(data)
        return results, pca.explained_variance_ratio_
        
    def _apply_clustering(self, data, n_clusters=3):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(data)
        return clusters, kmeans.inertia_ 