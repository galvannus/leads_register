from flask import Flask

from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

#Instancias
app = Flask(__name__)
bootstrap = Bootstrap()
csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()

#Importaciónes desde otro archivo
from .views import page
from .models import User

def create_app(config):
    app.config.from_object(config)

    
    csrf.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(page)

    with app.app_context():
        #Cración de conexión a BD
        db.init_app(app)
        #Creación de tablas
        db.create_all()
    
    return app