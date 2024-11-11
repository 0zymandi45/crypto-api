from flask import Flask
from app.config.config import Config
from app.routes.api_routes import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
