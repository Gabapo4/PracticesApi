from utils.db import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))

    def __init__(self, name=None,  lastname=None , username=None,  password=None):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.password = password
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "lastname", "username", "password")
