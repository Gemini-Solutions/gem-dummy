from flask import Flask
from flask_restful import Api
from scripts.post import Post
from scripts.put import Put
from scripts.get import Get
from scripts.delete import Delete

server = Flask(__name__)
api = Api(server)
api.add_resource(Post,"/test/v1/post")
api.add_resource(Put,"/test/v1/put")
api.add_resource(Get,"/test/v1/get")
api.add_resource(Delete,"/test/v1/delete")