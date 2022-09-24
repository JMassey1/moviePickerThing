import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jsglue import JSGlue

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    jsglue = JSGlue()

    app = Flask(__name__)
    jsglue.init_app(app)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    # app.config['SECRET_KEY'] = 'poopballs'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nxvnzhntksleiy:495c35c97e888d7b91dc720b059d10667c2b77760bbd263b22a23870f56ee4d3@ec2-34-230-110-100.compute-1.amazonaws.com:5432/d9afb5mopl9u7o'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Movie

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

