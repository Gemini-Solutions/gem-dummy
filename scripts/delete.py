from flask import request, make_response
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
                msg = {"msg": "Invalid given Employee ID"}
                return make_response(msg, 403)
        except:
            return {"msg": "Invalid given Arguments",
                    "Valid fields" : "employee_id"}
        return {
            "msg" : "Deleted Successfuly",
            "deleted data" : data
        }
