from flask import Blueprint
from models.resource import Resource, ResourceSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

resources = Blueprint('resources', __name__)
route="/resource"
fields=["name","practice_id"]

@resources.route(route)
def index():
    resources = get_all(Resource,ResourceSchema)
    print(resources)
    return resources

@resources.route(route+"/<id>")
@verify_token_middleware
def get_resource_by_id(id):
    return get_by_id(id, Resource,ResourceSchema)

@resources.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_resource():
    return add(Resource, fields)

@resources.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_resource(id):
    return update(id, Resource, fields)
    
@resources.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_resource(id):
    return delete(id, Resource)

