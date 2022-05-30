from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta

from routes.generic import response

def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRETTOKENKEY"), algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRETTOKENKEY"), algorithms="HS256")
        decode(token, key=getenv("SECRETTOKENKEY"), algorithms="HS256")
    except exceptions.DecodeError:
        return response("fail", None, "token invalido...")
    except exceptions.ExpiredSignatureError:
        #response.status_code = 401
        return response("fail", None, "token expirado...")
