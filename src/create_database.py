import os, dotenv
from projeto import bcrypt
from projeto import database, app
from projeto.models import Adm_User, FormsNotas, Projetos


with app.app_context():
    database.drop_all()
    database.create_all()
    dotenv.load_dotenv()

    senha = os.getenv('SENHA_ADM')

    senha_cripto =bcrypt.generate_password_hash(senha)

    user=Adm_User(
    user_db="cliente-adm",
    password_db=senha_cripto
    )
    

    database.session.add(user)
    database.session.commit()
 