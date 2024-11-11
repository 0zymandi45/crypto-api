from flask import Blueprint, jsonify, request
from app.services.bitcoin_service import get_price
from app.utils.cache import cache

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/price/<currency>", methods=["GET"])
@cache(timeout=60)  # Cache for 60 seconds
def price(currency):
    try:
        price_data = get_price(currency)
        return jsonify({"price": price_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
