# import requests
from flask import request
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
                return {"msg": "Invalid Parameters"}
            data = DB_connection().find_query(par)
            if data == None:
                return {"msg": "Data Not available for the given id"}
            return {"status": "Successful",
                    "Data": data}
        except:
            return {"msg": "Invalid given Arguments",
                    "Valid fields" : "employee_id"}