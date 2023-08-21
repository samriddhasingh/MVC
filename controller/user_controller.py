from app import app
from flask import request
from model.user_model import user_model
obj=user_model()

@app.route('/user/signup')
def user_signup_controller():  
    return obj.user_detail()

@app.route('/user/add',methods=['POST'])
def user_add():
    return obj.create_user(request.form)