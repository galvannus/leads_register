from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, HiddenField
from wtforms.fields.html5 import EmailField

from .models import User

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username esta fuera del rango')
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])

#Validación si el campo esta vacio (Para evitar bots)
def length_honeypot(form, field):
        if len(field.data) > 0:
            raise validators.ValidationError('Solo humanos pueden completar este registro!!')

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Correo electronico', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido.'),
        validators.Email(message='Ingrese un email valido.')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide.')
    ])
    confirm_password = PasswordField('Confirm Password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])
    honeypot = HiddenField('', [ length_honeypot ])

    #Metodo de validación de username
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso.')

    #Metodo de validación de email
    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso.')