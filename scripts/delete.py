# from flask import request
from flask_restful import Resource
from scripts.post import req

class Delete(Resource):
    @classmethod
    def delete(cls):
        req.clear()
        # logging.info("Input Request")
        # logging.info(req)
        print(req)
        return "Successful"
