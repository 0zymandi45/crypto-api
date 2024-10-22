def test_cache_hit(client, jwt_token, mock_cache):
    """Teste de cache hit"""
    headers = {'Authorization': f'Bearer {jwt_token}'}
    # Primeiro request popula o cache
    response = client.get('/currency/bitcoin', headers=headers)
    assert response.status_code == 200
    price_before = response.json['price']

    # Segundo request simula hit no cache
    response = client.get('/currency/bitcoin', headers=headers)
    assert response.status_code == 200
    price_after = response.json['price']
    assert price_before == price_after  # Deve ser igual já que o cache foi usado

def test_cache_miss(client, jwt_token, mock_cache):
    """Teste de cache miss"""
    headers = {'Authorization': f'Bearer {jwt_token}'}
    # Simula um cache miss
    mock_cache.clear()
    response = client.get('/currency/bitcoin', headers=headers)
    assert response.status_code == 200
