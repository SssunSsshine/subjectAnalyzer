from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    from .models import models_bp
    app.register_blueprint(models_bp)

    return app
