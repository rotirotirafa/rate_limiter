# Rate Limiter

## Descrição
O Rate Limiter é um sistema que limita a quantidade de requisições que um usuário pode fazer em um determinado período de tempo. O sistema é composto por um servidor HTTP que recebe as requisições dos usuários e um banco de dados que armazena as informações sobre as requisições.

## Requisitos
- Docker

## Run
Para rodar o sistema, execute o comando abaixo:
```docker compose up -d```

## Endpoints
- GET /
- GET /item
- GET /item/xpto

Pode ser acessado via browser http://localhost:8000/docs

# Portas
- 8000: Servidor HTTP
- 6379: Redis


