from utils.db import db, ma

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name=None):
        self.name = name
    
class GradeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
