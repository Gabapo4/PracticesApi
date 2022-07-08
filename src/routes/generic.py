from flask import jsonify, request
from utils.db import db
import json

def response(status,data=None,message=None,error=None):
    return  jsonify({
        "status":status,
        "data":data,
        "message":message,
        "error":error
        })

def get_all(model,schema):
    try:
        resultDB = model.query.all()
        model_schema = schema(many=True)
        resultJson = model_schema.dump(resultDB)
        return response("success", resultJson)
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))

def get_by_id(id,model,schema):
    try:
        resultDB = model.query.get(id)
        if resultDB:
            model_schema = schema()
            resultJson = model_schema.dump(resultDB)
            return response("success", resultJson)

        return response("Fail", None, "Data not found...")
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))

def add(model,fields):
    try:
        new_model = model()
        for field in fields:
            setattr(new_model,field,request.form[field])

        db.session.add(new_model)
        db.session.commit()
        
        return response("success", new_model.id)
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))

def update(id,model,fields):
    try:
        resultDB = model.query.get(id)
        if resultDB:
            for field in fields:
                setattr(resultDB,field,request.form[field])
            db.session.commit()
            return response("success")

        return response("Fail", None, "Data not found...")
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))
        
def delete(id,model):
    try:
        resultDB = model.query.get(id)
        if resultDB:
            db.session.delete(resultDB)
            db.session.commit()
            return response("success")

        return response("Fail", None, "Data not found...")
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))

def deleteByPracticeId(id,model):
    try:
        resultDB = model.query.filter_by(practice_id=id).all()
        if resultDB:
            for row in resultDB:
                db.session.delete(row)
            db.session.commit()
            return response("success")
        return response("Fail", None, "Data not found...")
    except Exception as e:
        return response("fail", None, "Error, no se pudo llevar acabo la accion...", str(e))