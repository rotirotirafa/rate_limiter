# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /src

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requirements primeiro para aproveitamento do cache de camadas do Docker
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código da aplicação
COPY . .

# Variáveis de ambiente para configuração
ENV APP_MODULE=src.app:app
ENV HOST=0.0.0.0
ENV PORT=8000

# Expõe a porta que a aplicação vai rodar
EXPOSE 8000

# Usa Uvicorn como servidor ASGI para FastAPI
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.app:app"]