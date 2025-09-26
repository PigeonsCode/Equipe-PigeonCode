import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #importação do banco de dados
from flask_login import LoginManager
from flask import url_for, request


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SECRET_KEY"] = "ba7783e47efacd4b8c6b40475222bbac"
database = SQLAlchemy(app)




from projeto.navigation import navigation_items

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
def inject_navigation():
    nav_copy = []
    for nav in navigation_items:
        nav_copy.append({**nav, 'nav_open': is_nav_open(nav, request.path), 'show_aside': show_aside(nav, request.path)})
    return dict(navigation=nav_copy)



from projeto import routes, models
