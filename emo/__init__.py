from flask import Flask
# from os import environ, path
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_alembic import Alembic


# db=SQLAlchemy()
#  DB_NAME = 'projs.db'


def create_app():
    
    app=Flask(__name__)
    app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///projs.db'
     # {DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
     # db.init_app(app)
    
    
    # app.config['SECRET_KEY'] = 'secret-key-goes-here'
    # app.config['SQLAlCHEMY_DATABASE_URI'] = f'sqlite:///projs.db'
    # {DB_NAME}'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    # db.init_app(app)
    
    
    from .views import views
    from .auth import  auth
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    # from .models import User,Note
    
    # create_database(app)
    
    # login_manager=LoginManager()
    # login_manager.login_view='auth.login_page'#where we are redirected 
    # login_manager.init_app(app)#tells loginmanager which app we are using
    
    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))
    
    return app

# def create_database(app):
#     if not path.exists('bestauth/'+ DB_NAME):
#         db.create_all(app=app)
#         print('created database!')