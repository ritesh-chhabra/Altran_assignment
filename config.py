from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# some input variables
dbName = "altran"
flaskPort = 50000


app = Flask(__name__) # Construct Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/' + dbName # Mysql config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # Suppressing some warnings
db = SQLAlchemy(app) # Construct SQLAlchemy object
api = Api(app) # Contruct API object