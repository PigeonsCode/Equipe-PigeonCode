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
    #a estrutura é definida desse jeito, porque precisamos saber quantos itens estão dentro da sessão verde (qualidade alta), quantos na sessão amarela (qualidade média) e quantos na sessão vermelha (qualidade baixa) e ainda, quais que são esses itens 
    #com termos mais técnicos, essa variável que define exatamente como será o dicionário que vai ser retornado no final
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
                nome_coluna_traduzida = regras_traducao[nome_coluna]
                notas_por_coluna[nome_coluna_traduzida] = [] #cria uma lista vazia dentro do dicionário para cada uma das colunas de média válidas

    

    for resposta in respostas_form: #percorre por todos os formulários cadastrados do projeto que estamos analisando
        for nome_coluna in atributos_media: #percorre nossa lista com os nomes de coluna
            nota = getattr(resposta, nome_coluna) #pega qual o valor armazenado na coluna especificada do objeto de resposta
            if nota is not None:
                nome_coluna_traduzida = regras_traducao[nome_coluna]
                notas_por_coluna[nome_coluna_traduzida].append(float(nota)) #se a nota não for vazia, preenche cada item do dicionário com a nota da coluna do objeto resposta equivalente


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

        tabela.append({
            "nota_final": round(media_geral, 2),
            "qualidade_processos": "Alta" if media_geral >= 3 else "Média",
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
    #essa função vai ta entupida de anotações porque estou PERDENDO A CABEÇA e quero QUE FUNCIONE AGORA EM UMA SÓ FUNÇÃO
    
    formularios = FormsNotas.query.filter_by(projeto_id=id_projeto).all()  
    #FormsNotas.query = "Vá na tabela FormsNotas do banco de dados"
    #filter_by(projeto_id=id_projeto) = "Filtre apenas os que têm este projeto_id"
    #.all() = "Pegue TODOS os resultados"
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
    #lista com os nomes pra depois mostrar bonitinho

    notas_por_categoria = {}
    #dicionario vazio pra poder por as notas

    for atributo in regras_traducao.keys():
        # cada nome no dicionario... (.KEYS PARA PEGAR APENAS OS NOMES!)
        notas_por_categoria[regras_traducao[atributo]] = []
        # coloca o nome bonitinho por categoria em uma lista vazia

    # Coleta todas as notas de cada formulário
    for formulario in formularios:
        # cada formulário dentro de formularios(ou no caso, o projeto)...
        for atributo, categoria in regras_traducao.items():
            # para cada par de nome (.ITEMS PEGA O NOME E O QUE FAZ! NO CASO PEGA O SEGUNDO NOME)
            nota = getattr(formulario, atributo)
            #  pega o valor da coluna respectiva
            if nota is not None:
                # se a nota não estiver vazia (se nao tiver nada dentro dela, ela vai fazer essa proxima linha)
                notas_por_categoria[categoria].append(float(nota))
                # passa a nota dos nome base para os nome bonitinho

    # Calcula as médias e encontra maior/menor
    medias = {}
    maior_media = {'categoria': None, 'valor': 0}
    menor_media = {'categoria': None, 'valor': 152}

    for categoria, notas in notas_por_categoria.items():
        if notas:  # Só calcula se houver notas
            media = sum(notas) / len(notas)
            medias[categoria] = media
            
            # Verifica se é a maior média
            if media > maior_media['valor']:
                maior_media = {'categoria': categoria, 'valor': media}
            
            # Verifica se é a menor média
            if media < menor_media['valor']:
                menor_media = {'categoria': categoria, 'valor': media}
    # Inicializa as listas de notas para cada categoria


    return {
        'medias': medias,
        'maior_pontuacao': maior_media['categoria'],
        'menor_pontuacao': menor_media['categoria']}

#def proc_maior_nota(id_projeto):

