from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os
import json

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jjk'
    app.config.from_object(config_class)
    # Initialize
    db.init_app(app)
    login_manager.init_app(app)

    # User loader (imported here to avoid circular import)
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Register blueprint
    from app.routes import bp
    app.register_blueprint(bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app