import os
from dataclasses import dataclass

@dataclass
class Config:
    # Veri yolları
    DATA_DIR: str = "data"
    RESULTS_DIR: str = "results"
    
    # Model parametreleri
    PCA_N_COMPONENTS: int = 2
    KMEANS_N_CLUSTERS: int = 3
    RANDOM_STATE: int = 42
    
    # Görselleştirme ayarları
    FIGURE_SIZE: tuple = (10, 6)
    
    def __post_init__(self):
        # Gerekli klasörleri oluştur
        os.makedirs(self.DATA_DIR, exist_ok=True)
        os.makedirs(self.RESULTS_DIR, exist_ok=True)

config = Config() 