 # tests/test_agents.py
import pytest
from src.agents import DataCollector, DataProcessor, ResultPresenter
from src.exceptions import AgentError
import json

@pytest.fixture
def sample_data():
    return {
        "source": {
            "type": "csv",
            "path": "tests/data/test_input.csv"
        }
    }

def test_data_collector(sample_data):
    collector = DataCollector()
    result = collector.process(json.dumps(sample_data))
    data = json.loads(result)
    
    assert "agent" in data
    assert data["agent"] == "data_collector"
    assert "type" in data
    assert "data" in data

def test_data_processor():
    processor = DataProcessor()
    with pytest.raises(AgentError):
        processor.process("invalid_message")

def test_result_presenter():
    presenter = ResultPresenter()
    with pytest.raises(AgentError):
        presenter.process("invalid_message")
        
