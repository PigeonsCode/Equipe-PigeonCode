from flask_wtf import FlaskForm #biblioteca que permite a criação de formulários de login
from wtforms import StringField, PasswordField,SubmitField,RadioField #importação dos campos dos formulários
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError #importação de funções que validam as informações inseridas 
#pelo usuário
from projeto.models import Adm_User



class FormLoginAdm(FlaskForm):
    username_adm = StringField("Nome de Usuário",validators=[DataRequired()])
    password_adm= PasswordField("Senha", validators=[DataRequired()])
    submit_button =  SubmitField("Entrar")
#validação dos dados inseridos pelo usuário

class FormUserAvalia(FlaskForm):
    # Inserir a numeração correta das perguntas e inserir coerce=int em todas as perguntas,
    #para que haja a conversão de string para int
    p1 = RadioField("Perguntas 1",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],coerce=int,validators=[DataRequired()])
    
    p2 = RadioField("Perguntas 2",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p3 = RadioField("Perguntas 3",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p4 = RadioField("Perguntas 4",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p5 = RadioField("Perguntas 5",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p6 = RadioField("Perguntas 6",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p7 = RadioField("Perguntas 7",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p8 = RadioField("Perguntas 8",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p9 = RadioField("Perguntas 9",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p10 = RadioField("Perguntas 10",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])


    p11 = RadioField("Perguntas 11",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])


    p12 = RadioField("Perguntas 12",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])


    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    
    p14 = RadioField("Perguntas 14",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p13 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    





