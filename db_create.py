
from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

#creation of the database
db.create_all()


