# Test authentication
import pytest

def test_login_success(client):
    """Teste para login bem-sucedido"""
    data = {'username': 'test_user', 'password': 'test_password'}
    response = client.post('/auth/login', json=data)
    assert response.status_code == 200
    assert 'token' in response.json

def test_login_failure(client):
    """Teste para falha de login"""
    data = {'username': 'wrong_user', 'password': 'wrong_password'}
    response = client.post('/auth/login', json=data)
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

def test_protected_route_without_token(client):
    """Teste de acesso a rota protegida sem token"""
    response = client.get('/protected')
    assert response.status_code == 401

def test_protected_route_with_token(client, jwt_token):
    """Teste de acesso a rota protegida com token JWT válido"""
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = client.get('/protected', headers=headers)
    assert response.status_code == 200
