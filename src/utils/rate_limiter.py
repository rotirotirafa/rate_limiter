import time

class RateLimiter:
    """
    Rate Limiter para APIs.
    Limita o número de requisições por usuário em um determinado intervalo de tempo
    redis_client: Cliente Redis para armazenar os dados de rate limiting
    max_requests: Número máximo de requisições permitidas
    window: Intervalo de tempo em segundos
    """

    def __init__(self, redis_client, max_requests=100, window=60):
        self.redis = redis_client
        self.max_requests = max_requests
        self.window = window

    def allow_request(self, user_id) -> bool:
        """Verifica se a requisição pode ser processada dentro do limite."""
        now = time.time()
        key = f"rate_limit:{user_id}"

        pipe = self.redis.pipeline()
        pipe.zadd(key, {now: now})
        pipe.zremrangebyscore(key, 0, now - self.window)
        pipe.zcard(key)
        pipe.expire(key, self.window * 2)

        _, _, request_count, _ = pipe.execute()

        result = request_count <= self.max_requests

        return result