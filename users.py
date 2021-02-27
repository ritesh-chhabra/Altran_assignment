from models import User, Address
from schema import UserAddressSchema, UserSchema, UserListSchema
from flask import request
from config import db
from flask_restful import Resource
from sqlalchemy import exc
import hashlib

# flask_restful class for handling GET and POST requests
class UserResource(Resource):
    def get(self):
        users = User.query.all() # get all the records of User Model
        users_schema = UserListSchema(many=True) # Marshmellow schema for list of users
        data = users_schema.dump(users) #dumping the data in User model format
        return {"data": data}

    def post(self):
        users_schema = UserSchema() # Marshmellow schema for validating data
        form_data = request.get_json() # get the data from body
        errors = users_schema.validate(form_data) # return list of validation errors
        if errors:
            print(errors)
            return {
                       "message": errors
                   }, 500
        # preparing data for User Model
        h = hashlib.md5(request.json["password"].encode())
        new_user = User(
            name = request.json["name"],
            email = request.json["email"],
            password = h.hexdigest(),
            profile_pic_url = request.json["profile_pic_url"],
            mobile = request.json["mobile"]
        )
        # preparing data for Address Model
        new_address = Address(
            house_num = request.json["address"]["house_num"], 
            address_1 = request.json["address"]["address_1"], 
            address_2 = request.json["address"]["address_2"], 
            city = request.json["address"]["city"], 
            state = request.json["address"]["state"], 
            pincode = request.json["address"]["pincode"]
        )
        new_user.address.append(new_address) # Adding address object to User object
        try:
            db.session.add(new_user) # Issue the insert statement
            db.session.commit() # Commit the changes to disk 
            return {"message": "User created"}, 201
        except exc.IntegrityError as e:
            db.session.rollback() # Roll back the transaction in case of error
            errorInfo = e.orig.args # get the data from error object
            return {"message": errorInfo[1]}, 200

