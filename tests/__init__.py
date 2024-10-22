import pytest
from app import create_app
from app.models import db
from pymongo import MongoClient

@pytest.fixture(scope='module')
def client():
    """Sets up the Flask test client for the application"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_db'  # Test database
    app.config['JWT_SECRET_KEY'] = 'test_jwt_secret_key'  # Test JWT key
    app.config['CACHE_TYPE'] = 'SimpleCache'  # Simple cache type for testing

    with app.test_client() as client:
        with app.app_context():
            # Initialize the MongoDB connection
            mongo = MongoClient(app.config['MONGO_URI'])
            db.init_app(app)
            db.connection.drop_database('test_db')  # Clean the test DB before
