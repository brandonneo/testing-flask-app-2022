from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/users_db'

#create database
db=SQLAlchemy(app)

login = LoginManager(app)

from app import routes, models

if __name__ == '__main__':
    app.run(debug=True)
