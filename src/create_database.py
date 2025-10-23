from projeto import database, app
from projeto.models import Adm_User, FormsNotas


with app.app_context():
    database.create_all()

