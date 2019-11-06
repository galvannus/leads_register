class Config:
    SECRET_KEY = ''
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}