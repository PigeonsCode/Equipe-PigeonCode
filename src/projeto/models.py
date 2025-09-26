from projeto import database, Login_manager
from flask_login import UserMixin

@Login_manager.user_loader
def load_usuario(id_usuario):
     return Adm_User.query.get(int(id_usuario))


class Adm_User(database.Model,UserMixin):
     id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
     user_db = database.Column(database.String,nullable=False, unique=True)
     password_db = database.Column(database.String,nullable=False,unique=True)


