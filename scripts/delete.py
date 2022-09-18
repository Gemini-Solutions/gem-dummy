from flask import request
from flask_restful import Resource
from scripts.db_connection import DB_connection


class Delete(Resource):
    @classmethod
    def delete(cls):
        try:
            id_s = request.args.get("id")
            if id_s == None:
                return {"msg": "Invalid Parameters"}
            data = DB_connection().delete_query(id_s)
            if data == None:
                return {"msg": "Invalid given Employee ID"}
        except:
            return {"msg": "Invalid given Arguments",
                    "Valid fields" : "employee_id"}
        return {
            "msg" : "Deleted Successfuly",
            "deleted data" : data
        }
