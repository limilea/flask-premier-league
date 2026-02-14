import os
from flask import Flask
from epl.extensions import db, migrate
from epl.core.routes import core_bp
from epl.clubs.routes import club_bp
from epl.players.routes import player_bp


def create_app():
    app = Flask(__name__)

    # ถ้ามี DATABASE_URI ใน env ใช้อันนั้น
    # ถ้าไม่มี ให้ fallback เป็น sqlite
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        os.environ.get('DATABASE_URI') or 'sqlite:///epl.db'
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'supersecretkey'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(club_bp, url_prefix='/clubs')
    app.register_blueprint(player_bp, url_prefix='/players')

    return app
