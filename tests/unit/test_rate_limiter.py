import pytest
import redis
from src.utils.rate_limiter import RateLimiter  # Importe da localização correta


class TestRateLimiter:
    def setup_method(self):
        # Crie um cliente Redis de teste
        self.redis_client = redis.Redis(host='localhost', port=6379, db=15)
        # Limpe o banco de dados antes de cada teste
        self.redis_client.flushdb()

    def test_initial_request_allowed(self):
        """Testa se a primeira requisição é sempre permitida"""
        # Passe o cliente Redis como primeiro argumento
        limiter = RateLimiter(
            redis_client=self.redis_client,
            max_requests=100,
            window=60
        )

        # Teste deve passar um user_id
        assert limiter.allow_request("user1") is True

    def test_request_limit_exceeded(self):
        """Testa se as requisições são limitadas corretamente"""
        limiter = RateLimiter(
            redis_client=self.redis_client,
            max_requests=3,
            window=60
        )

        # Permite as 3 primeiras requisições
        for _ in range(3):
            assert limiter.allow_request("user2") is True

        # A quarta requisição deve ser rejeitada
        assert limiter.allow_request("user2") is False