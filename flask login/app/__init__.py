from flask import Flask
from .models import db
from .routes import register_routes

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app