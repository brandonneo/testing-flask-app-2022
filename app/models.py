from app  import db
from flask_login import UserMixin

def load_user(id):
    return User.query.get(Int(id))

# def load_role(roles):
#     return User.query.get(roles)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))


    def get_id(self):
        return (self.id)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(64))
