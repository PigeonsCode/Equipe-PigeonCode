from flask import render_template,url_for
from projeto.navigation import navigation_items
from projeto import app
 
@app.route("/")
def homepage():
    return render_template("index.html", navigation=navigation_items, page_url="homepage")
 
@app.route("/login-adm")
def loginADM():
    return render_template("login-adm.html")
 
@app.route("/formularios")
def forms():
    return render_template("forms.html", page_url="scrum")
 
# Páginas de conteúdo
 
#Visão Geral e papéis
 
@app.route("/scrum")
def scrum():
    return render_template("/paginas-treinamento/scrum.html", page_url="scrum", first_item = True)
 
@app.route("/manifesto-agil")
def manifestoAgil():
    return render_template("/paginas-treinamento/manifesto.html", page_url="manifestoAgil",  first_item = True)
 
@app.route("/principios-ageis")
def principiosAgeis():
    return render_template("/paginas-treinamento/principios.html", page_url="principiosAgeis",  first_item = True)
 
@app.route("/product-owner")
def productOwner():
    return render_template("/paginas-treinamento/product-owner.html", page_url="productOwner",  first_item = True)
 
@app.route("/scrum-master")
def scrumMaster():
    return render_template("/paginas-treinamento/scrum-master.html", page_url="scrumMaster",  first_item = True)
 
@app.route("/dev-team")
def devTeam():
    return render_template("/paginas-treinamento/dev-team.html", page_url="devTeam",  first_item = True)
 
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
 
# Rota de visualização de template
@app.route("/template")
def template():
    return render_template("/paginas-treinamento/1-TEMPLATE.html", page_url="template")