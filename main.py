from config import app, api, flaskPort
from models import User, Address
from schema import UserAddressSchema, UserSchema, UserListSchema
from users import UserResource
from handlers import not_found_error, internal_error


# API endpoint
api.add_resource(UserResource, '/users')

# main function
if __name__ == '__main__':
    app.run(debug=True, port = int(flaskPort))