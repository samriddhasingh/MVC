
from pymongo import MongoClient
import json
from flask import jsonify
from bson import ObjectId
class user_model():
    def __init__(self):
        try:
            self.client=MongoClient('mongodb://localhost:27017')
            self.db=self.client['UserData']
            self.collection=self.db['Authentication']
            print('Connection Sucessful')
        except:
            print('Connection Failed')
    def user_detail(self):
        datalist=[]
        data=self.collection.find()	
        print(data)
        for i in data:
            i['_id']=str(i['_id'])
            datalist.append(i)
            print(i)
        print(datalist)
        result=json.dumps(datalist)
        print(result)
        return result

    def create_user(self,data):
        print(data['email'])
        name=data.get('name')
        age=data.get('age')
        education=data.get('education')
        email=data.get('email')
        final_data={'name':name,'age':age,'education':education,'email':email}
        self.collection.insert_one(final_data)
        return "This is a new user "
