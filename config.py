class Config:
    SECRET_KEY = 'alejandro'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://jorge:123123@localhost/leads_register'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_MAPS_API_KEY = 'AIzaSyAnTzEhULJBmTvmgbpDD8QJM60okEelkNc'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}