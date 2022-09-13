# from flask import request
from flask_restful import Resource
from scripts.post import req

class Get(Resource):
    @classmethod
    def get(cls):
        # logging.info("Input Request")
        # logging.info(req)
        print(req)
        return req
