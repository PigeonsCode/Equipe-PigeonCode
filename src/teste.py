from projeto import database,app
from projeto.models import Adm_User




with app.app_context():
 user=Adm_User(
 user_db="cliente-adm",
 password_db="api2025fatecsjc"
 
)
 database.session.add(user)
 database.session.commit()

#deixar session commit na mesma identação