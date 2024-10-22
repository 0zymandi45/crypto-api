from app.models import Currency

def test_insert_currency(client):
    """Teste de inserção no MongoDB"""
    new_currency = {'name': 'ethereum', 'price': 2500}
    response = client.post('/currency', json=new_currency)
    assert response.status_code == 201
    assert 'id' in response.json

def test_fetch_currency_from_db(client):
    """Teste de busca de dados no MongoDB"""
    # Simula inserção de uma moeda no MongoDB
    currency = Currency(name='bitcoin', price=30000)
    currency.save()

    response = client.get('/currency/bitcoin')
    assert response.status_code == 200
    assert response.json['price'] == 30000
