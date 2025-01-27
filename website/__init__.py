from flask import Flask


def create_app():
    app = Flask(__name__) #Initialises flask
    app.config['SECRET_KEY'] = 'abcdef' #Encrypts and secures cookies and session data of website

    from .views import views #Imports blueprints
    from.auth import auth

    app.register_blueprint(views, url_prefix='/') #Registers blueprints and assigns url prefix as none
    app.register_blueprint(auth, url_prefix='/')

    return app
