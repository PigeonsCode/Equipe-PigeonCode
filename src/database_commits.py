import os, dotenv
import secrets
from projeto import database,app
from projeto.models import Adm_User, FormsNotas,Projetos
from projeto import bcrypt
senha= "faatec_#20252"
senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
print(senha_hash)
with app.app_context():
 credenciais_adm = Adm_User(user_db='cliente-adm',
 password_db=senha_hash)
 
 projetoteste=Projetos(
 nome_projeto = "Projeto padrão de teste"
)
 database.session.add(projetoteste) 
 database.session.add(credenciais_adm)
 database.session.commit()

#deixar session commit na mesma identação