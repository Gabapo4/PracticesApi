from flask import Blueprint
from models.practice_topic import PracticeTopic, PracticeTopicSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

practiceTopics = Blueprint('practiceTopics', __name__)
route="/practiceTopic"
fields=["practice_id","topic_id"]

@practiceTopics.route(route)
def index():
    practiceTopics = get_all(PracticeTopic,PracticeTopicSchema)
    print(practiceTopics)
    return practiceTopics

@practiceTopics.route(route+"/<id>")
@verify_token_middleware
def get_practiceTopic_by_id(id):
    return get_by_id(id, PracticeTopic,PracticeTopicSchema)

@practiceTopics.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_practiceTopic():
    return add(PracticeTopic, fields)

@practiceTopics.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_practiceTopic(id):
    return update(id, PracticeTopic, fields)
    
@practiceTopics.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_practiceTopic(id):
    return delete(id, PracticeTopic)

