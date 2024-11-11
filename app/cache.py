import redis
import os
import json
from datetime import timedelta

# Configurar Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

def cache_data(key, data, expiration=timedelta(minutes=10)):
    """
    Cacheia dados em Redis com uma chave e tempo de expiração.
    """
    redis_client.setex(key, expiration, json.dumps(data))

def get_cached_data(key):
    """
    Recupera dados cacheados do Redis por chave.
    """
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None
