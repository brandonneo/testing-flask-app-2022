from flask import render_template,url_for, redirect
from flask_login  import login_user,logout_user, current_user, login_required, LoginManager
from app import app, db
# from app import app
from app.models import User


### login ###
login_manager = LoginManger()
login_manager.init_app(app)

def Load_user(User_id):
    return User.query.get(int(User_id))

@app.route('/')
def index():
    return render_template('index.html')
    #return "test"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))