from flask import Blueprint, jsonify, request
from .cache import cache_data, get_cached_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/currency', methods=['GET'])
def get_currency_price():
    currency = request.args.get('currency', 'BTC')
    cache_key = f"currency_{currency}"

    # Verifica se o valor está no cache
    cached_price = get_cached_data(cache_key)
    if cached_price:
        return jsonify({"currency": currency, "price": cached_price, "cached": True})

    # Aqui, simula-se a chamada para obter o preço (substitua pela chamada real)
    price = 50000  # Exemplo de preço estático
    cache_data(cache_key, price)
    return jsonify({"currency": currency, "price": price, "cached": False})
