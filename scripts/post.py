from flask import request
from flask_restful import Resource

req = {}
class Post(Resource):
    @classmethod
    def post(cls):
        req.update(request.get_json())
        # logging.info("Input Request")
        # logging.info(req)
        print(req)
        return "Successful"
