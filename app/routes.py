from flask import render_template,url_for, redirect,flash,session
from flask_login import login_user,logout_user, current_user, login_required, LoginManager
from app import app, db
from app.forms import LoginForm
from app.models import User


### login ###
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def Load_user(user):
    return User.query.get(int(user))

@app.route('/')
def index():
    return render_template('index.html')
    #return "test"



@app.route('/login' ,methods=['GET','POST'])
@login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    form_username = form.username.data
    form_password = form.password.data

    if form.validate_on_submit():
        user = User.query.fitler_by(user=form_username).frist()
        password = user.password
        if user is none or password != form_password:
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user)
        session.permanent = True
        return  redirect(url_for('index'))
    return render_template('login.html',title='Sign In' ,form =form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))