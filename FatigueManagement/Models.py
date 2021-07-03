#User Models

from FatigueManagement import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#create the user table
class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id= db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, index = True)
    email = db.Column(db.String(64), unique=True, index =True)
    subunit = db.Column(db.String(20), nullable = False)
    trade = db.Column(db.String(20), nullable = False)
    password_hashed = db.Column(db.String(128))
    reports = db.relationship('Report', backref = "author", lazy = True)

    def __init__(self, username, email, subunit, trade, password):
        self.username = username
        self.email = email
        self.subunit = subunit
        self.trade = trade
        self.password_hashed = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hashed,password)

    def __repr__(self):
        return f'Username: {self.username}'

class Report (db.Model):
    __tablename__ = 'Reports'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(20), db.ForeignKey(User.username), nullable = False)
    # build out the model after convo with Denver
