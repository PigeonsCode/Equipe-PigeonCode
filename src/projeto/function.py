from projeto.models import Projetos, FormsNotas
from projeto import database
from sqlalchemy.exc import IntegrityError
import os
from projeto import app

def calc_media(lista_de_notas):
   total_notas=0
   n_elementos = len(lista_de_notas)
   
   for i in lista_de_notas:
      total_notas+=int(i)

   media = total_notas/n_elementos
   return round(media, 2)

def calc_soma(lista_de_notas):
   total_notas=0
   
   for i in lista_de_notas:
      total_notas+=int(i)

   media = total_notas
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

def del_projetos(id_relatorio):
        id_relatorio = int(id_relatorio)      
        FormsNotas.query.filter_by(projeto_id=id_relatorio).delete()
        Projetos.query.filter_by(id=id_relatorio).delete()
        database.session.commit()


# Funções para gerar dados nos gráficos
def process_notas_pie(respostas_form):
    dados_processados = {
        'contagens': {'verde': 0, 'amarelo': 0, 'vermelho': 0},
        'sessoes': {'verde': [], 'amarelo': [], 'vermelho': []}
    }

    regras_traducao = {
        'm_inpr': 'Incremento do Produto',
        'm_dasc': 'Daily Scrum',
        'm_spretro': 'Sprint Retrospective',
        'm_buup':  'Burnup Chart',
        'm_spba': 'Sprint Backlog',
        'm_dod': 'Definition of Done',
        'm_spre': 'Sprint Review',
        'm_budo': 'Burndown Chart',
        'm_prba': 'Product Backlog',
        'm_dor': 'Definition of Ready',
        'm_sppl': 'Sprint Planning',
        'm_stpo': 'Story Points'
    }

    atributos_media = []
    notas_por_coluna = {}


    nomes_de_atributos = dir(respostas_form[0]) 
    for nome_coluna in nomes_de_atributos:
        if nome_coluna.startswith('m_'):
            valor_coluna = getattr(respostas_form[0], nome_coluna) 
            if isinstance(valor_coluna, (int,float)):
                atributos_media.append(nome_coluna) 
                nome_coluna_traduzida = regras_traducao[nome_coluna]
                notas_por_coluna[nome_coluna_traduzida] = [] 

    for resposta in respostas_form:
        for nome_coluna in atributos_media:
            nota = getattr(resposta, nome_coluna) 
            if nota is not None:
                nome_coluna_traduzida = regras_traducao[nome_coluna]
                notas_por_coluna[nome_coluna_traduzida].append(float(nota)) 

    for nome_coluna, lista_notas in notas_por_coluna.items(): 
        if not lista_notas:
            continue 
        media_sessao = sum(lista_notas) / len(lista_notas) 
        if media_sessao > 3.0:
            faixa = 'verde'
        elif media_sessao > 2.0 and media_sessao <= 3.0:
            faixa = 'amarelo'
        else: 
            faixa = 'vermelho'

        dados_processados['contagens'][faixa] += 1 
        dados_processados['sessoes'][faixa].append(nome_coluna)
    return dados_processados


DB_PATH = os.path.join(app.instance_path, "banco.db")

sessoes = [
        "Incremento do Produto",
        "Daily Scrum",
        "Sprint Retrospective",
        "Burndown Chart",
        "Burnup Chart",
        "Sprint Backlog",
        "Product Backlog",
        "Definition of Ready",
        "Definition of Done",
        "Sprint Planning",
        "Sprint Review",
        "Story Point"
    ]

mapeamento = {
        "Incremento do Produto": "m_inpr",
        "Daily Scrum": "m_dasc",
        "Sprint Retrospective": "m_spretro",
        "Burndown Chart": "m_budo",
        "Burnup Chart": "m_buup",
        "Sprint Backlog": "m_spba",
        "Product Backlog": "m_prba",
        "Definition of Ready": "m_dor",
        "Definition of Done": "m_dod",
        "Sprint Planning": "m_sppl",
        "Sprint Review": "m_spre",
        "Story Point": "m_stpo"
    }
mapeamento_invertido = {v: k for k, v in mapeamento.items()}

  
def gerar_dados_graficos_por_projeto(id_relatorio):


    forms = FormsNotas.query.filter_by(projeto_id=id_relatorio).all()

    notas = {sessao: [] for sessao in sessoes}

    for form in forms:
        for sessao in sessoes:
            coluna = mapeamento[sessao]
            valor = getattr(form, coluna, None)
            if valor is not None:
                notas[sessao].append(valor)

    medias = {}
    for sessao, valores in notas.items():
        medias[sessao] = sum(valores) / len(valores) if valores else 0

    return medias

def gerar_tabela_por_projeto(id_relatorio):

    rows = FormsNotas.query.filter_by(projeto_id=id_relatorio).all()

    tabela = []

    for r in rows:
        media_geral = sum([
            r.m_inpr, r.m_dasc, r.m_spretro, r.m_buup, r.m_spba,
            r.m_dod, r.m_spre, r.m_budo, r.m_prba, r.m_dor,
            r.m_sppl, r.m_stpo
        ]) / 12

        media = pont_refinada(float(r.media_lista))
        qualidade = ''
        if float(r.media_lista) < 85:
            qualidade = "Baixa"
        elif 85 <= float(r.media_lista) <= 114:
            qualidade = "Média"
        else:
            qualidade = "Alta"

        tabela.append({
            "nota_final": f'{media:.0f}',
            "qualidade_processos": qualidade,
            "melhor": mapeamento_invertido.get(r.melhor_nota_sessao, "—"),
            "pior": mapeamento_invertido.get(r.pior_nota_sessao, "—"),
        })

    return tabela

def media_questionarios(id_projeto):
    formularios = FormsNotas.query.filter_by(projeto_id= id_projeto).all()
    soma,cont =0,0

    for i in formularios:
        soma += float(i.media_lista)
        cont+=1
    if formularios:
        media_geral = soma/cont
    else:
        media_geral = 0
    return media_geral

def pont_refinada(media_geral):
    M = media_geral
    M =((M - 38)/(152 - 38))*100
    return M

def maior_menor_nota(id_projeto):
    
    formularios = FormsNotas.query.filter_by(projeto_id=id_projeto).all()  
   
    regras_traducao = {
        'm_inpr': 'Incremento do Produto',
        'm_dasc': 'Daily Scrum',
        'm_spretro': 'Sprint Retrospective',
        'm_buup':  'Burnup Chart',
        'm_spba': 'Sprint Backlog',
        'm_dod': 'Definition of Done',
        'm_spre': 'Sprint Review',
        'm_budo': 'Burndown Chart',
        'm_prba': 'Product Backlog',
        'm_dor': 'Definition of Ready',
        'm_sppl': 'Sprint Planning',
        'm_stpo': 'Story Points'}

    notas_por_categoria = {}

    for atributo in regras_traducao.keys():
        notas_por_categoria[regras_traducao[atributo]] = []

    for formulario in formularios:
        for atributo, categoria in regras_traducao.items():
            nota = getattr(formulario, atributo)
            if nota is not None:
                notas_por_categoria[categoria].append(float(nota))

    medias = {}
    maior_media = {'categoria': None, 'valor': 0}
    menor_media = {'categoria': None, 'valor': 152}

    for categoria, notas in notas_por_categoria.items():
        if notas: 
            media = sum(notas) / len(notas)
            medias[categoria] = media
            
            if media > maior_media['valor']:
                maior_media = {'categoria': categoria, 'valor': media}
            
            if media < menor_media['valor']:
                menor_media = {'categoria': categoria, 'valor': media}


    return {
        'medias': medias,
        'maior_pontuacao': maior_media['categoria'],
        'menor_pontuacao': menor_media['categoria']}


