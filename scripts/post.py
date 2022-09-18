from flask import request
from flask_restful import Resource
from scripts.db_connection import DB_connection


class Post(Resource):
    @classmethod
    def post(cls):
        req = request.get_json()
        DB_connection().insert_doc(req)
        return {"status" : "Successful",
                "Data":req}
