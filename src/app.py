from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config import config

from routes.user import users
from routes.practice import practices
from routes.process import process
from routes.resource import resources
from routes.practice_grade import practiceGrades
from routes.practice_topic import practiceTopics
from routes.topics import topics
from routes.grades import grades

from routes.auth import routes_auth

app = Flask(__name__)
app.config.from_object(config['development'])

CORS(app)
SQLAlchemy(app)
Marshmallow(app)
Bcrypt(app)

url_prefix = "/api"

app.register_blueprint(users, url_prefix=url_prefix)
app.register_blueprint(practices, url_prefix=url_prefix)
app.register_blueprint(practiceGrades, url_prefix=url_prefix)
app.register_blueprint(practiceTopics, url_prefix=url_prefix)
app.register_blueprint(process, url_prefix=url_prefix)
app.register_blueprint(resources, url_prefix=url_prefix)
app.register_blueprint(topics, url_prefix=url_prefix)
app.register_blueprint(grades, url_prefix=url_prefix)

app.register_blueprint(routes_auth)