import redis
from fastapi import FastAPI
from urllib.request import Request
from starlette.responses import JSONResponse
from src.utils.rate_limiter import RateLimiter

redis_client = redis.Redis(host='redis', port=6379, db=0)
limiter = RateLimiter(redis_client)

app = FastAPI(
    title="RateLimiterApi",
    description="Rate Limiter para APIs",
    version="0.1.0",
)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Middleware de rate limiting para todas as rotas"""
    user_id = request.headers.get('X-User-ID', 'anonymous')

    if not limiter.allow_request(user_id):
        return JSONResponse(
            status_code=429,
            content={"message": "Limite de requisições excedido"}
        )

    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item")
async def get_xpto():
    """Rota de recurso protegida por rate limiting"""
    return {"message": "Recurso acessado com sucesso"}

@app.get("/item/xpto")
async def get_xpto():
    """Rota de recurso protegida por rate limiting"""
    return {"message": "Recurso acessado com sucesso"}
