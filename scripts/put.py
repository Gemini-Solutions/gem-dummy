from flask import request
from flask_restful import Resource
from scripts.post import req

class Put(Resource):
    @classmethod
    def put(cls):
        req.update(request.get_json())
        # logging.info("Input Request")
        # logging.info(req)
        print(req)
        return "Updated Successfully"
