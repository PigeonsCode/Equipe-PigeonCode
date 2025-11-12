import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #importação do banco de dados
from flask_login import LoginManager
from flask import url_for, request
from flask_bcrypt import Bcrypt
from projeto.navigation import navigation_items

app=Flask(__name__)

app.config["SECRET_KEY"] = "ba7783e47efacd4b8c6b40475222bbac"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view="loginADM"

#filters
def kebab_case(value):
    if not value:
        return ''
    camelCaseString = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', value)
    kebabCaseString = re.sub('([a-z0-9])([A-Z])', r'\1-\2', camelCaseString)
    return kebabCaseString.lower()

app.jinja_env.filters['kebabify'] = kebab_case


#variaveis passadas em todas as rotas
def is_nav_open(nav_item, request_path):
    for sub in nav_item['subtopic']:
        if 'endpoint' in sub and request_path == url_for(sub['endpoint']):
            return True
    return False

def show_aside(nav_item, request_path):
    for sub in nav_item['subtopic']:
        if 'endpoint' in sub and request_path == url_for(sub['endpoint']):
            if sub.get('sub_navigation') is None:
                return False
            else:
                return True
    return False


@app.context_processor
def inject_global():
    projects = Projetos.query.order_by(Projetos.id).all()
    projects_list = []
    nav_copy = []
    for nav in navigation_items:
        nav_copy.append({**nav, 'nav_open': is_nav_open(nav, request.path), 'show_aside': show_aside(nav, request.path)})
    
    for p in projects:
        projects_list.append({
            'id': p.id,
            'nome': p.nome_projeto
         })
        
    return dict(navigation=nav_copy, projetos=projects_list)

# Funções para gerar dados nos gráficos
def process_notas_pie(respostas_form):
    #a estrutura é definida desse jeito, porque precisamos saber quantos itens estão dentro da sessão verde (qualidade alta), quantos na sessão amarela (qualidade média) e quantos na sessão vermelha (qualidade baixa) e ainda, quais que são esses itens 
    #com termos mais técnicos, essa variável que define exatamente como será o dicionário que vai ser retornado no final
    dados_processados = {
        'contagens': {'verde': 0, 'amarelo': 0, 'vermelho': 0},
        'sessoes': {'verde': [], 'amarelo': [], 'vermelho': []}
    }

    #essas duas são variáveis auxiliares para guardar informações
    #lista que vai conter o nome das colunas que são numéricas e armazenam médias (logo ela vai excluir o projeto_id, melhores e piores notas)  
    atributos_media = []
    #um dicionário que armazenará todas as médias dos formulários enviados dividas em suas respectivas sessões
    notas_por_coluna = {}


    nomes_de_atributos = dir(respostas_form[0]) #esse comando dir retorna uma lista de strings com todos os nomes de colunas do objeto
    for nome_coluna in nomes_de_atributos:
        if nome_coluna.startswith('m_'):
            valor_coluna = getattr(respostas_form[0], nome_coluna) #converte a string na coluna com nome_coluna para checar o tipo de seu valor
            if isinstance(valor_coluna, (int,float)): #checa se o valor da coluna é um int ou float mesmo
                atributos_media.append(nome_coluna) #adiciona o nome da coluna a lista que contém as colunas válidas de médias
                notas_por_coluna[nome_coluna] = [] #cria uma lista vazia dentro do dicionário para cada uma das colunas de média válidas
    

    for resposta in respostas_form: #percorre por todos os formulários cadastrados do projeto que estamos analisando
        for nome_coluna in atributos_media: #percorre nossa lista com os nomes de coluna
            nota = getattr(resposta, nome_coluna) #pega qual o valor armazenado na coluna especificada do objeto de resposta
            if nota is not None:
                notas_por_coluna[nome_coluna].append(float(nota)) #se a nota não for vazia, preenche cada item do dicionário com a nota da coluna do objeto resposta equivalente


    for nome_coluna, lista_notas in notas_por_coluna.items(): #percorre o dicionário de notas_por_coluna (percorre o nome da coluna e a sua respectiva lista de notas)
        if not lista_notas:
            continue #se a sessão não tiver notas válidas, ele pula p próxima
        media_sessao = sum(lista_notas) / len(lista_notas) #calcula a média de todas as notas enviadas para aquela sessão
        #classifica a média da sessão em uma das três faixas
        if media_sessao > 3.0:
            faixa = 'verde'
        elif media_sessao > 2.0 and media_sessao <= 3.0:
            faixa = 'amarelo'
        else: 
            faixa = 'vermelho'

        dados_processados['contagens'][faixa] += 1 
        #aqui acessamos a chave contagens do dicionário de dados_processadors, após isso acessamos algum dos itens dentro do dicionário de contagens (faixa depende do valor definido pela média da sessão) e aumentamos um no contador
        dados_processados['sessoes'][faixa].append(nome_coluna)
        #aqui acessamos a chave sessões do dicionário de dados_processados, após isso fazemos a mesma coisa do que no item anterior, mas dessa vez ao invés de aumentar um contador, adicionamos a coluna a qual média se refere na lista

    return dados_processados
    



from projeto import routes, models
from projeto.models import Projetos 

