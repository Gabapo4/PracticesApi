from flask import Blueprint
from models.grade import Grade, GradeSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

grades = Blueprint('grades', __name__)
route="/grade"
fields=["name"]

@grades.route(route)
def index():
    return get_all(Grade,GradeSchema)

@grades.route(route+"/<id>")
@verify_token_middleware
def get_grade_by_id(id):
    return get_by_id(id, Grade,GradeSchema)

@grades.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_grade():
    return add(Grade, fields)

@grades.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_grade(id):
    return update(id, Grade, fields)
    
@grades.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_grade(id):
    return delete(id, Grade)

