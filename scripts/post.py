from flask import request, make_response
from flask_restful import Resource
from scripts.db_connection import DB_connection


class Post(Resource):
    @classmethod
    def post(cls):
        try:
            req = request.get_json()
            if req["employee_id"] == None:
                msg = {"msg": "Employee Id should not be Null or None"}
                return make_response(msg, 400)
            DB_connection().insert_doc(req)
            return {"status" : "Successful",
                    "Data":req}
        except:
            msg = {"msg": "Employee Id should not be Null or None"}
            return make_response(msg, 400)