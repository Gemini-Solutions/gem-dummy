# import requests
from flask import request, make_response
from flask_restful import Resource
# from scripts.post import req
# from scripts.connection import Connection
from scripts.db_connection import DB_connection


class Get(Resource):
    @classmethod
    def get(cls):
        try:
            par = request.args.get("id")
            if par == None:
                msg =  {"msg": "Invalid Parameters"}
                return make_response(msg, 403)
            data = DB_connection().find_query(par)
            if data == None:
                msg = {"msg": "Data Not available for the given id"}
                return make_response(msg, 403)
            return {"status": "Successful",
                    "Data": data}
        except:
            return {"msg": "Invalid given Arguments",
                    "Valid fields" : "employee_id"}