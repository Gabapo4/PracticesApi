from functools import wraps
from flask import request
from utils.function_jwt import validate_token

def verify_token_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        response = validate_token(token, output=False)

        if(response):
            return response
        return func(*args, **kwargs)
    return decorated_function