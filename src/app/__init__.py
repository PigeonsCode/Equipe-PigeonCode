import re
from flask import Flask
app=Flask(__name__)
from app import routes

from app.navigation import navigation_items

@app.context_processor
def inject_navigation():
    return dict(navigation=navigation_items)

def kebab_case(value):
    if not value:
        return ''
    camelCaseString = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', value)
    kebabCaseString = re.sub('([a-z0-9])([A-Z])', r'\1-\2', camelCaseString)
    return kebabCaseString.lower()

app.jinja_env.filters['kebabify'] = kebab_case