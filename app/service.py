import requests
from .cache import cache_data, get_cached_data

# URL da API externa - troque para a URL real do Mercado Bitcoin
API_URL = "https://api.mercadobitcoin.net/api/v4/ticker"

def get_currency(currency):
    cache_key = f"currency_{currency}"
    
    # Tenta recuperar o preço do cache Redis
    cached_price = get_cached_data(cache_key)
    if cached_price:
        return {"price": cached_price, "cached": True}

    # Faz a chamada à API externa caso o valor não esteja no cache
    try:
        response = requests.get(f"{API_URL}/{currency}")
        response.raise_for_status()
        price_data = response.json()
        price = price_data.get("last")  # Exemplo de chave "last" como preço atual
        cache_data(cache_key, price)
        return {"price": price, "cached": False}
    except requests.RequestException as e:
        return {"error": "Erro ao consultar a API externa", "details": str(e)}

