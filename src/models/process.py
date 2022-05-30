from utils.db import db, ma

class Process(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    position = db.Column(db.String(2))

    practice_id = db.Column(db.Integer, db.ForeignKey("practice.id"))

    def __init__(self, name=None, description=None, position=None, practice_id=None):
        self.name = name
        self.description = description
        self.position = position
        self.practice_id = practice_id

class ProcessSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "position", "practice_id")
