from flask import Blueprint, request, jsonify
from os import getenv
from utils.function_jwt import write_token, validate_token

from models.user import User, UserSchema
from utils.db import bcrypt

from routes.generic import response

routes_auth = Blueprint('routes_auth', __name__)

@routes_auth.route("/login", methods=["POST"])
def login():
    key=getenv("SECRETTOKENKEY")
    username = request.form["username"]
    password = request.form["password"]
    resultDB = User.query.filter_by(username=username).first()
    model_schema = UserSchema()
    resultJson = model_schema.dump(resultDB)

    if resultJson:
        isPasswordCorrect = bcrypt.check_password_hash(resultJson["password"], password + key)
        if isPasswordCorrect:
            return write_token(data={"username":resultJson["username"], "name":resultJson["name"], "lastname":resultJson["lastname"]})
        else:
            return response("fail", None, "password incorrecto...")
    else:
        return response("fail", None, "usuario no valido...")


@routes_auth.route("/verify/token", methods=["POST"])
def verify():
    token = request.headers["Authorization"].split(" ")[1]
    return validate_token(token, output=True)