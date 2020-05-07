import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.main.views import views
from app.controls.operacoes import operacoes
from app.model.models import models

db = SQLAlchemy()
app_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY') or 'key hesthouse')

    # DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////home/osboxes/Documentos/projetos/automator/buscaimplacavel/web/app/bd/bot.db')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///' + app_dir +  '/bd/bot.db')
    
    app.config['MEDIA_ROOT'] = os.path.join(app_dir, 'gallery/')
    app.config['FILES'] = os.path.join(app_dir, 'files/')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.environ.get('GMAIL_USER') or 'papersrs2002@gmail.com'
    app.config['MAIL_PASSWORD'] = os.environ.get('GMAIL_PASSWORD') or 'ujlatqnjwmprumxd'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'resthouse.oficial@gmail.com'

    app.register_blueprint(views)
    app.register_blueprint(models)
    app.register_blueprint(operacoes)
    
    bootstrap = Bootstrap(app)
    db.init_app(app)

    return app
