from utils.db import db, ma

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    practice_id = db.Column(db.Integer, db.ForeignKey("practice.id"))

    def __init__(self, name=None, practice_id=None):
        self.name = name
        self.practice_id = practice_id

class ResourceSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "practice_id")