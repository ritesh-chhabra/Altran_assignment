from config import db

class User(db.Model):
    #User – This table will store the user details like name, email, password, profile picture URL and mobile. Email and mobile must be unique.
    #Address – This table will store the details of address like house/flat  number, Address Line 1, Address Line 2, City, State and Pin code.
    __tablename__ = "user"
    # unqiue constraints for the table (combination of mobile and email)
    __table_args__ = (
        db.UniqueConstraint('mobile', 'email'),
      )
    id = db.Column(db.Integer, primary_key = True) # primary key id
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    profile_pic_url = db.Column(db.String(200))
    mobile = db.Column(db.String(10))
    # adding the relatioship to model for Address class
    address = db.relationship(
        'Address',
        backref = 'user', # used for back reference like one to one map
        cascade='all, delete, delete-orphan'
    )

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    house_num = db.Column(db.String(50))
    address_1 = db.Column(db.String(50))
    address_2 = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
