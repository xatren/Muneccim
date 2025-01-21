from abc import ABC, abstractmethod
import json
from ..utils.logger import setup_logger
from ..exceptions import AgentError

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = setup_logger(f"agent.{name}")
        
    @abstractmethod
    def process(self, message):
        pass
        
    def create_message(self, data, message_type):
        try:
            return json.dumps({
                "agent": self.name,
                "type": message_type,
                "data": data
            })
        except Exception as e:
            self.logger.error(f"Mesaj oluşturma hatası: {str(e)}")
            raise AgentError(f"Mesaj oluşturulamadı: {str(e)}")
            
    def validate_message(self, message):
        """Gelen mesajın geçerliliğini kontrol et"""
        try:
            data = json.loads(message)
            required_fields = ["agent", "type", "data"]
            
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Eksik alan: {field}")
                    
            return data
        except json.JSONDecodeError:
            raise AgentError("Geçersiz JSON formatı")
        except ValueError as e:
            raise AgentError(str(e)) 