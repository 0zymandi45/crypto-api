import pytest
from app import create_app
from flask import jsonify
from unittest.mock import patch

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@patch('app.routes.get_currency')
def test_get_currency_price(mock_get_currency_price_from_api, client):
    # Dados simulados que a função vai retornar
    mock_get_currency_price_from_api.return_value = {"price": 20000, "cached": False}

    # Teste para consultar o preço da moeda (usando o mock)
    response = client.get('/currency?currency=BTC')

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['currency'] == 'BTC'
    assert json_data['price'] == 20000
    assert json_data['cached'] is False

@patch('app.routes.get_currency_price_from_api')
def test_get_currency_price_cached(mock_get_currency_price_from_api, client):
    # Dados simulados para quando o preço for encontrado no cache
    mock_get_currency_price_from_api.return_value = {"price": 15000, "cached": True}

    # Teste para consultar o preço da moeda quando o valor está no cache
    response = client.get('/currency?currency=BTC')

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['currency'] == 'BTC'
    assert json_data['price'] == 15000
    assert json_data['cached'] is True

@patch('app.routes.get_currency_price_from_api')
def test_get_currency_price_error(mock_get_currency_price_from_api, client):
    # Simula um erro na consulta à API externa
    mock_get_currency_price_from_api.return_value = {"error": "Erro ao consultar a API externa", "details": "Erro de rede"}

    # Teste para verificar quando há um erro na consulta
    response = client.get('/currency?currency=BTC')

    assert response.status_code == 500
    json_data = response.get_json()
    assert json_data['error'] == "Erro ao consultar a API externa"
    assert json_data['details'] == "Erro de rede"
