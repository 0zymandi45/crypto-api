from flask import Blueprint, jsonify, request
from .service import get_currency_price_from_api

api_bp = Blueprint('api', __name__)

@api_bp.route('/currency', methods=['GET'])
def get_currency_price():
    currency = request.args.get('currency', 'BTC')
    result = get_currency(currency)
    
    if "error" in result:
        return jsonify(result), 500
    
    return jsonify({"currency": currency, "price": result["price"], "cached": result["cached"]})
