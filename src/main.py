from agents import DataCollector, DataProcessor, ResultPresenter
from config import config
from exceptions import AgentError
from utils.logger import setup_logger
import json
import sys

logger = setup_logger("main")

def main():
    try:
        # Ajanları oluştur
        collector = DataCollector()
        processor = DataProcessor()
        presenter = ResultPresenter()
        
        # Veri toplama isteği
        initial_request = json.dumps({
            "source": {
                "type": "csv",
                "path": f"{config.DATA_DIR}/input.csv"
            }
        })
        
        logger.info("Veri toplama başlıyor...")
        collected_data = collector.process(initial_request)
        
        logger.info("Veri işleme başlıyor...")
        processed_data = processor.process(collected_data)
        
        logger.info("Sonuçlar hazırlanıyor...")
        final_results = presenter.process(processed_data)
        
        # Sonuçları yazdır
        results = json.loads(final_results)["data"]["report"]
        logger.info("İşlem tamamlandı!")
        print("\nSonuçlar:")
        print(json.dumps(results, indent=2))
        
    except AgentError as e:
        logger.error(f"Ajan hatası: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Beklenmeyen hata: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 