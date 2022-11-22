from app  import db
from flask_login import UserMixin

def load_user(id):
    return User.query.get(Int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), index=True, unique=True)
    passsword = db.Column(db.String(128))
    roles = db.Column(db.String)

    def get_id(self):
        return (self.id)