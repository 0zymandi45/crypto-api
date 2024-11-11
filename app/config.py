import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/your_db")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret")
