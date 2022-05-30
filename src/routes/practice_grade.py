from flask import Blueprint
from models.practice_grade import PracticeGrade, PracticeGradeSchema
from .generic import get_all, get_by_id, add, update, delete
from middleware.token_middleware import verify_token_middleware

practiceGrades = Blueprint('practiceGrades', __name__)
route="/practiceGrade"
fields=["practice_id", "grade_id"]

@practiceGrades.route(route)
def index():
    practiceGrades = get_all(PracticeGrade,PracticeGradeSchema)
    print(practiceGrades)
    return practiceGrades

@practiceGrades.route(route+"/<id>")
@verify_token_middleware
def get_practiceGrade_by_id(id):
    return get_by_id(id, PracticeGrade,PracticeGradeSchema)

@practiceGrades.route(route+"/add", methods=["POST"])
@verify_token_middleware
def add_practiceGrade():
    return add(PracticeGrade, fields)

@practiceGrades.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_practiceGrade(id):
    return update(id, PracticeGrade, fields)
    
@practiceGrades.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_practiceGrade(id):
    return delete(id, PracticeGrade)

