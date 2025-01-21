from .base_agent import BaseAgent
import matplotlib.pyplot as plt
import seaborn as sns
import json
import numpy as np

class ResultPresenter(BaseAgent):
    def __init__(self):
        super().__init__("result_presenter")
        
    def process(self, message):
        results = json.loads(message)["data"]
        
        # Görselleştirme
        self._create_visualizations(results)
        
        # Rapor oluştur
        report = self._generate_report(results)
        
        return self.create_message({
            "report": report,
            "visualizations": "saved_to_disk"  # Gerçek uygulamada dosya yolları eklenebilir
        }, "final_results")
        
    def _create_visualizations(self, results):
        pca_results = np.array(results["pca_results"])
        clusters = np.array(results["clusters"])
        
        plt.figure(figsize=(10, 6))
        plt.scatter(pca_results[:, 0], pca_results[:, 1], c=clusters, cmap='viridis')
        plt.title("PCA ve Kümeleme Sonuçları")
        plt.xlabel("Birinci Ana Bileşen")
        plt.ylabel("İkinci Ana Bileşen")
        plt.savefig("results/clustering.png")
        plt.close()
        
    def _generate_report(self, results):
        return {
            "explained_variance": results["explained_variance"],
            "cluster_count": len(set(results["clusters"])),
            "inertia": results["inertia"]
        } 