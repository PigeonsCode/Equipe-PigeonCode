from projeto.models import Projetos
from projeto import database
from sqlalchemy.exc import IntegrityError

def calc_media(lista_de_notas):
   total_notas=0
   n_elementos = len(lista_de_notas)
   
   for i in lista_de_notas:
      total_notas+=float(i)

   media = total_notas/n_elementos
   return round(media, 2)

def menor_index(lista_de_notas):
   menor = lista_de_notas[0]
   m_index = 0
   for i in range(len(lista_de_notas)):
      if lista_de_notas[i]<menor: 
         menor = lista_de_notas[i]
         m_index=i

   return m_index



def maior_index(lista_de_notas):
   maior = lista_de_notas[0]
   m_index = 0
   for i in range(len(lista_de_notas)):
      if lista_de_notas[i]>maior:
         maior = lista_de_notas[i]
         m_index = i
   return m_index

def criar_projetos (nome_forms):
    try:
        novo_projeto = Projetos(nome_projeto = nome_forms)
        database.session.add(novo_projeto)
        database.session.commit()   
        return True
       
    except IntegrityError:
        database.session.rollback()
        return False
       
        