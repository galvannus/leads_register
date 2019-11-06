LIBRERIAS

Flask
pip install Flask

Virtualenv
pip install virtualenv

WTForms
pip install WTForms

Bootstrap
pip install Flask-Bootstrap4

Flask Script
pip install Flask-Script

I use virtualenv with python3

CSRF
pip install Flask-WTF

Database
SQLAlchemy
pip isntall Flask-SQLAlchemy

Mysql client
pip install mysqlclient

If you have a problem installing mysqlclient, try this:

sudo apt-get install python-dev python3-dev
sudo apt-get install libmysqlclient-dev
pip install pymysql
pip install mysqlclient

Werkzeug
pip install Werkzeug

Flask-Login
pip install flask-login

Do you need to create the config.py file with this variables
class Config:
    SECRET_KEY = 'secret_key'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/leads_register'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}