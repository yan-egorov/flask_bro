from app import db
from werkzeug import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    nickname = db.Column(db.String(64), index = True, unique = True)
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    something = db.Column(db.String(2000))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)    

    def __init__(self, firstname, nickname, lastname, something, email, password):
        self.firstname = firstname.title()
        self.nickname = nickname.title()
        self.lastname = lastname.title()
        self.something = something
        self.email = email.lower()
        self.set_password(password)
        self.role = ROLE_ADMIN if nickname.lower() == "admin" else ROLE_USER
        
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
  
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    def __repr__(self):
        return '<Post %r>' % (self.body)