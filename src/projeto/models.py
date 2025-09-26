from projeto import database
from flask_login import UserMixin

class Adm_User(database.Model,UserMixin):
     id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
     user_db = database.Column(database.String,nullable=False, unique=True)
     password_db = database.Column(database.String,nullable=False,unique=True)


