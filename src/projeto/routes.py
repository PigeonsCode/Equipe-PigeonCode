import bcrypt
from projeto import database, app, bcrypt, login_manager
from projeto import database,app,bcrypt
from projeto.models import Adm_User
from flask import render_template,url_for,redirect,flash
from flask_login import login_required,login_user,logout_user,current_user
from projeto.navigation import navigation_items
from projeto.forms import FormLoginAdm, FormUserAvalia,FormDelProjeto,FormCriaProjeto
from projeto.models import Adm_User,FormsNotas, Projetos 
from projeto.function import calc_media,calc_soma,menor_index,maior_index,criar_projetos,del_projetos,process_notas_pie,media_questionarios,pont_refinada, maior_menor_nota, gerar_tabela_por_projeto, gerar_dados_graficos_por_projeto

@app.route("/")
def homepage():

    return render_template("index.html", navigation=navigation_items, page_url="homepage")

@app.route("/triagem-adm")
def teste_adm():
    if current_user.is_authenticated:
        return redirect(url_for("area_restrita"))
    else:
        return redirect(url_for("loginADM"))
    

@app.route("/login-adm", methods = ["GET", "POST"])
def loginADM():
    form_login_adm = FormLoginAdm()
    if form_login_adm.validate_on_submit():
         user_login_attempt = Adm_User.query.filter_by(user_db = form_login_adm.username_adm.data).first()
         if  user_login_attempt and bcrypt.check_password_hash(user_login_attempt.password_db , form_login_adm.password_adm.data) :
            login_user(user_login_attempt,remember=False)
            return redirect (url_for("area_restrita")) 
         else:
             flash("Usuário ou senha incorretos!")
             redirect (url_for("loginADM"))
    return render_template("login-adm.html", form = form_login_adm)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/relatorio/<int:id_relatorio>", methods = ["GET","POST"])
@login_required
def relatorio(id_relatorio):
    formdelprojeto = FormDelProjeto()
    form_cria_projeto = FormCriaProjeto()
    respostas_form = FormsNotas.query.filter_by(projeto_id=id_relatorio).all()
    projeto = Projetos.query.get(id_relatorio)
    tabela = gerar_tabela_por_projeto(id_relatorio)
    grafico = gerar_dados_graficos_por_projeto(id_relatorio)
    
    
    media_projeto = media_questionarios(id_relatorio)
    qualidade = ""
    pont_final = f'{pont_refinada(media_projeto):.0f}'
    maior_med = maior_menor_nota(id_relatorio)
    maior_resultado = maior_med['maior_pontuacao']
    menor_med = maior_menor_nota(id_relatorio)
    menor_resultado = menor_med['menor_pontuacao']
    if media_projeto < 76:
        qualidade = "Baixa"
    elif 76 <= media_projeto <= 114:
        qualidade = "Média"
    else:
        qualidade = "Alta"
        
    if formdelprojeto.validate_on_submit() and formdelprojeto.project_del_confirm.data=="CONFIRMAR":
       
        del_projetos(id_relatorio)
        return redirect(url_for("area_restrita"))
        
    elif  formdelprojeto.validate_on_submit() and formdelprojeto.project_del_confirm.data !="Confirmar":
         flash("digite CONFIRMAR")
         return redirect(url_for("area_restrita"))
    

    if form_cria_projeto.validate_on_submit():

        if criar_projetos(form_cria_projeto.project_name.data):
            return redirect(url_for("area_restrita"))
        else: 
            flash("Já existe um projeto com este nome!")
            return redirect(url_for("area_restrita"))
    

    if respostas_form:
        dados_pie = process_notas_pie(respostas_form)

    else:
        dados_pie = {'contagens': {'verde': 0, 'amarelo': 0, 'vermelho': 0},
        'sessoes': {'verde': [], 'amarelo': [], 'vermelho': []}}
          
    return render_template("relatorio.jinja2", relatorio=id_relatorio, projeto = projeto, 
                           form_info = respostas_form, form_del=formdelprojeto, dados_pie = dados_pie, form_cria_projeto = form_cria_projeto, qualidade = qualidade, media_projeto = media_projeto, pont_final= pont_final, maior_resultado= maior_resultado, menor_resultado= menor_resultado, dados_bar = grafico, dados_table = tabela)


@app.route("/formulario-avaliativo", methods = ["GET","POST"])
def forms():
    
    form_avaliacao = FormUserAvalia()

    projects = Projetos.query.order_by(Projetos.id).all()
    projects_list = [(p.id, p.nome_projeto) for p in projects]
    form_avaliacao.select_projeto.choices = projects_list

    if form_avaliacao.validate_on_submit():
        incremento_r1 = form_avaliacao.incremento_do_produto_p1.data
        incremento_r2 = form_avaliacao.incremento_do_produto_p2.data
        incremento_r3 = form_avaliacao.incremento_do_produto_p3.data
        incremento_r4 = form_avaliacao.incremento_do_produto_p4.data

        lista_incremento_do_produto = [ incremento_r1, incremento_r2, incremento_r3, incremento_r4]
        media_incremento_do_produto = calc_media(lista_incremento_do_produto)
        soma_incremento_do_produto = calc_soma(lista_incremento_do_produto)

        daily_p1 = form_avaliacao.daily_scrum_p1.data
        daily_p2 = form_avaliacao.daily_scrum_p2.data

        lista_daily_scrum = [daily_p1,daily_p2]
        media_daily_scrum = calc_media(lista_daily_scrum)
        soma_daily_scrum = calc_soma(lista_daily_scrum)      

        sprint_retro_r1 = form_avaliacao.sprint_retrospective_p1.data
        sprint_retro_r2 = form_avaliacao.sprint_retrospective_p2.data
        sprint_retro_r3 = form_avaliacao.sprint_retrospective_p3.data
        sprint_retro_r4 = form_avaliacao.sprint_retrospective_p4.data

        lista_sprint_retro=[sprint_retro_r1,sprint_retro_r2,sprint_retro_r3,sprint_retro_r4]
        media_sprint_retro = calc_media(lista_sprint_retro)
        soma_sprint_retro = calc_soma(lista_sprint_retro)
       

        burnu_r1 = form_avaliacao.burnup_p1.data

        sprint_back_r1 = form_avaliacao.sprint_backlog_p1.data
        sprint_back_r2 = form_avaliacao.sprint_backlog_p2.data
        sprint_back_r3 = form_avaliacao.sprint_backlog_p3.data
        sprint_back_r4 = form_avaliacao.sprint_backlog_p4.data

        lista_sprint_back = [sprint_back_r1,sprint_back_r2,sprint_back_r3,sprint_back_r4]
        media_sprint_back = calc_media(lista_sprint_back)
        soma_sprint_back = calc_soma(lista_sprint_back)
        

        dod_r1 = form_avaliacao.dod_p1.data
        dod_r2 = form_avaliacao.dod_p2.data
        dod_r3 = form_avaliacao.dod_p3.data
        
        lista_dod = [dod_r1,dod_r2,dod_r3]
        media_dod = calc_media(lista_dod)
        soma_dod = calc_soma(lista_dod)
       

        sprint_rev_r1 = form_avaliacao.sprint_review_p1.data
        sprint_rev_r2 = form_avaliacao.sprint_review_p2.data
        sprint_rev_r3 = form_avaliacao.sprint_review_p3.data
        sprint_rev_r4 = form_avaliacao.sprint_review_p4.data

        lista_sprint_rev = [sprint_rev_r1,sprint_rev_r2,sprint_rev_r3,sprint_rev_r4]
        media_sprint_rev = calc_media(lista_sprint_rev)
        soma_sprint_rev = calc_soma(lista_sprint_rev)
        

        burndown_r1 = form_avaliacao.burndown_p1.data
        burndown_r2 = form_avaliacao.burndown_p2.data

        lista_burndown = [burndown_r1,burndown_r2]
        media_burndown = calc_media(lista_burndown)
        soma_burndown = calc_soma(lista_burndown)
        

        product_backlog_r1 = form_avaliacao.product_backlog_p1.data
        product_backlog_r2 = form_avaliacao.product_backlog_p2.data
        product_backlog_r3 = form_avaliacao.product_backlog_p3.data
        product_backlog_r4 = form_avaliacao.product_backlog_p4.data

        lista_backlog = [product_backlog_r1,product_backlog_r2,product_backlog_r3,product_backlog_r4]
        media_backlog = calc_media(lista_backlog)
        soma_backlog = calc_soma(lista_backlog)
        

        dor_r1 = form_avaliacao.dor_p1.data
        dor_r2 = form_avaliacao.dor_p2.data 
        dor_r3 = form_avaliacao.dor_p3.data

        lista_dor = [dor_r1,dor_r2,dor_r3]
        media_dor = calc_media(lista_dor)
        soma_dor = calc_soma(lista_dor)
      

        sprint_planning_r1 = form_avaliacao.sprint_planning_p1.data
        sprint_planning_r2 = form_avaliacao.sprint_planning_p2.data 
        sprint_planning_r3 = form_avaliacao.sprint_planning_p3.data
        sprint_planning_r4 = form_avaliacao.sprint_planning_p4.data
        sprint_planning_r5 = form_avaliacao.sprint_planning_p5.data

        lista_sprint_planning = [sprint_planning_r1,sprint_planning_r2,sprint_planning_r3,sprint_planning_r4,sprint_planning_r5]
        media_sprint_planning = calc_media(lista_sprint_planning)
        soma_sprint_planning = calc_soma(lista_sprint_planning)
       

        story_point_r1 = form_avaliacao.story_point_p1.data
        story_point_r2 = form_avaliacao.story_point_p2.data

        lista_story_point = [story_point_r1,story_point_r2]
        media_story_point = calc_media(lista_story_point)
        soma_story_point = calc_soma(lista_story_point)


        lista_de_sessoes =['m_inpr','m_dasc','m_spretro',
        'm_buup','m_spba','m_dod','m_spre','m_budo','m_prba','m_dor','m_sppl','m_stpo']

        lista_notas = [media_incremento_do_produto,media_daily_scrum,media_sprint_retro,burnu_r1
        ,media_sprint_back,media_dod,media_sprint_rev,media_burndown,media_backlog,media_dor,
        media_sprint_planning,media_story_point]

        lista_notas2 = [soma_incremento_do_produto,soma_daily_scrum,soma_sprint_retro,burnu_r1
        ,soma_sprint_back,soma_dod,soma_sprint_rev,soma_burndown,soma_backlog,soma_dor,
        soma_sprint_planning,soma_story_point]

        media_lista = calc_soma(lista_notas2)
        
        menor_pos= menor_index(lista_notas)
        menor = lista_de_sessoes[menor_pos]

        maior_pos = maior_index(lista_notas)
        maior = lista_de_sessoes[maior_pos]
        


        formulario = FormsNotas (projeto_id = form_avaliacao.select_projeto.data , media_lista=media_lista, pior_nota_sessao=menor, 
                                 melhor_nota_sessao=maior, m_inpr= media_incremento_do_produto,
                                 m_dasc=media_daily_scrum,m_spretro=media_sprint_retro,
                                 m_buup=burnu_r1,m_spba=media_sprint_back,m_dod=media_dod,
                                 m_spre=media_sprint_rev,m_budo=media_burndown,
                                 m_prba=media_backlog,m_dor =media_dor,m_sppl=media_sprint_planning,
                                 m_stpo = media_story_point)
        database.session.add(formulario)
        database.session.commit()
        
        flash("Formulário enviado com sucesso!", "success")
        return redirect (url_for("forms"))

    if form_avaliacao.errors:
        flash("Você deve preencher todos os campos do formulário!", "danger")

    return render_template("forms.html", page_url="formulario-avaliativo", form = form_avaliacao)
 
# Páginas de conteúdo
@app.route("/area-restrita",methods = ["GET","POST"])
@login_required
def area_restrita():
    form_cria_projeto = FormCriaProjeto()

    if form_cria_projeto.validate_on_submit(): 
        if criar_projetos(form_cria_projeto.project_name.data):
            return redirect(url_for("area_restrita"))
        else: 
            return redirect(url_for("area_restrita"))
            flash("Já existe um projeto com este nome!")

    return render_template("/area-restrita.html",form_cria_projeto = form_cria_projeto)

@app.route("/scrum")
def scrum():
    return render_template("/paginas-treinamento/scrum.html", page_url="scrum", first_item = True)
 
@app.route("/manifesto-agil")
def manifestoAgil():
    return render_template("/paginas-treinamento/manifesto.html", page_url="manifestoAgil",  first_item = True)
 
@app.route("/principios-ageis")
def principiosAgeis():
    return render_template("/paginas-treinamento/principios.html", page_url="principiosAgeis",  first_item = True)
 
@app.route("/valores")
def valores():
    return render_template("/paginas-treinamento/valores.html", page_url="valores")
 
@app.route("/papeis")
def papeis():
    return render_template("/paginas-treinamento/papeis.html", page_url="papeis")
 
@app.route("/sprints")
def sprints():
    return render_template("/paginas-treinamento/sprints.html", page_url="sprints")
 
@app.route("/sprint-planning")
def sprintPlanning():
    return render_template("/paginas-treinamento/sprint-planning.html", page_url="sprintPlanning")
 
@app.route("/dailly-scrum")
def daillyScrum():
    return render_template("/paginas-treinamento/daily-scrum.html", page_url="daillyScrum")
 
@app.route("/sprint-review")
def sprintReview():
    return render_template("/paginas-treinamento/sprint-review.html", page_url="sprintPlanning")
 
@app.route("/sprint-restrospective")
def sprintRestrospective():
    return render_template("/paginas-treinamento/sprint-restrospective.html", page_url="sprintPlanning")
 
@app.route("/product-backlog")
def productBacklog():
    return render_template("/paginas-treinamento/product-backlog.html", page_url="productBacklog")
 
@app.route("/sprint-backlog")
def sprintBacklog():
    return render_template("/paginas-treinamento/sprint-backlog.html", page_url="sprintBacklog")
 
@app.route("/incremento-produto")
def incrementoProduto():
    return render_template("/paginas-treinamento/incremento.html", page_url="incrementoProduto")
 
@app.route("/definition-of-ready")
def definitionOfReady():
    return render_template("/paginas-treinamento/dor.html", page_url="definitionOfReady")
 
@app.route("/definition-of-done")
def definitionOfDone():
    return render_template("/paginas-treinamento/dod.html", page_url="definitionOfDone")
 
@app.route("/story-point")
def storyPoint():
    return render_template("/paginas-treinamento/story-point.html", page_url="storyPoint")
 
@app.route("/burn-down-chart")
def burnDownChart():
    return render_template("/paginas-treinamento/burndown.html", page_url="burnDownChart")

@app.route("/burn-up-chart")
def burnUpChart():
    return render_template("/paginas-treinamento/burnup.html", page_url="burnUpChart")

