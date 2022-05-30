from flask import Blueprint, request, jsonify
from os import getenv
from models.user import User, UserSchema
from .generic import get_all, get_by_id, add, update, delete, response
from middleware.token_middleware import verify_token_middleware

from utils.db import db, bcrypt

users = Blueprint('users', __name__)
route="/user"
fields=["name", "lastname", "username", "password"]

@users.route(route)
@verify_token_middleware
def index():
    return get_all(User,UserSchema)

@users.route(route+"/<id>")
@verify_token_middleware
def get_user_by_id(id):
    return get_by_id(id, User,UserSchema)

@users.route(route+"/add", methods=["POST"])
def add_user():
    key=getenv("SECRETTOKENKEY")
    name = request.form["name"]
    lastname = request.form["lastname"]
    username = request.form["username"]
    password = request.form["password"]

    resultDB = User.query.filter_by(username=username).first()
    model_schema = UserSchema()
    resultJson = model_schema.dump(resultDB)
    if(resultJson):
        return response("fail", None, "El nombre del usuario ya esta utilizado...")

    encrypted_password = bcrypt.generate_password_hash(password + key).decode("UTF-8")
    try:
        new_user = User(name,lastname,username,encrypted_password)  
        db.session.add(new_user)
        db.session.commit() 
        return response("success")
    except Exception:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...")

@users.route(route+"/update/<id>", methods=['PUT'])
@verify_token_middleware
def update_user(id):
    return update(id, User, fields)
    
@users.route(route+"/delete/<id>", methods=['DELETE'])
@verify_token_middleware
def delete_user(id):
    return delete(id, User)

