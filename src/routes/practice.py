from flask import Blueprint, request
from models.practice import Practice, PracticeSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

practices = Blueprint('practices', __name__)
route="/practice"
fields=["name","description","code","public","image","user_id"]

from flask import jsonify
import json
def response(status,data=None,message=None,error=None):
    return  jsonify({
        "status":status,
        "data":data,
        "message":message,
        "error":error
        })

@practices.route(route)
def index():
    practices = get_all(Practice,PracticeSchema)
    print(practices)
    return practices

@practices.route(route+"/<id>")
@verify_token_middleware
def get_practice_by_id(id):
    return get_by_id(id, Practice,PracticeSchema)

@practices.route(route+"/add", methods=["POST"])
def add_practice():
    return add(Practice, fields)

@practices.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_practice(id):
    return update(id, Practice, fields)
    
@practices.route(route+"/delete/<id>", methods=['DELETE'])
def delete_practice(id):
    return delete(id, Practice)

