from config import app
from models import db

from sqlalchemy_utils.functions import database_exists, create_database, drop_database

dbUri = app.config["SQLALCHEMY_DATABASE_URI"]

if database_exists(dbUri):
    drop_database(dbUri)
    print("DROP database - SUCCESS")

create_database(dbUri)
print("CREATE database - SUCCESS")

db.create_all()
print("CREATE Tables - SUCCESS")
