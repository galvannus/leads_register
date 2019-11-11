from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user

from .forms import LoginForm, RegisterForm, LeadForm
from .models import User

from . import login_manager

page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='Index')

@page.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Cerraste sesión exitosamente')
    return redirect(url_for('.login'))

@page.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('.leads_list'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Usuario autenticado con exito')
        else:
            flash('Usuario o Password invalidos.', 'error')

    return render_template('auth/login.html', title='Login', form=form)

@page.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    #Se obtienen datos de la petición "request.form"
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            flash('Usuario registrado exitosamente.')

    return render_template('auth/register.html', title='Registro', form=form)

@page.route('/leads_list')
@login_required
def leads_list():
    return render_template('/leads/leads_list.html')

@page.route('/aria_ocean')
def new_lead():
    form = LeadForm()
    return render_template('/landing_pages/aria_ocean.html', title='Aria Ocean', form=form)