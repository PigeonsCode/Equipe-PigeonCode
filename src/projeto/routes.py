import bcrypt
from projeto import database,app,bcrypt, login_manager
from projeto.models import Adm_User
from flask import Flask,render_template,url_for,redirect,flash,request
from flask_login import login_required,login_user,logout_user,current_user
from projeto.navigation import navigation_items
from projeto import app
from projeto.forms import FormLoginAdm, FormUserAvalia
from projeto.models import Adm_User,FormsNotas
from projeto.function import calc_media,menor_index,maior_index

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
            return redirect (url_for("area_restrita")) #criar pagina de acesso restrito com o nome AcessoADM, usar @login_required
         else:
             flash("Usuário ou senha incorretos!")
             redirect (url_for("loginADM"))
    return render_template("login-adm.html", form = form_login_adm)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/formulario-avaliativo", methods = ["GET","POST"])
def forms():
   
    form_avaliacao = FormUserAvalia()
    if form_avaliacao.validate_on_submit():
        incremento_r1 = form_avaliacao.incremento_do_produto_p1.data
        incremento_r2 = form_avaliacao.incremento_do_produto_p2.data
        incremento_r3 = form_avaliacao.incremento_do_produto_p3.data
        incremento_r4 = form_avaliacao.incremento_do_produto_p4.data

        lista_incremento_do_produto = [ incremento_r1, incremento_r2, incremento_r3, incremento_r4]
        media_incremento_do_produto = calc_media(lista_incremento_do_produto)
        

        daily_p1 = form_avaliacao.daily_scrum_p1.data
        daily_p2 = form_avaliacao.daily_scrum_p2.data

        lista_daily_scrum = [daily_p1,daily_p2]
        media_daily_scrum = calc_media(lista_daily_scrum)
      

        sprint_retro_r1 = form_avaliacao.sprint_retrospective_p1.data
        sprint_retro_r2 = form_avaliacao.sprint_retrospective_p2.data
        sprint_retro_r3 = form_avaliacao.sprint_retrospective_p3.data
        sprint_retro_r4 = form_avaliacao.sprint_retrospective_p4.data

        lista_sprint_retro=[sprint_retro_r1,sprint_retro_r2,sprint_retro_r3,sprint_retro_r4]
        media_sprint_retro = calc_media(lista_sprint_retro)
       

        burnu_r1 = form_avaliacao.burnup_p1.data

        sprint_back_r1 = form_avaliacao.sprint_backlog_p1.data
        sprint_back_r2 = form_avaliacao.sprint_backlog_p2.data
        sprint_back_r3 = form_avaliacao.sprint_backlog_p3.data
        sprint_back_r4 = form_avaliacao.sprint_backlog_p4.data

        lista_sprint_back = [sprint_back_r1,sprint_back_r2,sprint_back_r3,sprint_back_r4]
        media_sprint_back = calc_media(lista_sprint_back)
       

        dod_r1 = form_avaliacao.dod_p1.data
        dod_r2 = form_avaliacao.dod_p2.data
        dod_r3 = form_avaliacao.dod_p3.data
        
        lista_dor = [dod_r1,dod_r2,dod_r3]
        media_dod = calc_media(lista_dor)
       

        sprint_rev_r1 = form_avaliacao.sprint_review_p1.data
        sprint_rev_r2 = form_avaliacao.sprint_review_p2.data
        sprint_rev_r3 = form_avaliacao.sprint_review_p3.data
        sprint_rev_r4 = form_avaliacao.sprint_review_p4.data

        lista_sprint_rev = [sprint_rev_r1,sprint_rev_r2,sprint_rev_r3,sprint_rev_r4]
        media_sprint_rev = calc_media(lista_sprint_rev)
        

        burndown_r1 = form_avaliacao.burndown_p1.data
        burndown_r2 = form_avaliacao.burndown_p2.data

        lista_burndown = [burndown_r1,burndown_r2]
        media_burndown = calc_media(lista_burndown)
        

        product_backlog_r1 = form_avaliacao.product_backlog_p1.data
        product_backlog_r2 = form_avaliacao.product_backlog_p2.data
        product_backlog_r3 = form_avaliacao.product_backlog_p3.data
        product_backlog_r4 = form_avaliacao.product_backlog_p4.data

        lista_backlog = [product_backlog_r1,product_backlog_r2,product_backlog_r3,product_backlog_r4]
        media_backlog = calc_media(lista_backlog)
        

        dor_r1 = form_avaliacao.dor_p1.data
        dor_r2 = form_avaliacao.dor_p2.data 
        dor_r3 = form_avaliacao.dor_p3.data

        lista_dor = [dor_r1,dor_r2,dor_r3]
        media_dor = calc_media(lista_dor)
      

        sprint_planning_r1 = form_avaliacao.sprint_planning_p1.data
        sprint_planning_r2 = form_avaliacao.sprint_planning_p2.data 
        sprint_planning_r3 = form_avaliacao.sprint_planning_p3.data
        sprint_planning_r4 = form_avaliacao.sprint_planning_p4.data
        sprint_planning_r5 = form_avaliacao.sprint_planning_p5.data

        lista_sprint_planning = [sprint_planning_r1,sprint_planning_r2,sprint_planning_r3,sprint_planning_r4,sprint_planning_r5]
        media_sprint_planning = calc_media(lista_sprint_planning)
       

        story_point_r1 = form_avaliacao.story_point_p1.data
        story_point_r2 = form_avaliacao.story_point_p2.data

        lista_story_point = [story_point_r1,story_point_r2]
        media_story_point = calc_media(lista_story_point)


        lista_de_sessoes =['m_inpr','m_dasc','m_spretro',
        'm_buup','m_spba','m_dod','m_spre','m_budo','m_prba','m_dor','m_sppl','m_stpo']

        lista_notas = [media_incremento_do_produto,media_daily_scrum,media_sprint_retro,burnu_r1
        ,media_sprint_back,media_dod,media_sprint_rev,media_burndown,media_backlog,media_dor,
        media_sprint_planning,media_story_point]
        
        menor_pos= menor_index(lista_notas)
        menor = lista_de_sessoes[menor_pos]

        maior_pos = maior_index(lista_notas)
        maior = lista_de_sessoes[maior_pos]
        
        formulario = FormsNotas (projeto_id = 1 ,pior_nota_sessao=menor, 
                                 melhor_nota_sessao=maior, m_inpr= media_incremento_do_produto,
                                 m_dasc=media_daily_scrum,m_spretro=media_sprint_retro,
                                 m_buup=burnu_r1,m_spba=media_sprint_back,m_dod=media_dod,
                                 m_spre=media_sprint_rev,m_budo=media_burndown,
                                 m_prba=media_backlog,m_dor =media_dor,m_sppl=media_sprint_planning,
                                 m_stpo = media_story_point)
        database.session.add(formulario)
        database.session.commit()
        
        
        return redirect (url_for("forms"))

    
    if request.method == "POST" and form_avaliacao.errors:
        missing = []
        for field_name, field_errors in form_avaliacao.errors.items():
            try:
                label = getattr(form_avaliacao, field_name).label.text
            except Exception:
                label = field_name
            missing.append(f"{label}: {'; '.join(field_errors)}")
        
      
        
        flash("Você deve preencher todos os campos do formulário", "danger")

    return render_template("forms.html", page_url="formulario-avaliativo", form = form_avaliacao)
 
# Páginas de conteúdo
 
#Visão Geral e papéis
@app.route("/area-restrita")
@login_required
def area_restrita():
    return render_template("/area-restrita.html")

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

#Eventos
 
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
 
#Artefatos
@app.route("/product-backlog")
def productBacklog():
    return render_template("/paginas-treinamento/product-backlog.html", page_url="productBacklog")
 
@app.route("/sprint-backlog")
def sprintBacklog():
    return render_template("/paginas-treinamento/sprint-backlog.html", page_url="sprintBacklog")
 
@app.route("/incremento-produto")
def incrementoProduto():
    return render_template("/paginas-treinamento/incremento.html", page_url="incrementoProduto")
 
#Itens solos
@app.route("/definition-of-ready")
def definitionOfReady():
    return render_template("/paginas-treinamento/dor.html", page_url="definitionOfReady")
 
@app.route("/definition-of-done")
def definitionOfDone():
    return render_template("/paginas-treinamento/dod.html", page_url="definitionOfDone")
 
#Métricas Ágeis
@app.route("/story-point")
def storyPoint():
    return render_template("/paginas-treinamento/story-point.html", page_url="storyPoint")
 
@app.route("/burn-down-chart")
def burnDownChart():
    return render_template("/paginas-treinamento/burndown.html", page_url="burnDownChart")

@app.route("/burn-up-chart")
def burnUpChart():
    return render_template("/paginas-treinamento/burnup.html", page_url="burnUpChart")