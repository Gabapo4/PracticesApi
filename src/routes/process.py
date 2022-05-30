from flask import Blueprint
from models.process import Process, ProcessSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

processs = Blueprint('processs', __name__)
route="/process"
fields=["name","description","position","practice_id"]

@processs.route(route)
def index():
    processs = get_all(Process,ProcessSchema)
    print(processs)
    return processs

@processs.route(route+"/<id>")
@verify_token_middleware
def get_process_by_id(id):
    return get_by_id(id, Process,ProcessSchema)

@processs.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_process():
    return add(Process, fields)

@processs.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_process(id):
    return update(id, Process, fields)
    
@processs.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_process(id):
    return delete(id, Process)

