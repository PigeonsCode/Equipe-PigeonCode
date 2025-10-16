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
   


































































































    
    sprint_backlog_p1 = RadioField("As tarefas definidas no Sprint Backlog decorrem dos respectivos itens no Product Backlog?",
                          choices=[
                          (4,"Sim, todas as tarefas são derivadas de pelo menos uma das User Stories programadas para a Sprint em questão."),
                          (3,"Parcialmente, algumas tarefas decorrem de User Stories de Sprints passadas ou futuras, mas a maioria está fiel ao programado para a Sprint."),
                          (2,"Minimamente, a maioria das tarefas estão desconexas com as User Stories definidas previamente, deixando o time confuso sobre o que deve ser entregue."),
                          (1,"Não, nenhuma das tarefas decorrem das User Stories corretas, impossibilitando que o time entregue o MVP referente a Sprint.")],validators=[DataRequired()])
    
    sprint_backlog_p2 = RadioField("A velocidade é definida pela quantidade média de Story points concluídos em uma Sprint. Com base nessa definição, os itens do Sprint Backlog respeitam a métrica do time?",
                          choices=[
                          (4,"Sim, os itens foram definidos o mais próximo possível da média alcançável, tendo qualquer item sobressalente definido como meta complementar às obrigatórias."),
                          (3,"Parcialmente, houve a tentativa de permanecer na média do time, mas devido ao valor prometido, itens a mais foram estabelecidos como meta obrigatória."),
                          (2,"Minimamente, ou a quantidade de Story Points está consideravelmente acima da média, arriscando a conclusão do prometido para Sprint. Ou, a quantidade de Story Points está consideravelmente abaixo da média e não foram adicionados mais itens para evitar períodos de zero produtividade"),
                          (1,"Não, a média não foi considerada em nenhum momento e a quantidade de Story Points está muito acima ou muito abaixo da média, arriscando a entrega do produto inteiro e a qualidade das próximas Sprints.")],validators=[DataRequired()])
    
    sprint_backlog_p3 = RadioField("A Sprint possui um MVP (Produto mínimo viável) bem estabelecido?",
                          choices=[
                          (4,"Sim, o MVP pode ser enxergado claramente tanto pelas tarefas abordadas no Sprint Backlog, quanto explicado mais a fundo em algum outro tipo de documento. A equipe tem plena consciência do que deve ser entregue."),
                          (3,"Parcialmente, o MVP pode ser enxergado nas tarefas abordadas do Sprint Backlog, porém não está registrado explicitamente em nenhum lugar. A equipe tem bom conhecimento sobre o que deve ser entregue."),
                          (2,"Minimamente, o MVP pode ser vagamente observado nas tarefas e não está registrado em nenhum outro local. A equipe está consideravelmente perdida em relação ao que foi prometido."),
                          (1,"Não, o MVP não é claro por meio da escolha das tarefas e não está anotado em nenhum lugar. A equipe não sabe o que deve ser entregue.")],validators=[DataRequired()])
    
    sprint_backlog_p4 = RadioField("As tarefas selecionadas possuem prioridade, User Story e estimativas (Story Points) bem definidas?",
                          choices=[
                          (4,"Sim, as tarefas listadas no Sprint Backlog possuem cada um dos itens mencionados, escritos de forma clara e concisa."),
                          (3,"Parcialmente, quase todas estão padronizadas e alguns itens estão mais concisos e bem escritos do que outros."),
                          (2,"Minimamente, a lista foi feita seguindo um padrão diferente, porém ainda mantém os itens principais: User Story e Story Points."),
                          (1,"Não, a lista está despadronizada e segue algo único e pensado pela própria equipe ao invés das normas especificadas.")],validators=[DataRequired()])
    
    dod_p1 = RadioField(" A Definition of Done têm critérios de aceitação bem definidos para considerar um item pronto?",
                          choices=[
                          (4,"Sim, foram definidos critérios de aceitação bem específicos, objetivos e inquestionáveis, levando a uma fácil compreensão sobre o que se considerou pronto."),
                          (3,"Parcialmente, foram definidos critérios de aceitação específicos, objetivos, mas questionáveis, levando a algumas dúvidas sobre o que se considerou pronto."),
                          (2,"Minimamente, foram definidos critérios nada específicos, não objetivos e questionáveis, levando a uma dificuldade de compreensão sobre o que se considera pronto."),
                          (1,"Não, não foram definidos critérios de aceitação sobre a DoD, ocasionando total falta de consenso no que seria considerado pronto")],validators=[DataRequired()])
    
    dod_p2 = RadioField("A Definition of Done foi acordada formalmente entre o Product Owner e o Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, o Product Owner e o time desenvolveram os critérios em conjunto, deixando a DoD documentada e de fácil acesso a todos."),
                          (3,"Parcialmente, uma das partes teve mais poder de decisão do que a outra, porém a DoD foi documentada e de fácil acesso a todos."),
                          (2,"Minimamente, apenas uma das partes decidiu os critérios para a DoD, em que ela não está claramente documentada e não está de fácil acesso a todos."),
                          (1,"Não, apenas uma das partes decidiu os critérios, a DoD não está documentada, sendo lembrada por meio de acordos verbais, gerando grandes chances do filtro ser completamente ignorado e vários itens não prontos serem aprovados.")],validators=[DataRequired()])
    
    dod_p3 = RadioField("O DoR foi seguido corretamente pela equipe de desenvolvimento?",
                          choices=[
                          (4,"Sim, todos tiveram uma clara compreensão e conseguiram seguir os critérios para definir itens como preparado corretamente."),
                          (3,"Parcialmente, a maioria teve uma boa compreensão e conseguiu seguir os critérios para definir itens como preparado de forma aceitável, mas não excelente."),
                          (2,"Minimamente, a minoria compreendeu e dificilmente conseguiu seguir os critérios para definir itens como preparado, tendo alguns itens definidos incorretamente."),
                          (1,"Não, não houve compreensão e não foi possível seguir os critérios para definir itens como preparado corretamente.")],validators=[DataRequired()])
    
    
    sprint_review_p1 = RadioField("As partes interessadas forneceram feedback sobre o incremento apresentado?",
                          choices=[
                          (4,"Sim, as partes interessadas forneceram feedback claro e construtivo sobre o incremento, contribuindo significativamente para melhorias no produto"),
                          (3,"Parcialmente, o feedback das partes interessadas foi fornecido acerca do incremento, mas de forma pouco objetiva ou pouco detalhada."),
                          (2,"Minimamente, houve pouco feedback das partes interessadas sobre o incremento, sem contribuições relevantes para sua melhoria."),
                          (1,"Não, as partes interessadas não forneceram feedback sobre o incremento apresentado, resultando em incerteza sobre o nível de satisfação.")],validators=[DataRequired()])
    
    sprint_review_p2 = RadioField("Os resultados do Sprint estão bem alinhados à visão do produto e ao objetivo definido? Houve impedimentos significativos que afetaram essas entregas?",
                          choices=[
                          (4,"Sim, os resultados do Sprint estão totalmente alinhados à visão do produto e ao objetivo definido. Não houve impedimentos significativos durante o trabalho."),
                          (3,"Parcialmente, os resultados do Sprint estão em boa parte alinhados à visão do produto e ao objetivo definido. Mas alguns impedimentos afetaram pequenas entregas e detalhes."),
                          (2,"Minimamente, os resultados do Sprint ficaram pouco alinhados com a visão do produto e o objetivo definido. Houve impedimentos relevantes que afetaram a entrega."),
                          (1,"Não, os resultados do Sprint estão desalinhados com a visão do produto e com o objetivo definido. Houve fortes impedimentos que comprometeram significativamente a entrega.")],validators=[DataRequired()])
    
    sprint_review_p3 = RadioField("No caso de itens não concluídos, o Product Backlog foi atualizado de acordo?",
                          choices=[
                          (4,"Sim, o Product Backlog foi atualizado de acordo, refletindo fielmente o estado atual dos itens não concluídos"),
                          (3,"Parcialmente, o Product Backlog foi atualizado de acordo, mas alguns ajustes ou itens ficaram pendentes de revisão."),
                          (2,"Minimamente, o Product Backlog foi atualizado de forma incompleta, com diversas informações desatualizadas."),
                          (1,"Não, o Product Backlog não foi atualizado, afetando a transparência e o planejamento das próximas Sprints.")],validators=[DataRequired()])
    
    sprint_review_p4 = RadioField("Com base no ritmo do time e nas funcionalidades restantes, a previsão de entrega para o Produto Final ainda é realista?",
                          choices=[
                          (4,"Sim, a previsão de entrega continua realista, considerando o ritmo de trabalho atual e as atividades restantes."),
                          (3,"Parcialmente, a previsão de entrega ainda é realista, mas há riscos que podem comprometer o prazo se não receberem atenção e serem tratados."),
                          (2,"Minimamente, a previsão de entrega parece pouco realista, e o ritmo de trabalho do time precisa se ajustar para evitar atrasos."),
                          (1,"Não, a previsão de entrega não parece mais realista, exigindo um replanejamento e revisão do trabalho acerca do produto.")],validators=[DataRequired()])
    
    burndown_p1 = RadioField("O gráfico apresenta uma linha de progresso ideal, dedicada a guiar o tempo em que as tarefas são concluídas até o final do Sprint?",
                          choices=[
                          (4,"Sim, o gráfico apresenta uma linha de progresso ideal, que serve como referência para guiar o ritmo em que as tarefas devem ser concluídas ao longo do Sprint."),
                          (3,"Parcialmente, nem todas as tarefas ou prazos refletem com precisão o ritmo planejado."),
                          (2,"Minimamente, o gráfico mostra apenas alguns pontos de referência do progresso ideal, dificultando que o time o use como guia consistente para acompanhar a conclusão das tarefas."),
                          (1,"Não, o gráfico não apresenta uma linha de progresso ideal clara, impedindo que o time tenha uma referência eficaz para acompanhar o andamento das tarefas até o final do Sprint.")],validators=[DataRequired()])
    
    burndown_p2 = RadioField("Ao longo do Sprint, no BurnDown Chart, como você avalia a linha de conclusão do trabalho real com a linha de conclusão ideal estabelecida?",
                          choices=[
                          (4,"A linha de conclusão do trabalho real acompanhou a linha ideal, mostrando que o Sprint seguiu o planejamento previsto e que o time conseguiu cumprir as tarefas dentro do prazo."),
                          (3,"A linha de conclusão do trabalho real apresentou um desempenho próximo da linha ideal, com pequenas variações."),
                          (2,"A linha de conclusão do trabalho real divergiu de forma considerável da linha ideal em alguns momentos."),
                          (1,"A linha de conclusão do trabalho real apresentou grandes diferenças em relação à linha ideal, mostrando que o planejamento do Sprint não foi seguido corretamente e que o time enfrentou dificuldades para concluir as tarefas no prazo.")],validators=[DataRequired()])
    
    
 





