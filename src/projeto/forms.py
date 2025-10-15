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
    product_backlog_p1 = RadioField("As tarefas foram priorizadas a partir da dor do cliente?",
                          choices=[
                          (4,"Sim e todos os itens seguem uma ordem de prioridade definida a partir dos princípios e feedbacks do cliente."),
                          (3,"Parcialmente, a maioria dos itens está priorizada no ponto de vista do cliente, porém um item ou outro leva em conta requisitos na perspectiva de desenvolvimento ao invés do que traz maior valor de produto."),
                          (2,"Minimamente, a minoria parte da dor do cliente, enquanto outras pela ótica do desenvolvimento e as outras que deveriam ser incluídas foram esquecidas."),
                          (1,"Não foram respeitadas as dores do cliente, levando a um Product Backlog inconciso e incerto quanto ao MVP.")],coerce=int,validators=[DataRequired()])
    
    product_backlog_p2 = RadioField("Os itens do Product Backlog seguem o padrão de Id, User Story, Descrição, Prioridade e Estimativa?",
                          choices=[
                          (4,"Sim, as tarefas listadas no Product Backlog possuem cada um dos itens mencionados, escritos de forma clara e concisa."),
                          (3,"Parcialmente, quase todas estão padronizadas e alguns itens estão mais concisos e bem escritos do que outros."),
                          (2,"Minimamente, a lista foi feita seguindo um padrão diferente, porém ainda mantém os itens principais: User Story, Descrição e Prioridade."),
                          (1,"Não, a lista está despadronizada e segue algo único e pensado pela própria equipe ao invés das normas especificadas.")],validators=[DataRequired()])
    
    product_backlog_p3 = RadioField("As User Stories têm uma definição clara de seus objetivos?",
                          choices=[
                          (4,"Sim, as histórias foram escritas claramente e seguem o padrão: Como <usuário>, quero <funcionalidade> para <finalidade>."),
                          (3,"Parcialmente, algumas histórias ficaram confusas, permitindo interpretações levemente diferentes dos membros. Contudo, seguem o padrão especificado."),
                          (2,"Minimamente, a maioria das histórias são confusas, permitindo várias interpretações diferentes. Algumas seguem o padrão, enquanto outras fogem."),
                          (1,"Não, todas as histórias estão confusas e mal escritas, deixando o time desorientado sobre o caminho a seguir. Não seguem o padrão em nenhum dos itens listados.")],
                          validators=[DataRequired()])
    
    product_backlog_p4 = RadioField("Houve mudanças decorrentes de conversas com o cliente? Se sim, o Product Backlog foi atualizado corretamente a partir do novo feedback?",
                          choices=[
                          (4,"Mudanças existiram e o Product Backlog foi alterado de acordo, com os novos itens seguindo o padrão corretamente. "),
                          (3,"O Product Backlog não possui todas as atualizações conversadas. Porém, os itens adicionados continuam seguindo o padrão corretamente. "),
                          (2,"Não houveram mudanças e o Product Backlog não precisou ser alterado, mantendo a qualidade que já possuía."),
                          (1,"O Product Backlog não foi alterado, mesmo com atualizações pendentes. Permaneceu o mesmo até o fim da Sprint. ")],validators=[DataRequired()])
    
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


    dor_p1 = RadioField("A Definition of Ready têm critérios específicos, mensuráveis e atingíveis para considerar um item preparado?",
                          choices=[
                          (4,"Sim, todos os critérios da DoR são específicos, mensuráveis e atingíveis, proporcionando total clareza e objetividade para os membros do time."),
                          (3,"Parcialmente, a maioria dos critérios são específicos, mas existem itens subjetivos, gerando o risco de debates durante a checagem."),
                          (2,"Minimamente, a maioria dos critérios é vago e não mensurável. A DoR foi feita, mas raramente é checada."),
                          (1,"Não, os critérios são completamente subjetivos e a equipe está perdida. Ou a DoR é ignorada ou nem foi feita pelo time.")]
                          ,validators=[DataRequired()])
    
    
    dor_p2 = RadioField("A Definition of Ready foi acordada formalmente entre o Product Owner e o Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, o Product Owner e o time desenvolveram os critérios em conjunto, deixando a DoR documentada e de fácil acesso a todo"),
                          (3,"Parcialmente, uma das partes teve mais poder de decisão do que a outra, porém a DoR foi documentada e de fácil acesso a todos."),
                          (2,"Minimamente, apenas uma das partes decidiu os critérios para a DoR, em que ela não está claramente documentada e não está de fácil acesso a todos"),
                          (1,"Não, apenas uma das partes decidiu os critérios, a DoR não está documentada, sendo lembrada por meio de acordos verbais, gerando grandes chances do filtro ser completamente ignorado e vários itens não preparados serem aprovados.")],validators=[DataRequired()])
    
    dor_p3 = RadioField("O DoR foi seguido corretamente pela equipe de desenvolvimento?",
                          choices=[
                          (4,"Sim, todos tiveram uma clara compreensão e conseguiram seguir os critérios para definir itens como preparado corretamente."),
                          (3,"Parcialmente, a maioria teve uma boa compreensão e conseguiu seguir os critérios para definir itens como preparado de forma aceitável, mas não excelente."),
                          (2,"Minimamente, a minoria compreendeu e dificilmente conseguiu seguir os critérios para definir itens como preparado, tendo alguns itens definidos incorretamente"),
                          (1,"Não, não houve compreensão e não foi possível seguir os critérios para definir itens como preparado corretamente.")],validators=[DataRequired()])
    
    p16 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p17 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p18 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p19 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p20 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p21 = RadioField("Na reunião, foram definidos quais itens do Product Backlog seriam realizados na Sprint?",
                          choices=[
                          (4,"Sim, os itens do Product Backlog que seriam selecionados para a Sprint foram definidos de forma clara e objetiva, não gerando dúvidas."),
                          (3,"Parcialmente, os itens do Product Backlog que seriam selecionados para a Sprint não foram definidos com excelência, mas foi possível ter uma compreensão boa, sem muitas dúvidas."),
                          (2,"Minimamente, os itens do Product Backlog que seriam selecionados para a Sprint não foram definidos corretamente, gerando pouca compreensão e muitas dúvidas."),
                          (1,"Não, não foram definidos os itens do Product Backlog a serem selecionados para a Sprint, gerando grande incompreensão e falta de organização.")],
                          validators=[DataRequired()])
    
    p22 = RadioField("As tarefas foram planejadas devidamente?",
                          choices=[
                          (4,"Sim, as tarefas foram planejadas considerando os itens do Product Backlog que devem ser priorizados, bem como quais serão os itens entregáveis para a Sprint e se existem riscos e dependências entre eles."),
                          (3,"Parcialmente, as tarefas consideraram a maioria dos itens marcados como prioridade no Product Backlog, excluindo alguns itens de pouca prioridade. Foram definidos os itens entregáveis, mas a análise de riscos e dependências foi pouco discutida."),
                          (2,"Minimamente, as tarefas desconsideraram algumas prioridades médias e várias das baixas. Itens que deveriam entrar como entregáveis foram esquecidos e a análise de riscos foi extremamente breve ou inexistente."),
                          (1,"Não, as tarefas selecionadas não levaram em conta quais itens deveriam ser priorizados do Product Backlog, muito menos os itens entregáveis e os riscos e dependências entre eles; resultando em uma Sprint com promessas confusas.")],validators=[DataRequired()])
    
    p23 = RadioField("Como você avalia a forma como foi feita a divisão das tarefas?",
                          choices=[
                          (4,"Ótima, as tarefas foram bem distribuídas, considerando a capacidade e habilidade de cada membro, favorecendo o equilíbrio do time e o cumprimento dos prazos."),
                          (3,"Boa, a maioria das tarefas foram distribuídas considerando a capacidade e habilidade de cada membro e, como certas tarefas foram mal pensadas, uma pequena parte dos colaboradores tem mais trabalho e responsabilidades."),
                          (2,"Neutra, a maioria das tarefas foram distribuídas sem considerar a capacidade e habilidade de cada membro e, com isso, vários colaboradores se viram sobrecarregados de trabalho."),
                          (1,"Ruim, as tarefas foram mal distribuídas, muitos membros ficaram sobrecarregados enquanto outros tiveram pouca participação e ficaram ociosos.")],validators=[DataRequired()])
    
    p24 = RadioField("Os itens selecionados do Product Backlog atendiam ao DoR definido antes do início do planejamento?",
                          choices=[
                          (4,"Sim, todos os itens selecionados do Product Backlog atenderam ao DoR definido, apresentando critérios claros, compreensíveis e prontos para execução."),
                          (3,"Parcialmente, a maioria dos itens selecionados do Product Backlog atendeu ao DoR definido, mas alguns apresentaram dúvidas que precisaram ser resolvidas durante a Sprint."),
                          (2,"Minimamente, poucos itens selecionados do Product Backlog atenderam ao DoR definido, ocasionando grandes incertezas e retrabalho durante a execução."),
                          (1,"Não, os itens selecionados do Product Backlog não atenderam ao DoR definido, comprometendo a clareza e o andamento do Sprint.")],validators=[DataRequired()])
    
    p25 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p26 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p27 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p28 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p29 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p30 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p31 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p32 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p33 = RadioField("Pergunta 33",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p34 = RadioField("As Story Points foram definidas de acordo com as estimativas de esforço entre os membros do Time de Desenvolvimento?",
                          choices=[
                          (4,"Sim, todas as Story Points foram definidas de acordo com as estimativas de esforço compartilhadas pelos membros do Time de Desenvolvimento."),
                          (3,"Parcialmente, a maioria das Story Points foram definidas com as estimativas de esforço entre os membros do Time de Desenvolvimento, mas houveram outras que foram definidas por perspectivas individuais."),
                          (2,"Minimamente, poucas Story Points foram definidas de acordo com as estimativas do Time de Desenvolvimento."),
                          (1,"Não, as Story Points não foram definidas de acordo com as estimativas do Time de Desenvolvimento, sendo determinadas sem consenso ou alinhamento entre os membros.")],validators=[DataRequired()])
    
    
    p35 = RadioField(" Como você avalia a utilização das métricas de estimativa em seus Backlogs?",
                          choices=[
                          (4,"As métricas de estimativa foram utilizadas de forma consistente e eficaz, permitindo que o Time de Desenvolvimento planejasse e priorizasse as tarefas do Backlog com clareza e precisão."),
                          (3,"As métricas de estimativa foram úteis na maior parte do tempo, auxiliando o planejamento do Backlog, embora algumas tarefas possam não ter sido estimadas com total precisão."),
                          (2,"A utilização das métricas de estimativa apresentou resultados medianos, sem grande impacto no planejamento do Backlog."),
                          (1,"As métricas de estimativa foram pouco e/ou mal utilizadas, dificultando o planejamento e a priorização das tarefas do Backlog, atrapalhando o acompanhamento do progresso do Sprint.")],validators=[DataRequired()])
    
    p36 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p37 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
    p38 = RadioField("Perguntas 13",
                          choices=[
                          (4,""),
                          (3,""),
                          (2,""),
                          (1,"")],validators=[DataRequired()])
    
 
    
    




