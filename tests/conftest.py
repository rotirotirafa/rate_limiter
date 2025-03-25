import pytest
import redis
from src.app import app

@pytest.fixture(scope="session")
def test_redis_client():
    """Cliente Redis para testes"""
    test_redis = redis.Redis(host='localhost', port=6379, db=15)
    yield test_redis
    test_redis.flushdb()

@pytest.fixture(scope="module")
def api_client():
    """Cliente de teste para FastAPI"""
    from fastapi.testclient import TestClient
    return TestClient(app)