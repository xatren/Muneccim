# src/exceptions.py
class AgentError(Exception):
    """Temel ajan hatası"""
    pass

class DataCollectionError(AgentError):
    """Veri toplama hatası"""
    pass

class ProcessingError(AgentError):
    """Veri işleme hatası"""
    pass

class PresentationError(AgentError):
    """Sonuç sunumu hatası"""
    pass