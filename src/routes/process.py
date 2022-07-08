from flask import Blueprint
from models.process import Process, ProcessSchema
from .generic import get_all, get_by_id, add, update, delete, deleteByPracticeId
from middleware.token_middleware import verify_token_middleware

process = Blueprint('process', __name__)
route="/process"
fields=["name","description","position","practice_id"]

@process.route(route)
def index():
    process = get_all(Process,ProcessSchema)
    print(process)
    return process

@process.route(route+"/<id>")
@verify_token_middleware
def get_process_by_id(id):
    return get_by_id(id, Process,ProcessSchema)

@process.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_process():
    return add(Process, fields)

@process.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_process(id):
    return update(id, Process, fields)
    
@process.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_process(id):
    return delete(id, Process)

#Querys Especiales
@process.route(route+"/deleteAllById/<id>", methods=['DELETE'])
def delete_processAllById(id):
    return deleteByPracticeId(id, Process)