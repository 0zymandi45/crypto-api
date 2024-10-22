# Test API routes
def test_home_route(client):
    """Teste da rota home"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask API" in response.data

def test_get_currency_price(client, jwt_token):
    """Teste de requisição de preço de moeda"""
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = client.get('/currency/bitcoin', headers=headers)
    assert response.status_code == 200
    assert 'price' in response.json

def test_missing_currency(client, jwt_token):
    """Teste de requisição de moeda inexistente"""
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = client.get('/currency/nonexistentcoin', headers=headers)
    assert response.status_code == 404
    