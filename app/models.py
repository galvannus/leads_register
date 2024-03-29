import datetime

from flask_login import UserMixin

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    #Atributos
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(94), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    leads = db.relationship('Lead')

    def verify_password(self, password):
        return check_password_hash(self.encrypted_password, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)

    #Retorna el usuario por consola
    def __str__(self):
        return self.username

    #Metodo de clase
    @classmethod
    def create_element(cls, username, password, email):
        user = User(username=username, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return user
    
    #Metodo de validación de username
    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()
    
    #Metodo de validación de email
    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()

    #Metodo de validación de id
    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()

class Lead(db.Model):
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    fullname = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())