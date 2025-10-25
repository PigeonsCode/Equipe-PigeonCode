from projeto import database,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Adm_User.query.get(int(id_usuario))


class Adm_User(database.Model,UserMixin):
     id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
     user_db = database.Column(database.String,nullable=False, unique=True)
     password_db = database.Column(database.String,nullable=False,unique=True)


class FormsNotas(database.Model):
     id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
     projeto_id = database.Column(database.Integer,database.ForeignKey('projetos.id'),nullable=False)
     pior_nota_sessao = database.Column(database.String, nullable=False)
     melhor_nota_sessao = database.Column(database.String, nullable=False)
     m_inpr = database.Column(database.Float, nullable=False)
     m_dasc = database.Column(database.Float, nullable=False)
     m_spretro = database.Column(database.Float, nullable=False)
     m_buup = database.Column(database.Float, nullable=False)
     m_spba = database.Column(database.Float, nullable=False)
     m_dod = database.Column(database.Float, nullable=False)
     m_spre = database.Column(database.Float, nullable=False)
     m_budo = database.Column(database.Float, nullable=False)
     m_prba = database.Column(database.Float, nullable=False)
     m_dor = database.Column(database.Float, nullable=False)
     m_sppl = database.Column(database.Float, nullable=False)
     m_stpo = database.Column(database.Float, nullable=False)

class Projetos(database.Model):
     id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
     nome_projeto = database.Column(database.String, unique=True, nullable=False)
     id_forms = database.relationship('FormsNotas', backref = 'projetos', lazy=True)