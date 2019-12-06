from app import db
from hashutils import make_pw_hash


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id')) #connects blog to user via user id 

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body
        self.owner = owner
    
    def _repr__(self):
        return '<blog %r>' % self.name

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True) #email can only be used once
    pw_hash = db.Column(db.String(120)
    blogs = db.relationship('Blog', backref='owner') #establishes relationship between blog and user
    
    def __init__(self, email.password):
        self.email = email
        self.pw_hash = make_pw_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email
