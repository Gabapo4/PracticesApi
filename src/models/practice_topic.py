from utils.db import db, ma

class PracticeTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    practice_id = db.Column(db.Integer, db.ForeignKey("practice.id"))
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"))

    def __init__(self, name=None, practice_id=None, topic_id=None):
        self.practice_id = practice_id
        self.topic_id = topic_id

class PracticeTopicSchema(ma.Schema):
    class Meta:
        fields = ("id", "practice_id", "topic_id")