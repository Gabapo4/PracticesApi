from utils.db import db, ma

class Practice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    code = db.Column(db.String(5))
    public = db.Column(db.Integer)
    image = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, name=None, description=None, code=None, public=None, image=None, user_id=None):
        self.name = name
        self.description = description
        self.code = code
        self.public = public
        self.image = image
        self.user_id = user_id

class PracticeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "code", "public", "image","user_id")