from .base_agent import BaseAgent
import pandas as pd
import json

class DataCollector(BaseAgent):
    def __init__(self):
        super().__init__("data_collector")
        
    def process(self, message):
        # Mesaj JSON formatında kaynak bilgisi içermeli
        config = json.loads(message)
        
        # Veri kaynağından okuma
        data = self._read_data(config["source"])
        
        # Sonucu JSON formatında döndür
        return self.create_message(
            data=data.to_dict(),
            message_type="collected_data"
        )
        
    def _read_data(self, source):
        if source["type"] == "csv":
            return pd.read_csv(source["path"])
        # Diğer kaynak tipleri eklenebilir
        raise ValueError(f"Desteklenmeyen kaynak tipi: {source['type']}") 