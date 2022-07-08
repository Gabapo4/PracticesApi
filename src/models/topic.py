from utils.db import db, ma

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    icon = db.Column(db.String(50))

    def __init__(self, name=None, description=None, icon=None):
        self.name = name
        self.description = description
        self.icon = icon
    
class TopicSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "icon")

    #_links = ma.Hyperlinks(
    #    {
    #        "self": ma.URLFor("topic_detail", values=dict(id="<id>")),
    #        "collection": ma.URLFor("topics"),
    #    }
    #)