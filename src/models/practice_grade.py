from utils.db import db, ma

class PracticeGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    practice_id = db.Column(db.Integer, db.ForeignKey("practice.id"))
    grade_id = db.Column(db.Integer, db.ForeignKey("grade.id"))

    def __init__(self, name=None, practice_id=None, grade_id=None):
        self.practice_id = practice_id
        self.grade_id = grade_id

class PracticeGradeSchema(ma.Schema):
    class Meta:
        fields = ("id", "practice_id", "grade_id")