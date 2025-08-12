from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
mg = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mg.init_app(app, db)


    from app.routes.route_main import main_bp
    from app.routes.route_yugioh import yugioh_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(yugioh_bp)


    with app.app_context():
        db.create_all()

    return app