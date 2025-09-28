import os, dotenv
import secrets
from projeto import database,app
from projeto.models import Adm_User
from projeto import bcrypt
from dotenv import load_dotenv

dotenv.load_dotenv()

senha = os.getenv('SENHA_ADM')

senha_cripto =bcrypt.generate_password_hash(senha)

with app.app_context():
 user=Adm_User(
 user_db="cliente-adm",
 password_db=senha_cripto
 
)
 database.session.add(user)
 database.session.commit()

#deixar session commit na mesma identação