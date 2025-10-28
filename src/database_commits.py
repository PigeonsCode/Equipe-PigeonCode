import os, dotenv
from projeto import database,app
from projeto.models import Adm_User,Projetos
from projeto import bcrypt


with app.app_context():

 projetoteste=Projetos(
 nome_projeto = "Projeto Daily Sync"
)
 database.session.add(projetoteste) 
 database.session.commit()

#deixar session commit na mesma identação