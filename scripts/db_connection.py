import bson
import pymongo
from flask import jsonify
from pymongo import MongoClient
from bson import json_util
import json


class DB_connection():
    def get_database(self):
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = f"mongodb+srv://gem_user:gem_user@gemdb.op1lm.mongodb.net/flaskDB?retryWrites=true&w=majority"
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)
        fdb =  client["flaskDB"]
        collection_name = fdb["dummy"]
        print(collection_name)
        return collection_name


    def insert_doc(self,dict):
        cur = self.get_database()
        sample = json.loads(json_util.dumps(dict))
        cur.insert_one(sample)

    def find_query(self,id_s):
        print(id_s)
        cur = self.get_database()
        data = cur.find_one({'employee_id': id_s},{'_id': 0})
        # print(list(data))
        return json.loads(bson.json_util.dumps(data))

    def update_query(self,id_s,exp):
        print(id_s)
        cur = self.get_database()
        prev = {'employee_id': id_s}
        updated = {'$set': {'experience': exp}}
        cur.update_one(prev,updated)
        data = self.find_query(id_s)
        # print(list(data))
        return json.loads(bson.json_util.dumps(data))


    def delete_query(self,id_s):
        print(id_s)
        cur = self.get_database()
        data = self.find_query(id_s)
        rec = {'employee_id': id_s}
        cur.delete_one(rec)
        # print(list(data))
        return json.loads(bson.json_util.dumps(data))