from marshmallow import fields, Schema, validate

# defining marshmallow schema for validations and serialization of data
class UserAddressSchema(Schema):
    house_num = fields.String(required=True)
    address_1 = fields.String(required=True)
    address_2 = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    pincode = fields.Integer(required=True)

class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    profile_pic_url = fields.URL(required=True)
    mobile = fields.String(validate=validate.Length(min=10,max=14), required=True)
    address = fields.Nested(UserAddressSchema, required=True) # nesting the address object

class UserListSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    profile_pic_url = fields.URL(required=True)
    mobile = fields.String(required=True)
    address = fields.Nested(UserAddressSchema, required=True, many = True)
