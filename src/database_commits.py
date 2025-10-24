import os, dotenv
import secrets
from projeto import database,app
from projeto.models import Adm_User, FormsNotas,Projetos
from projeto import bcrypt


with app.app_context():
 projetoteste=Projetos(
 nome_projeto = "Projeto padrão de teste"
)
 database.session.add(projetoteste)
 database.session.commit()

#deixar session commit na mesma identação