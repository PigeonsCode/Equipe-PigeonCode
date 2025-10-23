import os, dotenv
import secrets
from projeto import database,app
from projeto.models import Adm_User, FormsNotas
from projeto import bcrypt



senha = "faatec#_api20252"

senha_cripto =bcrypt.generate_password_hash(senha)

with app.app_context():
 user=Adm_User(
 user_db="cliente-adm",
 password_db=senha_cripto
)
 database.session.add(user)
 database.session.commit()

#deixar session commit na mesma identação