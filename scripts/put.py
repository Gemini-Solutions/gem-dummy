from flask import request
from flask_restful import Resource
from scripts.db_connection import DB_connection


class Put(Resource):
    @classmethod
    def put(cls):
        try:
            req = request.get_json()
            exp, id_s = req["experience"],req["employee id"]
            if exp == None or id_s == None:
                return {"msg": "Invalid Parameters"}
            data = DB_connection().update_query(id_s,exp)
            if data == None:
                return {"msg": "Invalid given Employee ID"}
        except:
            return {"msg": "Invalid given Arguments",
                    "Valid fields" : "employee_id, experience"}
        return {
            "msg" : "Updated Successfuly",
            "Updated data" : data
        }
