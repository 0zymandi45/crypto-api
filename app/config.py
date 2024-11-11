import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    
    # Configuração do Redis
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_EXPIRATION = timedelta(minutes=int(os.getenv("REDIS_EXPIRATION_MINUTES", 10)))
    
    # Configuração de MongoDB (caso necessário)
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/crypto_db")
    
    # Configuração da API externa
    API_URL = os.getenv("API_URL", "https://api.mercadobitcoin.net/api/v4/ticker")

config = Config()

