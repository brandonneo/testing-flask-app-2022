from flask import render_template
#from flask_login  import login_user,logout_user, current_user, login_required, LoginManager
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')
    #return "test"

### login ###
# login_manager = LoginManger()
# login_manager.init_app(app)

def Load_user(User_id):
    return User.query.get(int(User_id))
