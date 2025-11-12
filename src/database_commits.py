import os, dotenv
from projeto import database,app
from projeto.models import Adm_User,Projetos
from projeto import bcrypt
from dotenv import load_dotenv


dotenv.load_dotenv()

senha = os.getenv('SENHA_ADM')

senha_cripto =bcrypt.generate_password_hash(senha)

with app.app_context():
 projeto0=Projetos(nome_projeto="projeto daily falcon") 
 projeto1=Projetos(nome_projeto="Projeto teste 1")
 projeto2 = Projetos(nome_projeto="Projeto teste 2")
 projeto3=Projetos(nome_projeto="projeto daily two-peak") 
 projeto4=Projetos(nome_projeto="Projeto hawk")
 projeto5 = Projetos(nome_projeto="Projeto tes 67")
 
     
 database.session.add(projeto0)
 database.session.add(projeto1)
 database.session.add(projeto2)
 database.session.add(projeto3)
 database.session.add(projeto4)
 database.session.add(projeto5)
   
 database.session.commit()
