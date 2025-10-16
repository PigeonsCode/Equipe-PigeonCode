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































































































































































































    



     incremento_do_produto_p9 = RadioField("Como foi a satisfação do cliente em relação à entrega do incremento do produto ao final do Sprint?",
                          choices=[
                          (4,"O cliente está completamente satisfeito e ansioso para a próxima entrega. Foram feitas nulas ou poucas críticas a respeito do que lhe foi apresentado e o feedback se manteve positivo em praticamente toda sua extensão."),
                          (3,"Cliente satisfeito, porém aponta refinamentos. Foram feitas poucas críticas leves e quase nenhuma crítica extensa. O feedback foi majoritariamente positivo, poucas mudanças solicitadas."),
                          (2,"O cliente está insatisfeito e exigente para a próxima entrega. Foram feitas muitas críticas leves e muitas críticas extensas. O feedback pendeu mais para o lado negativo do que positivo e mudanças drásticas foram solicitadas."),
                          (1,"Cliente extremamente insatisfeito e risco de desistência. Foram feitas apenas críticas extensas. O feedback foi completamente negativo e a continuação do projeto está ameaçada.")],validators=[DataRequired()])
    
     inscremento_do_produto_p10 = RadioField("O incremento do produto atendeu a todas as tarefas definidas na versão final do Sprint Backlog?",
                          choices=[
                          (4,"Sim, todas as tarefas obrigatórias foram concluídas com êxito e também as definidas como metas complementares. O maior valor de produto para aquela Sprint foi entregue com sucesso."),
                          (3,"Parcialmente, todas as tarefas obrigatórias foram concluídas, porém algumas ou todas as complementares foram deixadas para a próxima Sprint. O valor do incremento do produto entregue foi alto."),
                          (2,"Minimamente, algumas tarefas obrigatórias não foram concluídas e nenhuma das complementares. O valor do produto entregue foi menor do que o prometido."),
                          (1,"Não, nenhuma tarefa foi concluída como o planejado e o valor do produto entregue não foi cumprido, ameaçando a completude das próximas Sprints.")],validators=[DataRequired()])


     incremento_do_produto_p11 = RadioField("O incremento trouxe avanços significativos para atingir a meta do projeto na totalidade?",
                          choices=[
                          (4,"Sim, o incremento concluiu com o que prometeu no Product Backlog e avança com o valor do produto planejado para as próximas Sprints."),
                          (3,"Parcialmente, o incremento concluiu a maioria dos itens que prometeu no Product Backlog, mas afeta o valor do produto que será remanejado para próximas Sprints."),
                          (2,"Minimamente, o incremento concluiu a minoria dos itens que prometeu no Product Backlog e arrisca o valor do produto planejado para as próximas Sprints. Não atrapalha gravemente o andamento do projeto."),
                          (1,"Não, o incremento não coincide com o prometido e ameaça fortemente a conclusão do projeto conforme a meta e tempo planejados. Há possibilidade de não conseguir entregar ao final de todas as Sprints.")],validators=[DataRequired()])


     incremento_do_produto_p12 = RadioField("O produto entregue está conforme os critérios definidos pela Definição de Pronto?",
                          choices=[
                          (4,"Sim, tudo o que foi pontuado no DoD foi seguido estritamente pela equipe e a qualidade do incremento reflete isso."),
                          (3,"Parcialmente, a minoria dos itens do DoD foram esquecidos, porém, a qualidade do incremento não foi comprometida."),
                          (2,"Minimamente, a maioria dos itens do DoD foram esquecidos e, com isso, a qualidade do incremento foi comprometida, ocasionando em complicações que terão que ser resolvidas na próxima Sprint."),
                          (1,"Não, os itens do DoD não foram seguidos e a qualidade do incremento foi muito comprometida, levando bugs, erros e outras complicações para a próxima Sprint.")],validators=[DataRequired()])
    
     daily_scrum_p19 = RadioField("Nas reuniões de Daily Scrum, foram feitas perguntas para acompanhar o que já foi feito, quais serão os próximos passos e se há impedimentos, para cada membro do Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, todos foram questionados e deram respostas sobre o progresso, planejamento e impedimentos de forma satisfatória."),
                          (3,"Parcialmente, a maioria foi questionada e deu respostas sobre o progresso, planejamento e impedimentos de forma aceitável."),
                          (2,"Minimamente, a minoria foi questionada e deu respostas sobre o progresso, planejamento e impedimentos de forma insatisfatória."),
                          (1,"Não, não foi utilizado nenhuma metodologia de perguntas para acompanhar o progresso, planejamento e impedimentos do time, ocasionando em extrema incerteza sobre o andamento do trabalho.")],validators=[DataRequired()])
    
     daily_scrum_p20 = RadioField("Como você avalia a eficácia das reuniões de Daily Scrum? (Considere se elas mantiveram o foco de acompanhar o progresso do Sprint.)",
                          choices=[
                          (4,"Ótima, todos tiveram abertura e conseguiram comunicar claramente sobre seus progressos, planos e impedimentos, deixando evidente o avanço do time."),
                          (3,"Boa, a maioria teve abertura e conseguiu comunicar claramente sobre seus progressos, planos e impedimentos. Por terem membros que ou não se comunicaram com clareza, ou não tiveram espaço para falar, o avanço do time é perceptível, mas incerto em certas partes."),
                          (2,"Neutra, a minoria teve abertura na conversa e conseguiram comunicar claramente sobre seus progressos, planos e impedimentos. O avanço do time é dificilmente perceptível e há várias incertezas."),
                          (1,"Negativa, nenhuma parte conseguiu se comunicar sobre seus progressos, planos e impedimentos, ocasionando no time estando completamente perdido quanto ao avanço do time.")],validators=[DataRequired()])
    
     sprint_retrospective_p30 = RadioField("Durante a reunião da Sprint Retrospective, os colaboradores da equipe citaram o que ocorreu bem, onde detectaram problemas e as áreas de melhoria?",
                          choices=[
                          (4,"Sim, todos os pontos positivos, fraquezas e áreas de melhoria foram abordados de forma aberta e colaborativa."),
                          (3,"Parcialmente, alguns pontos positivos e problemas foram abordados, mas nem todas as áreas de melhoria foram identificadas."),
                          (2,"Minimamente, poucos pontos foram discutidos, sem aprofundamento em causas ou soluções."),
                          (1,"Não, a equipe não discutiu abertamente os pontos positivos, problemas e nem as áreas de melhoria.")],validators=[DataRequired()])
    
     sprint_retrospective_p31 = RadioField("Todos os integrantes (Product Owner, Scrum Master e Dev Team) conseguiram apresentar suas perspectivas de forma aberta e construtiva?",
                          choices=[
                          (4,"Sim, todos os integrantes apresentaram suas perspectivas ativamente, expressando suas perspectivas com respeito, abertura e foco na melhoria do time."),
                          (3,"Parcialmente, a maioria dos integrantes participou apresentando suas perspectivas, mas houve pouca contribuição ou abertura por parte de alguns membros."),
                          (2,"Minimamente, poucos integrantes apresentaram suas perspectivas, com pouca contribuição aberta e construtiva dentre os membros do time."),
                          (1,"Não, os integrantes não tiveram abertura para expressar suas opiniões de forma construtiva.")],validators=[DataRequired()])
    
     sprint_retrospective_p32 = RadioField("Houve uma boa concordância e uniformidade nas respostas de cada um? Ou cada membro pareceu ter uma perspectiva diferente do que deu ou não, certo?",
                          choices=[
                          (4,"Sim, os membros do grupo compartilham percepções semelhantes sobre o que foi realizado corretamente e sobre o que ainda pode ser aprimorado."),
                          (3,"Parcialmente, alguns membros apresentaram pontos semelhantes sobre o que foi feito corretamente e ao que ainda precisa ser aprimorado, enquanto outros demonstraram pontos de vista diferentes."),
                          (2,"Minimamente, apesar de haver concordância entre as respostas, a maioria apresentou percepções distintas sobre o que foi realizado corretamente e sobre os pontos que precisam de melhoria."),
                          (1,"Não, os membros do grupo demonstraram perspectivas totalmente distintas sobre o que foi bem realizado e sobre os pontos que podem melhorar.")],validators=[DataRequired()])
    
     sprint_retrospective_p33 = RadioField("Houve uma participação ativa de todos os membros na reunião?",
                          choices=[
                          (4,"Sim, todos os membros do grupo mostraram proatividade em compartilhar ideias, expressar pontos de vista e contribuírem de forma ativa para as decisões do grupo."),
                          (3,"Parcialmente, a maioria dos membros se mostrou ativo para compartilhar suas perspectivas, mas alguns não tiveram a mesma participação."),
                          (2,"Minimamente, poucos membros do grupo compartilharam suas ideias e perspectivas, mas ainda houve participação ativa entre alguns."),
                          (1,"Não, nenhum membro do grupo se mostrou proativo a participar e compartilhar suas perspectivas e contribuir ativamente.")],validators=[DataRequired()])
    
     burnup_p38 = RadioField("Como você avalia a utilização do gráfico de Burnup para o acompanhamento da conclusão das Sprints ao longo do projeto todo?",
                          choices=[
                          (4,"O gráfico de Burnup foi utilizado de forma eficaz para acompanhar a conclusão das Sprints ao longo do projeto, permitindo que o time visualizasse de forma clara o progresso e identificasse se estava dentro do planejamento."),
                          (3,"O gráfico de Burnup ajudou na visualização do progresso do projeto e acompanhamento das Sprints, embora em alguns momentos a interpretação dos dados pudesse ser melhorada."),
                          (2,"A utilização do gráfico de Burnup teve impacto limitado, sendo pouco utilizado para monitorar a conclusão das Sprints ou para tomar decisões de planejamento."),
                          (1,"O gráfico de Burnup não foi utilizado de forma adequada, dificultando a visualização do progresso das Sprints e comprometendo o acompanhamento do avanço do projeto.")],validators=[DataRequired()])
    
    