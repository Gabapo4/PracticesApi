from flask import Blueprint
from models.topic import Topic, TopicSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

topics = Blueprint('topics', __name__)
route="/topic"
fields=["name","description"]

@topics.route(route)
def index():
    return get_all(Topic,TopicSchema)

@topics.route(route+"/<id>")
@verify_token_middleware
def get_topic_by_id(id):
    return get_by_id(id, Topic,TopicSchema)

@topics.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_topic():
    return add(Topic, fields)

@topics.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_topic(id):
    return update(id, Topic, fields)
    
@topics.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_topic(id):
    return delete(id, Topic)

